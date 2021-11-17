#Riječnici u Pythonu

osoba = {
    "ime" : "Dominik",
    "prezime" : "Ban",
    "dob" : 16
}

print (osoba["ime"])

print (osoba.get("prezime"))

x = osoba.keys()

print(x)

osoba["razred"] = "2.C."

print(osoba.get("razred"))

for x in osoba:
    print(x)

for x in osoba:
    print(osoba[x])

for x in osoba.values():
    print(x)