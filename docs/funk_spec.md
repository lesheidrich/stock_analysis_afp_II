# <p align="center">Funkcionális Specifikáció</p>

## 1. Jelenlegi helyzet leírása

<p align="justify">A megrendelő cégnek tevékenységi köréből adódóan, fontos, hogy naprakészen nyomon követhesse a tőzsde változását és a világpiac alaulását, hogy a munkájukat hatékonyan tudják végezni. A jelenlegi cégen belül használt keresési és nyomon követési módszereket nem tartják elég gyorsnak és hatékonynak. Ennek legnagyobb háránya, hogy a módszer megköveteli az adatok hosszas keresését, a változások nehézkes nyomonkövetését és az adatok papír alapú cseréjét. Mindez negatív hatással van a cég hatékonyságára és az alkalmazottak munkavégzésére.</p>


## 2. Vágyállomrendszer leírása

<p align="justify">Csapatunk egy olyan alkalmazást szeretne készíteni, ami a legfrissebb tőzsdei adatokat kérné le egy adott ticker alapján a felhasználók részére. Célunk egy felhaszálóbarát és letisztult alkalmazás készítése, hogy minél kényelmesebb legyen a tőzsdei folyamatok követése. Az alkalmazás tickerenként a fontosabb pénzügyi mutatókat tenné elérhetővé a felhasználó számára, és azon értékelő műveleteket hajtana végre. Hivatalos dokumentáció is elérhető lenne a felületen keresztül. Továbbá a rendszer tárolná az előző információkat a könnyebb jövőbeli elérhetőség érdekében.</p>

## 3. Jelenlegi üzleti folyamatok modellje

<p align="justify">Az információgyűjtés egy összetett, bonyodalmas és időigényes manuális folyamat. Ezt jó menedzsmenttel és delegációval kezelte eddig ügyfelünk, azonban ez jelentősen megnövelte létszámukat és költségvetésüket. Továbbá tapasztalatuk szerint, a létszám bővülésével nem növekszik azonos mennyiségben a csoporton belüli hatékonyság.</p>

<p align="justify">Amint az alábbi diagram mutatja, a kutató csoport feladata több eszköz segítségével beszerezni a ticker-el kapcsolatos információt. Ezek után a dokumentációs csapat ezt feldolgozza, az információ így a fizikai adatállományukba kerül. Az értékelő csoport a fizikai adatállományban szereplő információt használja a menedzsment számára készített reportokhoz és befektetési stratégiákhoz.</p>

<img width=100%
     src="https://raw.githubusercontent.com/lesheidrich/stock_analysis_afp_II/main/img/docs/kov_spec_jelenlegi_uzleti_folyamatok.jpg" 
     alt="jelenlegi üzleti folyamatok diagram">


## 4. Igényelt üzleti folyamatok modellje

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


## 5. Követelménylista

| Id | Modul | Név | Leírás |
| :---: | --- | --- | --- |
| K1 | GUI | Login | Az felhasználó a felületen keresztül fér hozzá a rendszerhez, és inicializálja az API kulcsot |
| K2 | GUI | Főablak | Megjeleníti az FMP szerkesztősége által kiadott piaci híreket, üdvözlő információkat és keresési lehetőséget biztosít a felhasználónak. |
| K3 | Funkció | Keresés | Ticker használatával rákereshet a felhasználó egy részvényre. A rendszer megjeleníti a főbb pénzügyi mutatókat ezek alapján javaslatot tesz, illetve SEC éves reportokhoz is hozzáférést biztosít |
| K4 | Funkció | Mentés | A felhasználó csv formátumban lementheti az SEC reportokat. |
| K5 | Funkció | Frissítés | Az adott ticker adatait frissíti az adatbázisban. |
| K6 | Funkció | Utoljára megtekintett | Megjeleníti az utoljára megtekintett tickereket, a felhasznó usernévvel együtt. |


## 6. Használati esetek

<p align="justify">

  * **Bejelentkezés:** A felhasználó egy felhasználónév és jelszó megadása után továbbléphet a főoldalra.
  * **Keresés ticker-ek alapján:** A főoldalon megtalálható szövegdobozba egy adott tickert begépelve rákereshet a részvényre és annak adataira, illetve azzal kapcsolatos további javaslatokra, reportokra.
  * **Adatok letöltése:** A felhasználónak lehetősége van a letöltés gomb megnyomása után lementeni a SEC reportokat csv formátumban.
  * **Keresések visszanézése:** A felhasználónak lehetősége van a visszatekintés gombra kattintva megtekinteni, hogy más felhasználók milyen részvényekre kerestek rá korábban.
  * **Frissítés:** Egy frissítés gomb által lehetősége van a felhasználónak frissíteni a részvény adatait az adatbázisban.
