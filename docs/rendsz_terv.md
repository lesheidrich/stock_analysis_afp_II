# Rendszerterv
## 1. A rendszer célja

## 2. Projektterv

### 2.1 Projektszerepkörök, felelőségek:
   * Scrum masters:
     - Matuch Richárd
   * Product owner: Teszt Elek
   * Üzleti szereplő:
     - Megrendelő: Teszt Elek
     
### 2.2 Projektmunkások és felelőségek:
   * Frontend:
   * Backend:
   * Tesztelés:
     - D. Tóth Gyula Bátor
     - Deme Viktor
     - Heidrich Lóránd
     - Szilágyi Debóra
     
### 2.3 Ütemterv:

|Funkció                  | Feladat                                | Prioritás | Becslés (nap) | Aktuális becslés (nap) | Eltelt idő (nap) | Becsült idő (nap) |
|-------------------------|----------------------------------------|-----------|---------------|------------------------|------------------|---------------------|
|Követelmény specifikáció |Megírás                                 |         1 |             1 |                      1 |                1 |                   1 |             
|Funkcionális specifikáció|Megírás                                 |         1 |             1 |                      1 |                1 |                   1 |
|Rendszerterv             |Megírás                                 |         1 |             1 |                      1 |                1 |                   1 |
|Program                  |Képernyőtervek elkészítése              |         2 |             1 |                      1 |                1 |                   1 |
|Program                  |Prototípus elkészítése                  |         3 |             8 |                      8 |                8 |                   8 |
|Program                  |Alapfunkciók elkészítése                |         3 |             8 |                      8 |                8 |                   8 |
|Program                  |Titkosítási funkciók elkészítése        |         3 |             8 |                      8 |                8 |                   8 |
|Program                  |Fájlbaírás / Fájlból olvasás elkészítése|         3 |             8 |                      8 |                8 |                   8 |
|Program                  |Tesztelés                               |         4 |             2 |                      2 |                2 |                   2 |

### 2.4 Mérföldkövek:
   * Prototípus átadása

## 3. Üzleti folyamatok modellje

### 3.1 Üzleti szereplők

<p>A rendszert regisztráció után bárki használhatja. Akármelyik felhasználó aki elvégezte a regisztrációs lépéseket a szoftvert mindenféle korlátozás nélkül használhatja. Annak eldöntése, hogy a szoftver kinek az eszközére települ és ki használhatja azt a megrendelő vállalat dönti el.</p>

### 3.2 Üzleti folyamatok

<p>Ügyfélünk úgy döntött, hogy kissebb specializált csapatokat és könnyen szemmel követhető folyamatok kiépítésével javíthatják teljesítményüket. Ezt tovább szeretnék fokozni technológiai újításokkal.</p>

<p>A megrendelői elvárás alapját képezi egy olyan alkalmazás, amely:
<ul>
  <li>fő szolgáltatójuk, az FMP szolgáltatásait elérhetővé teszik saját rendszerükön keresztül</li>
  <li>real-time adatokat tud lekérni a tőzsdéről egy adott ticker alapján</li>
  <li>adott tickerek éves színtű pénzügyi mutatóihoz és dokumentumaihoz hozzáférést tesz lehetővé saját rendszeren keresztül is</li>
  <li>kereskedési javaslatokat tesz pénzügyi mutatók alapján</li>
  <li>bejelentkezési lehetőséget biztosít</li>
  <li>lehetőséget ad más felhasználók által megtekintett tickereket is visszanézni</li>
</ul>
</p>

<img width=100%
     src="https://raw.githubusercontent.com/lesheidrich/stock_analysis_afp_II/main/img/docs/kov_spec_igenyelt_uzleti_foly.jpg" 
     alt="igényelt üzleti folyamatok diagram">

## 4. Követelmények

### Funkcionális követelmények

