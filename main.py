import csv
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np

mapping_religion: Dict[str, str] = {
    "Afghanistan": "Islamische Länder (>90% Muslime)",
    "Somalia": "Islamische Länder (>90% Muslime)",
    "Marokko": "Islamische Länder (>90% Muslime)",
    "Tunesien": "Islamische Länder (>90% Muslime)",
    "Jemen": "Islamische Länder (>90% Muslime)",
    "Mauretanien": "Islamische Länder (>90% Muslime)",
    "Libyen": "Islamische Länder (>90% Muslime)",
    "Malediven": "Islamische Länder (>90% Muslime)",
    "Iran, Islamische Republik": "Islamische Länder (>90% Muslime)",
    "Türkei": "Islamische Länder (>90% Muslime)",
    "Algerien": "Islamische Länder (>90% Muslime)",
    "Komoren": "Islamische Länder (>90% Muslime)",
    "Dschibuti": "Islamische Länder (>90% Muslime)",
    "Tadschikistan": "Islamische Länder (>90% Muslime)",
    "Irak": "Islamische Länder (>90% Muslime)",
    "Pakistan": "Islamische Länder (>90% Muslime)",
    "Aserbaidschan": "Islamische Länder (>90% Muslime)",
    "Turkmenistan": "Islamische Länder (>90% Muslime)",
    "Niger": "Islamische Länder (>90% Muslime)",
    "Jordanien": "Islamische Länder (>90% Muslime)",
    "Usbekistan": "Islamische Länder (>90% Muslime)",
    "Syrien": "Islamische Länder (>90% Muslime)",
    "Kosovo": "Islamische Länder (>90% Muslime)",
    "Sudan": "Islamische Länder (>90% Muslime)",
    "Sudan (ohne Südsudan) (ab 09.07.2011)": "Islamische Länder (>90% Muslime)",
    "Sudan (einschließlich Südsudan) (bis 08.07.2011)": "Islamische Länder (>90% Muslime)",
    "Senegal": "Islamische Länder (>90% Muslime)",
    "Saudi-Arabien": "Islamische Länder (>90% Muslime)",
    "Ägypten": "Islamische Länder (>90% Muslime)",
    "Oman": "Islamische Länder (>50% Muslime)",
    "Bangladesch": "Islamische Länder (>50% Muslime)",
    "Gambia": "Islamische Länder (>50% Muslime)",
    "Mali": "Islamische Länder (>50% Muslime)",
    "Kirgisistan": "Islamische Länder (>50% Muslime)",
    "Guinea": "Islamische Länder (>50% Muslime)",
    "Kuwait": "Islamische Länder (>50% Muslime)",
    "Palästinensische Gebiete": "Islamische Länder (>50% Muslime)",
    "Bahrain": "Islamische Länder (>50% Muslime)",
    "Indonesien": "Islamische Länder (>50% Muslime)",
    "Katar": "Islamische Länder (>50% Muslime)",
    "Vereinigte Arabische Emirate": "Islamische Länder (>50% Muslime)",
    "Kasachstan": "Islamische Länder (>50% Muslime)",
    "Sierra Leone": "Islamische Länder (>50% Muslime)",
    "Libanon": "Islamische Länder (>50% Muslime)",
    "Albanien": "Islamische Länder (>50% Muslime)",
    "Brunei Darussalam": "Islamische Länder (>50% Muslime)",
    "Malaysia": "Islamische Länder (>50% Muslime)",
    "Tschad": "Islamische Länder (>50% Muslime)",
    "Burkina Faso": "Islamische Länder (>50% Muslime)",
    "Eritrea": "Islamische Länder (>50% Muslime)",
    "Bosnien und Herzegowina": "Sonstige Länder (<50% Muslime)",
    "Nigeria": "Sonstige Länder (<50% Muslime)",
    "Guinea-Bissau": "Sonstige Länder (<50% Muslime)",
    "Cote d'Ivoire": "Sonstige Länder (<50% Muslime)",
    "Äthiopien": "Sonstige Länder (<50% Muslime)",
    "Nordmazedonien": "Sonstige Länder (<50% Muslime)",
    "Tansania": "Sonstige Länder (<50% Muslime)",
    "Benin": "Sonstige Länder (<50% Muslime)",
    "Zypern": "Sonstige Länder (<50% Muslime)",
    "Kamerun": "Sonstige Länder (<50% Muslime)",
    "Israel": "Sonstige Länder (<50% Muslime)",
    "Togo": "Sonstige Länder (<50% Muslime)",
    "Ghana": "Sonstige Länder (<50% Muslime)",
    "Mosambik": "Sonstige Länder (<50% Muslime)",
    "Montenegro (ab 03.06.2006)": "Sonstige Länder (<50% Muslime)",
    "Mauritius": "Sonstige Länder (<50% Muslime)",
    "Liberia": "Sonstige Länder (<50% Muslime)",
    "Suriname": "Sonstige Länder (<50% Muslime)",
    "Singapur": "Sonstige Länder (<50% Muslime)",
    "Indien": "Sonstige Länder (<50% Muslime)",
    "Malawi": "Sonstige Länder (<50% Muslime)",
    "Zentralafrikanische Republik": "Sonstige Länder (<50% Muslime)",
    "Bulgarien": "Sonstige Länder (<50% Muslime)",
    "Russische Föderation": "Sonstige Länder (<50% Muslime)",
    "Uganda": "Sonstige Länder (<50% Muslime)",
    "Georgien": "Sonstige Länder (<50% Muslime)",
    "Gabun": "Sonstige Länder (<50% Muslime)",
    "Sri Lanka": "Sonstige Länder (<50% Muslime)",
    "Frankreich": "Sonstige Länder (<50% Muslime)",
    "Schweden": "Sonstige Länder (<50% Muslime)",
    "Kenia": "Sonstige Länder (<50% Muslime)",
    "Guyana": "Sonstige Länder (<50% Muslime)",
    "Belgien": "Sonstige Länder (<50% Muslime)",
    "Niederlande": "Sonstige Länder (<50% Muslime)",
    "Österreich": "Sonstige Länder (<50% Muslime)",
    "Serbien": "Sonstige Länder (<50% Muslime)",
    "Serbien (einschl. Kosovo) (03.06.2006-16.02.2008)": "Sonstige Länder (<50% Muslime)",
    "Serbien und Montenegro (05.02.2003-02.06.2006)": "Sonstige Länder (<50% Muslime)",
    "Trinidad und Tobago": "Sonstige Länder (<50% Muslime)",
    "Vereinigtes Königreich": "Sonstige Länder (<50% Muslime)",
    "Liechtenstein": "Sonstige Länder (<50% Muslime)",
    "Deutschland": "Sonstige Länder (<50% Muslime)",
    "Südsudan (ab 09.07.2011)": "Sonstige Länder (<50% Muslime)",
    "Schweiz": "Sonstige Länder (<50% Muslime)",
    "Fidschi": "Sonstige Länder (<50% Muslime)",
    "Thailand": "Sonstige Länder (<50% Muslime)",
    "Griechenland": "Sonstige Länder (<50% Muslime)",
    "Philippinen": "Sonstige Länder (<50% Muslime)",
    "Dänemark": "Sonstige Länder (<50% Muslime)",
    "Norwegen": "Sonstige Länder (<50% Muslime)",
    "Mongolei": "Sonstige Länder (<50% Muslime)",
    "Ruanda": "Sonstige Länder (<50% Muslime)",
    "Italien": "Sonstige Länder (<50% Muslime)",
    "Nepal": "Sonstige Länder (<50% Muslime)",
    "Äquatorialguinea": "Sonstige Länder (<50% Muslime)",
    "Myanmar": "Sonstige Länder (<50% Muslime)",
    "Slowenien": "Sonstige Länder (<50% Muslime)",
    "Timor-Leste": "Sonstige Länder (<50% Muslime)",
    "Kanada": "Sonstige Länder (<50% Muslime)",
    "Australien": "Sonstige Länder (<50% Muslime)",
    "Spanien": "Sonstige Länder (<50% Muslime)",
    "Cabo Verde": "Sonstige Länder (<50% Muslime)",
    "Luxemburg": "Sonstige Länder (<50% Muslime)",
    "Palau": "Sonstige Länder (<50% Muslime)",
    "Argentinien": "Sonstige Länder (<50% Muslime)",
    "Madagaskar": "Sonstige Länder (<50% Muslime)",
    "Burundi": "Sonstige Länder (<50% Muslime)",
    "Finnland": "Sonstige Länder (<50% Muslime)",
    "Malta": "Sonstige Länder (<50% Muslime)",
    "Kambodscha": "Sonstige Länder (<50% Muslime)",
    "Kroatien": "Sonstige Länder (<50% Muslime)",
    "China": "Sonstige Länder (<50% Muslime)",
    "Südafrika": "Sonstige Länder (<50% Muslime)",
    "Ukraine": "Sonstige Länder (<50% Muslime)",
    "Kongo, Demokratische Republik": "Sonstige Länder (<50% Muslime)",
    "Neuseeland": "Sonstige Länder (<50% Muslime)",
    "St. Vincent und die Grenadinen": "Sonstige Länder (<50% Muslime)",
    "Vereinigte Staaten": "Sonstige Länder (<50% Muslime)",
    "Hongkong": "Sonstige Länder (<50% Muslime)",
    "Andorra": "Sonstige Länder (<50% Muslime)",
    "Kongo, Republik": "Sonstige Länder (<50% Muslime)",
    "Irland": "Sonstige Länder (<50% Muslime)",
    "Angola": "Sonstige Länder (<50% Muslime)",
    "Sambia": "Sonstige Länder (<50% Muslime)",
    "Barbados": "Sonstige Länder (<50% Muslime)",
    "Seychellen": "Sonstige Länder (<50% Muslime)",
    "Simbabwe": "Sonstige Länder (<50% Muslime)",
    "Panama": "Sonstige Länder (<50% Muslime)",
    "Eswatini": "Sonstige Länder (<50% Muslime)",
    "Antigua und Barbuda": "Sonstige Länder (<50% Muslime)",
    "Moldau, Republik": "Sonstige Länder (<50% Muslime)",
    "Belize": "Sonstige Länder (<50% Muslime)",
    "St. Lucia": "Sonstige Länder (<50% Muslime)",
    "Monaco": "Sonstige Länder (<50% Muslime)",
    "Taiwan": "Sonstige Länder (<50% Muslime)",
    "Rumänien": "Sonstige Länder (<50% Muslime)",
    "Portugal": "Sonstige Länder (<50% Muslime)",
    "Marshallinseln": "Sonstige Länder (<50% Muslime)",
    "Venezuela, Bolivarische Republik": "Sonstige Länder (<50% Muslime)",
    "Ungarn": "Sonstige Länder (<50% Muslime)",
    "Belarus": "Sonstige Länder (<50% Muslime)",
    "Namibia": "Sonstige Länder (<50% Muslime)",
    "Botsuana": "Sonstige Länder (<50% Muslime)",
    "Lettland": "Sonstige Länder (<50% Muslime)",
    "Estland": "Sonstige Länder (<50% Muslime)",
    "Salomonen": "Sonstige Länder (<50% Muslime)",
    "Grenada": "Sonstige Länder (<50% Muslime)",
    "St. Kitts und Nevis": "Sonstige Länder (<50% Muslime)",
    "Japan": "Sonstige Länder (<50% Muslime)",
    "Vietnam": "Sonstige Länder (<50% Muslime)",
    "Honduras": "Sonstige Länder (<50% Muslime)",
    "Armenien": "Sonstige Länder (<50% Muslime)",
    "Macau": "Sonstige Länder (<50% Muslime)",
    "Island": "Sonstige Länder (<50% Muslime)",
    "Mexiko": "Sonstige Länder (<50% Muslime)",
    "Korea, Republik": "Sonstige Länder (<50% Muslime)",
    "Polen": "Sonstige Länder (<50% Muslime)",
    "Kolumbien": "Sonstige Länder (<50% Muslime)",
    "Chile": "Sonstige Länder (<50% Muslime)",
    "Tschechien": "Sonstige Länder (<50% Muslime)",
    "Kuba": "Sonstige Länder (<50% Muslime)",
    "Laos, Demokratische Volksrepublik": "Sonstige Länder (<50% Muslime)",
    "Paraguay": "Sonstige Länder (<50% Muslime)",
    "Litauen": "Sonstige Länder (<50% Muslime)",
    "Haiti": "Sonstige Länder (<50% Muslime)",
    "Jamaika": "Sonstige Länder (<50% Muslime)",
    "Lesotho": "Sonstige Länder (<50% Muslime)",
    "Bahamas": "Sonstige Länder (<50% Muslime)",
    "Dominica": "Sonstige Länder (<50% Muslime)",
    "Tuvalu": "Sonstige Länder (<50% Muslime)",
    "Brasilien": "Sonstige Länder (<50% Muslime)",
    "Korea, Demokratische Volksrepublik": "Sonstige Länder (<50% Muslime)",
    "Bolivien, Plurinationaler Staat": "Sonstige Länder (<50% Muslime)",
    "Dominikanische Republik": "Sonstige Länder (<50% Muslime)",
    "Ecuador": "Sonstige Länder (<50% Muslime)",
    "Papua-Neuguinea": "Sonstige Länder (<50% Muslime)",
    "Bhutan": "Sonstige Länder (<50% Muslime)",
    "El Salvador": "Sonstige Länder (<50% Muslime)",
    "Guatemala": "Sonstige Länder (<50% Muslime)",
    "Nicaragua": "Sonstige Länder (<50% Muslime)",
    "Peru": "Sonstige Länder (<50% Muslime)",
    "Puerto Rico": "Sonstige Länder (<50% Muslime)",
    "Costa Rica": "Sonstige Länder (<50% Muslime)",
    "Slowakei": "Sonstige Länder (<50% Muslime)",
    "Uruguay": "Sonstige Länder (<50% Muslime)",
    "Samoa": "Sonstige Länder (<50% Muslime)",
    "Sao Tome und Principe": "Sonstige Länder (<50% Muslime)",
    "Vanuatu": "Sonstige Länder (<50% Muslime)",
    "San Marino": "Sonstige Länder (<50% Muslime)",
    "Kiribati": "Sonstige Länder (<50% Muslime)",
    "Mikronesien, Föderierte Staaten von": "Sonstige Länder (<50% Muslime)",
    "Nauru": "Sonstige Länder (<50% Muslime)",
    "Tonga": "Sonstige Länder (<50% Muslime)",
    "Vatikanstadt": "Sonstige Länder (<50% Muslime)",
    "Britische Überseegebiete": "Sonstige Länder (<50% Muslime)",
    "Jugoslawien, Soz. Föd. Republik (bis 26.04.1992)": "Sonstige Länder (<50% Muslime)",
    "Jugoslawien, Bundesrep. (27.04.1992-04.02.2003)": "Sonstige Länder (<50% Muslime)",
    "Sowjetunion (bis 25.12.1991)": "Sonstige Länder (<50% Muslime)",
    "Tschechoslowakei (bis 31.12.1992)": "Sonstige Länder (<50% Muslime)",
    "Staatenlos": "Staatenlos",
    "Ungeklärt / Ohne Angabe": "Ungeklärt / Ohne Angabe",
}
# cf.: https://de.wikipedia.org/wiki/Liste_der_L%C3%A4nder_nach_muslimischer_Bev%C3%B6lkerung
mapping_religion_colors: Dict[str, str] = {
    "Islamische Länder (>90% Muslime)": "darkgreen",
    "Islamische Länder (>50% Muslime)": "limegreen",
    "Sonstige Länder (<50% Muslime)": "dodgerblue",
    "Staatenlos": "red",
    "Ungeklärt / Ohne Angabe": "gray",
    "Andere": "tab:brown",
}
apply_mapping_religion = False

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
        if apply_mapping_religion:
            country = mapping_religion[country]
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
        if country not in data[year]:
            data[year][country] = 0
        data[year][country] += naturalizations

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
    if apply_mapping_religion:
        p = ax.bar(years, naturalizations, label=label, bottom=bottom, color=mapping_religion_colors[country])
    else:
        p = ax.bar(years, naturalizations, label=label, bottom=bottom)
    bottom += naturalizations

displayed_characteristic: str = "Staatsbürgerschaft"
if apply_mapping_religion:
    displayed_characteristic: str = "Religion"
ax.set_title(f"Einbürgerungen von Ausländern in Deutschland nach {displayed_characteristic}\n"
             f"{min(years)} - {max(years)} (insg. {sum_all_totals:_} Stck.)")
ax.legend(loc="upper center", prop={'size': 8})

plt.show()