</p>


## 7. Megfeleltetés, hogyan fedik le a használati eseteket a követelményeket

| Használati eset | Megfeleltetése |
| :---: | --- |
| Bejelentkezés | A felhasználó a kliens oldal segítségével hozzáférhet a rendszerhez. |
| Keresés | A felhasználó ticker alapján kereshet rá a részvényre. Emellett megjelennek a főbb pénzügyi mutatók és javaslatok. Illetve a SEC éves reportjaihoz is hozzáférést kap.|
| Letöltés | A felhasználó csv formátumban lementheti a SEC reportokat. |
| Keresések visszanézése | A felhasználó könnyedén visszanézheti a legutoljára megtekintett tickereket, illetve a felhasználó usernevét is. |
| Frissítés | A felhasználó frissítheti az adott ticker adatait az adatbázisban. |


## 8. Képernyőtervek
Login
<img src="https://github.com/lesheidrich/stock_analysis_afp_II/blob/main/docs/Pictures/Dia1.JPG?raw=true">
Sign up
<img src="https://github.com/lesheidrich/stock_analysis_afp_II/blob/main/docs/Pictures/Dia2.JPG?raw=true">
Főablak
<img src="https://github.com/lesheidrich/stock_analysis_afp_II/blob/main/docs/Pictures/Dia3.JPG?raw=true">
Információs ablak
<img src="https://github.com/lesheidrich/stock_analysis_afp_II/blob/main/docs/Pictures/Dia4.JPG?raw=true">

## 9. Forgatókönyvek

<p align="justify">Minden felhasználónak a program elindulása után egy bejelentkező felület jelenik meg. Amennyiben még nem regisztrált felhasználó, úgy ezen a felületen a regisztrálj gombra kattintva regisztrálhat is. Sikeres bejelentkezést követően pedig a főoldal jelenik meg.

A főoldalon található egy szövegdoboz, amibe ha beírjuk a keresendő tickert, akkor azt követően megjelennek a részvény adatok és információk. A ticker beírásakor ügyeljünk arra hogy helyesen írjuk azt be, mivel ha elgépeljük, úgy nem megfelelő eredményeket vagy hibaüzenetet kapunk vissza.

Miután megtaláltuk a keresett részvényt, elolvashatjuk annak adatait és a javaslatokat, reportokat. A felhasználónak lehetősége nyílik arra hogy frissítse az adott ticker adatait az adatbázisban. Illetve lehetősége van lementeni a SEC repotokat egy CSV fáljba.</p>



## 10. Funkció - követelmény megfeleltetése

<p align="justify"></p>

| Id | Követelmény | Funkció |
| :---: | --- | --- |
| K1 | Login | Az felhasználó a felületen keresztül fér hozzá a rendszerhez, és inicializálja az API kulcsot |
| K2 | Főablak | Megjeleníti az FMP szerkesztősége által kiadott piaci híreket, üdvözlő információkat és keresési lehetőséget biztosít a felhasználónak. |
| K3 | Keresés | Ticker használatával rákereshet a felhasználó egy részvényre. A rendszer megjeleníti a főbb pénzügyi mutatókat ezek alapján javaslatot tesz, illetve SEC éves reportokhoz is hozzáférést biztosít |
| K4 | Mentés | A felhasználó csv formátumban lementheti az SEC reportokat. |
| K5 | Frissítés | Az adott ticker adatait frissíti az adatbázisban. |
| K6 | Utoljára megtekintett | Megjeleníti az utoljára megtekintett tickereket, a felhasznó usernévvel együtt. |


## 11. Fogalomszótár

<p align="justify">
<ul>
     <li><b>csv:</b> comma separated values, vesszővel elválasztott szöveg alapú táblázat.</li>
     <li><b>Pénzügyi mutató:</b> A pénzügyi mutató egy olyan szám vagy arány, amely a pénzügyi teljesítményt vagy pénzügyi egészséget jellemzi egy vállalat, szervezet 
            vagy egyéni személy esetében.</li>
     <li><b>Real-time:</b> Valós idejű, azonnali.</li>
     <li><b>SEC:</b> Securities and Exchange Commission, az Egyesült Államok kormányának független szerve amely a tőzsdén lévő cégeket felügyeli.</li>
     <li><b>Ticker:</b> A ticker kód egy részvény részvényjegyzéken használt azonosítója. Minden egyedi kód számokból, betűkből, vagy akár mindkettőből áll.</li> 
</ul>
</p>
