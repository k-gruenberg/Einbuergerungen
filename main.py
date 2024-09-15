import csv
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np

# Jahr -> Staatsangehörigkeit -> Anzahl Einbürgerungen
data: Dict[int, Dict[str, int]] = {}

# Staatsangehörigkeit -> Anzahl Einbürgerungen insg. in allen Jahren
countries_totals: Dict[str, int] = {}

# Jahr;Staatsangehörigkeit;männlich;weiblich;Insgesamt
# © Statistisches Bundesamt (Destatis), 2024
# Stand: 15.09.2024 / 23:31:47
with open('12511-0003.csv', newline='', encoding='ISO-8859-1') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        [year, country, _m, _f, naturalizations] = row
        if country == "Insgesamt":
            continue
        if naturalizations == "-":
            naturalizations = 0
        else:
            naturalizations = int(naturalizations)
        if country not in countries_totals:
            countries_totals[country] = 0
        countries_totals[country] += naturalizations
        year = int(year)
        if year not in data:
            data[year] = dict()
        data[year][country] = naturalizations

countries: List[str] = list(countries_totals.keys())
countries_sorted_desc_by_total: List[str] =\
    sorted(countries, key=lambda c: countries_totals[c], reverse=True)

sum_all_totals: int = sum(countries_totals.values())
print(f"Insgesamt gab es von 2000-2023 {sum_all_totals:_} Einbürgerungen.")

print("Länder nach Gesamtzahl der Einbürgerungen 2000-2023:")
for country in countries_sorted_desc_by_total:
    print(f"{country}: {countries_totals[country]:_} ({100.0*countries_totals[country]/sum_all_totals:0.2f}%)")

no_of_displayed_countries: int = 9
displayed_countries: List[str] =\
    countries_sorted_desc_by_total[:no_of_displayed_countries]

print(f"Dargestellte Länder: {displayed_countries}")

for year in data.keys():
    sum_others: int = sum(data[year][c] for c in data[year] if c not in displayed_countries)
    print(f'Anzahl "Andere" im Jahr {year}: {sum_others:_}')
    data[year]["Andere"] = sum_others

countries_totals["Andere"] = sum(countries_totals[c] for c in countries if c not in displayed_countries)

countries = displayed_countries + ["Andere"]

years: List[int] = list(data.keys())
naturalizations_per_country: Dict[str, List[int]] =\
    {country: [data[year][country] for year in years] for country in countries}

fig, ax = plt.subplots()
bottom = np.zeros(len(years))

for country, naturalizations in naturalizations_per_country.items():
    label = country + f" ({100.0*countries_totals[country]/sum_all_totals:0.2f}%)"
    p = ax.bar(years, naturalizations, label=label, bottom=bottom)
    bottom += naturalizations

ax.set_title(f"Einbürgerungen von Ausländern in Deutschland nach Staatsbürgerschaft\n"
             f"{min(years)} - {max(years)} (insg. {sum_all_totals:_} Stck.)")
ax.legend(loc="upper center", prop={'size': 8})

plt.show()

