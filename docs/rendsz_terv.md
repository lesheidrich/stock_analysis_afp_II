# Rendszerterv
## 1. A rendszer célja

<p>Az alkalmazásunk infromálja a tőzsde után éredklődőket, de a már ebben jártasoknak is segítséget tudjon nyújtani. Felhasználóinknak egy egyszerű, de igényesen elrendezett felületet kínálunk melyen a belépést, vagy az új profil létrehozását megteheti. Ezt követően a felhasználó elolvashatja a híreket vagy ha egy kifejezett tőzsdei tickert. Itt megtekintheti a pénzügyi mutatókat, mentheti a számára fontos tickereket, vagy vissza nézheti a már megtekintetteket.</p>

## 2. Projektterv

### 2.1 Projektszerepkörök, felelőségek:
   * Scrum masters:
     - Matuch Richárd
   * Product owner: Teszt Elek
   * Üzleti szereplő:
     - Megrendelő: Teszt Elek
     
### 2.2 Projektmunkások és felelőségek:
   * Frontend:
     - D. Tóth Gyula Bátor
     - Deme Viktor
     - Heidrich Lóránd
     - Szilágyi Debóra
   * Backend:
     - D. Tóth Gyula Bátor
     - Deme Viktor
     - Heidrich Lóránd
     - Szilágyi Debóra
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
|Program                  |GUI elkészítése                         |         3 |             8 |                      8 |                8 |                   8 |
|Program                  |Adatbázisrendszer létrehozása           |         3 |             8 |                      8 |                8 |                   8 |
|Program                  |Titkosítási funkciók elkészítése        |         3 |             8 |                      8 |                8 |                   8 |
|Program                  |Fájlbaírás / Fájlból olvasás elkészítése|         3 |             8 |                      8 |                8 |                   8 |
|Program                  |Tesztelés                               |         4 |             2 |                      2 |                2 |                   2 |

### 2.4 Mérföldkövek:
   * Dokumentáció megírása
   * Alapfunkciók elkészítése
   * GUI elkészítése
   * Adatbázisrendszer létrehozása
   * Prototípus átadása
   * Tesztelés
   * Esetleges hibák javítása
   * Kész program átadása

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

<p>A rendszer a lokális kliens melett egy API-n keresztül kapcsólódik egy adatbázishoz ahonnan folyamatosan adatokat kér le, így a program internetre kapcsolódás nélkül nem működik. Kétféle jogosultsági kör létezik, admin és felhasználó (user). Ezek jogai között különböző funkciók elérésénél különbséget teszünk.</p>

### 5.2 Menühierarchiák

<p>A szoftver egymásra épülő menürendszert tartalmaz. Az indításkor a felhasználót egy regisztrációs/bejelentkező menü fogadja. A regisztrációs/bejelentkezési lépések elvégzése után a főmenübe kerül a felhasználó. Itt megtalálja az input mezőt, a keresési funkció használatával érhető el a felhasználó számára érdekelt tickerhez kapcsolódó tőzsdei és pénzügyi mutatók menüje. Ebben a menüpontban található a mentés, frissítés illetve az utoljára megtekintett tickerek megnézésének funkciója.</p>

## 6. Fizikai környezet

### Vásárolt softwarekomponensek és külső rendszerek

<p>Nincsenek vásárolt szoftverkomponensek.</p>

### Hardver topológia

<p>Az alkalmazásnak szüksége van internet elérésre. De ezen követelmény teljesülése mellett a 32 és 64 bites Windowson rendszereken egyaránt működik. Amennyiben az a Windows rendszer rendelkezik .NET Frameworkkel.</p>

### Fizikai alrendszerek

<p>Kliens gépek: Olyan gépek melyek képesek Windows futatására alkalmas és internetes hozzáféréssel rendelkeznek.</p>

### Fejlesztő eszközök

<p> Python, a webalkalmazás része főleg</p>

## 8. Architekturális terv

### Webszerver

<p>Az alkalmazásunk folyamatos internet kapcsolatra van szüksége, mert a webszerverünkről hívja le a frissítéseket és kezeli a bejelentkezést.</p>

### Adatbázis rendszer

<p>Az alkalmazásunk folyamatos internet kapcsolatra van szüksége, mert az adatbázishoz szükséges lesz a kapcsolódás.</p>

### A program elérése, kezelése

<p>A programot Windows operációs rendszert futtató és .NET keretrendszerrel rendelkező számítógép futtathatja. A futtatás egyszerű, csak kétszer kell rákattintani az állománynak a parancsikonjára.</p>

## 9. Adatbázis terv

Az adatbázis az AFP API json válaszainak tükörképe. Az adatokat a business logic strukturálja tovább mielőtt REST szolgáltatással továbbküli a kliensnek.

<img src="https://raw.githubusercontent.com/lesheidrich/stock_analysis_afp_II/main/img/docs/adatbazis_terv.jpg" alt="adatbázis terv diagram">


## 10. Implementációs terv

  * Az alkalmazás a Financial Modeling Prep API-t használja az adatbázishoz való csatlakozáshoz, új információ lekéréséhez.
  * A felhasználói felület, kliens GUI - C# window form alkalmazás.
  * Python webszerver, illetve .NET Framework (csak olyan Windows rendszeren futtatható, amely rendelkezik a .NET Framework-el).

## 11. Tesztterv

<p>A tesztelések célja a teljes rendszer beleértve a kliens, az API és az adatbázis funkcionalitásának teljes vizsgálata és ellenőrzése a rendszer által megvalósított üzleti szolgáltatások verifikálása. A teszteléseket a fejlesztő csapat tagjai mind elvégzik. Egymás tesztjeit sorra saját maguk is végrehajtják és felülvizsgálják. A teszt eredményeit a tagok külön fájlokba dokumentálják.</p>

### Tesztesetek

 | Teszteset                                            | Elvárt eredmény | 
 |-----------                                           |-----------------| 
 | Helytelen regisztrációs adatok megadása              | A regisztráció sikertelen lesz, a program hibaüzenetet dob. |
 | Helyes regisztrációs adatok megadása                 | A regisztráció sikeres lesz, a felhasználó bekerül az adatbázisba. |
 | Helytelen/nem létező bejelentkezési adatok megadása  | A bejelentkezés sikertelen lesz, a program hibaüzenetet dob. |
 | Helyes/létező bejelentkezési adatok megadása         | A bejelentkezés sikeres lesz, a felhasználó a főmenübe kerül. |
 | Helytelen/nem létező ticker megadása                 | A keresés sikertelen lesz, a program hibaüzenetet dob, a felhasználó a főmenüben marad. |
 | Helyes/létező ticker megadása                        | A keresés sikeres lesz, a felhasználó megkapja az adott tickerhez tartozó világpiaci és pénzügyi mutatókat. |
 | Mentés funkció használata                            | A felhasználó csv formátumban megkapja az adott tickerhez tartozó világpiaci és pénzügyi mutatókat. |
 | Frissítés funkció használata                         | Az adott ticker adatai frissülnek az adatbázisban. |
 | Utoljára megtekintett funkció használata             | Megjelennek az utoljára megtekintett tickereket, a felhasznó usernévvel együtt. |


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
