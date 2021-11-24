#Rad s datotekama

with open("podatci.txt", "r", encoding="utf-8") as podatci_file:
    sadrzaj = podatci_file.read()
    print(sadrzaj)

with open("podatci.txt", "w", encoding="utf-8") as podatci_file:
    podatci_file.write("Pozdrav, ")
with open("podatci.txt", "a", encoding="utf-8") as podatci_file:
    podatci_file.write("Rap, Hip-Hop, Drill, Jazz, Blues, Trap, Dubstep, Country, Pop, Rock, Heavy Metal")

with open("korisnici.txt", "r", encoding="utf-8") as korisnici_file:
    k_lines = korisnici_file.read().splitlines()

    for line in k_lines:
        print(line)
