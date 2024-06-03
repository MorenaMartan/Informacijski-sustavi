# SalonSync 
SalonSync je web aplikacija za praćenje ponude u salonu.
## Funkcionalnosti
### Osnovne funkcionalnosti
1. Dodaj uslugu
2. Pogledaj usluge
3. Uredi usluge
4. Izbriši usluge


----
## Struktura
Omogućeno je dodavanje, pregledavanje, izmjenjivanje te brisanje usluga. 

----
## Pokretanje
- Preuzeti sve datoteke s Githuba i spremiti ih u mapu
- Putem naredbenog retka pozicionirati se u mapu iz prethodnog koraka
- Pomoću naredbe:
```
docker build -t salonsync .
``` 
izraditi docker image
- Pomoću naredbe: 
```
docker run -p 5000:5000 salonsync 
```
pokrenuti konteiner pomoću stvorenog image-a
- Otvoriti preglednik: http://localhost:5000