| ID | Megnevezés | Leírás |
| :---: | --- | --- |
| K1 | Bejelentkezés | A felhasználó a kliens oldal segítségével hozzáférhet a rendszerhez. |
| K2 | Keresés | A felhasználó ticker alapján kereshet rá a részvényre. Emellett megjelennek a főbb pénzügyi mutatók és javaslatok. Illetve a SEC éves reportjaihoz is hozzáférést kap.|
| K3 | Letöltés | A felhasználó csv formátumban lementheti a SEC reportokat. |
| K4 | Keresések visszanézése | A felhasználó könnyedén visszanézheti a legutoljára megtekintett tickereket, illetve a felhasználó usernevét is. |
| K5 | Frissítés | A felhasználó frissítheti az adott ticker adatait az adatbázisban. |

### Nemfunkcionális követelmények

| ID | Megnevezés | Leírás |
| --- | --- | --- |
| K6 | Letisztult megjelenés | A program megjelenése legyen könnyedén áttekinthető és letisztult. Törekedni kell az egyértelmű és kényelmes megoldásokra. |
| K7 | Gyorsaság | Fontos, hogy az adatok frissítésénél és letöltésénél, illetve maga a program gyors működése a részvények gyors váltakozása miatt.|

### Támogatott eszközök
<p align="justify">Python webszerver, illetve .NET Framework (csak olyan Windows rendszeren futtatható, amely rendelkezik a .NET Framework-el).</p>

## 5. Funkcionális terv

### 5.1 Rendszerszereplők

<p>A rendszer a lokális kliens melett egy API-n keresztül kapcsólódik egy adatbázishoz ahonnan folyamatosan adatokat kér le, így a program internetre kapcsolódás nélkül nem működik. Kétféle jogosultsági kör létezik, admin és felhasználó (user). Ezek jogai között, különböző funkciók elérésénél különbséget teszünk</p>

### 5.2 Menühierarchiák

## 6. Fizikai környezet

### Vásárolt softwarekomponensek és külső rendszerek

### Hardver topológia

### Fizikai alrendszerek

### Fejlesztő eszközök

## 8. Architekturális terv

### Webszerver

### Adatbázis rendszer

### A program elérése, kezelése

## 9. Adatbázis terv

Az adatbázis az AFP API json válaszainak tükörképe. Az adatokat a business logic strukturálja tovább mielőtt REST szolgáltatással továbbküli a kliensnek.

<img src="https://raw.githubusercontent.com/lesheidrich/stock_analysis_afp_II/main/img/docs/adatbazis_terv.jpg" alt="adatbázis terv diagram">


## 10. Implementációs terv

## 11. Tesztterv

### Tesztesetek

 | Teszteset | Elvárt eredmény | 
 |-----------|-----------------| 
 | ... | ... |

### A tesztelési jegyzőkönyv kitöltésére egy sablon:

**Tesztelő:** Vezetéknév Keresztnév

**Tesztelés dátuma:** Év.Hónap.Nap

Tesztszám | Rövid leírás | Várt eredmény | Eredmény | Megjegyzés
----------|--------------|---------------|----------|-----------
például. Teszt #01 | Regisztráció | A felhasználó az adatok megadásával sikeresen regisztrálni tud  | A felhasználó sikeresen regisztrált | Nem találtam problémát.
... | ... | ... | ... | ...

## 12. Telepítési terv
<p align="justify">A szoftver telepítéséhez szükségünk van egy 32 bites Windows rendszerű számítógépre, illetve szükségünk van kialakítani egy megfelelő adatbázist a webszerverhez, ezáltal internetre is szükségünk lesz.</p>

## 13. Karbantartási terv
<p align="justify">Fontos ellenőrizni:</p>
<p>
<ul>
  <li>Az adatok frissülnek az adatbázisban</li>
  <li>A program nem lassul be</li>
  <li>A bejelentkezés és regisztráció jól működik</li>
  <li>A dokumentumok jól töltődnek le</li>
  <li>Kinézet és jó megjelenítés</li>
</ul>

Illetve figyelembe kell venni a felhasználók által kapott visszajelzéseket. Ha valamilyen hibát talál, azt mielőbb ki kell javítani. 
</p>
