# Z podanego zbioru danych wyselekcjonuj 5 o największej wartości na jednostkę, znając kategorię obiektu
# Dane znajdują się w folderze "dane" w pliku "zbiór_wejściowy.json" oraz "kategorie.json"
# Wynik przedstaw w czytelnej formie na standardowym wyjściu
# Polecenie rozumiem jako wypisanie ze zbioru wejściowego informacji o 5 najdroższych surowcach za jednostkę (uncję),
# bo zastanawiałem się także nad interpretacją z największą wartością posiadanego surowca przez danego właściciela
import json

with open("dane/zbiór_wejściowy.json", "r") as file:
    zbior_wejsciowy = json.load(file)

with open("dane/kategorie.json", "r") as file:
    kategorie = json.load(file)

def masa_na_uncje(masa):
    if "ct" in masa:
        masa = float(masa.replace("ct", "").replace(",", "."))
        return masa * 0.007054792
    elif "g" in masa:
        masa = float(masa.replace("g", "").replace(",", "."))
        return masa * 0.0352739619

typ_czystosc_wartosc = {}
for item in kategorie:
    typ_czystosc_wartosc[(item["Typ"], item["Czystość"])] = item["Wartość za uncję (USD)"]


obiekty_z_wartosciami = []


for obiekt in zbior_wejsciowy:
    masa = masa_na_uncje(obiekt["Masa"])
    if (obiekt["Typ"], obiekt["Czystość"]) in typ_czystosc_wartosc:
        wartosc_za_uncje = typ_czystosc_wartosc[(obiekt["Typ"], obiekt["Czystość"])]
        wartosc_wlasciciela = round(masa * wartosc_za_uncje, 2)
        obiekty_z_wartosciami.append((obiekt, wartosc_za_uncje, wartosc_wlasciciela))    

obiekty_z_wartosciami.sort(key=lambda x: x[1], reverse=True)
najlepsze = obiekty_z_wartosciami[:5]

print("5 danych o największej wartości na jednostkę:\n")
print(f"{'':<5} {'Typ':<10} {'Czystość':<12} {'Wartość za uncję (USD)':<25} {'Barwa':<15} {'Pochodzenie':<15} {'Właściciel':<30} {'Masa':<10} {'Wartość posiadanego surowca (USD)':<20}")
print('-' * 150)
for i, element in enumerate(najlepsze, start=1):
    obiekt = element[0]
    wartosc_za_uncje = element[1]
    wartosc_wlasciciela = element[2]

    print(f"{i:<5} {obiekt['Typ']:<10} {obiekt['Czystość']:<12} "
          f"{wartosc_za_uncje:<25} {obiekt['Barwa']:<15} {obiekt['Pochodzenie']:<15} "
          f"{obiekt['Właściciel']:<30} {obiekt['Masa']:<10} {wartosc_wlasciciela:<20}")

print('-' * 150)
