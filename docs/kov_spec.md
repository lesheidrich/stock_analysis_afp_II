# <p align="center">Követelmény Specifikáció</p>

## 1. Áttekintés

<p align="justify">Az 5.5x csapata meg lett bízva egy tőzsde alkalmazás létrehozásával. Ügyfelünk, Warren Buffet, szeretne egy általánosan felhasználható alkalmazást, amely modernizálná a Berkshire Hathaway munkafolyamatait. Az alkalmazástól javult információhozzáférést, biztonsági mentéseket, illetve gyorsabb munkafolyamatokat vár a mengrendelő.</p>
<p align="justify">Csapatunk büszkén állt a feladat elé. Nálunk okosabb csapatokkal konferálva létrehoztuk azt az alkalmazás tervet, amely szerény véleményünk szerint az elfogadhatóan sikeres üzletembert immár Elon Musk-szerű magaslatokra emelheti.</p>


## 2. A jelenlegi helyzet leírása

<p align="justify">A Berkshire Hathaway tevékenységi köréből adódóan, fontos, hogy naprakészen nyomon követhesse a tőzsde változását és a világpiac alakulását, hogy a munkájukat hatékonyan tudják végezni. A jelenlegi cégen belül használt keresési és nyomon követési módszereket nem tartják elég gyorsnak és hatékonynak. Ennek legnagyobb háránya, hogy a módszer megköveteli az adatok hosszas keresését, a változások nehézkes nyomonkövetését és az adatok papír alapú cseréjét. Mindez negatív hatással van a cég hatékonyságára és az alkalmazottak munkavégzésére.</p>


## 3. Vágyálomrendszer

<p align="justify">Csapatunk egy olyan alkalmazást szeretne készíteni, ami a legfrissebb tőzsdei adatokat kérné le egy adott ticker alapján a felhasználók részére. Célunk egy felhaszálóbarát és letisztult alkalmazás készítése, hogy minél kényelmesebb legyen a tőzsdei folyamatok követése. Az alkalmazás tickerenként a fontosabb pénzügyi mutatókat tenné elérhetővé a felhasználó számára, és azon értékelő műveleteket hajtana végre. Hivatalos dokumentáció is elérhető lenne a felületen keresztül. Továbbá a rendszer tárolná az előző információkat a könnyebb jövőbeli elérhetőség érdekében.</p>


## 4. Jelenlegi üzleti folyamatok modellje

<p align="justify">Az információgyűjtés egy összetett, bonyodalmas és időigényes manuális folyamat. Ezt jó menedzsmenttel és delegációval kezelte eddig ügyfelünk, azonban ez jelentősen megnövelte létszámukat és költségvetésüket. Továbbá tapasztalatuk szerint, a létszám bővülésével nem növekszik azonos mennyiségben a csoporton belüli hatékonyság.</p>

<p align="justify">Amint az alábbi diagram mutatja, a kutató csoport feladata több eszköz segítségével beszerezni a ticker-el kapcsolatos információt. Ezek után a dokumentációs csapat ezt feldolgozza, az információ így a fizikai adatállományukba kerül. Az értékelő csoport a fizikai adatállományban szereplő információt használja a menedzsment számára készített reportokhoz és befektetési stratégiákhoz.</p>

<img width=100%
     src="https://raw.githubusercontent.com/lesheidrich/stock_analysis_afp_II/main/img/docs/kov_spec_jelenlegi_uzleti_folyamatok.jpg" 
     alt="jelenlegi üzleti folyamatok diagram">


## 5. Igényelt üzleti folyamatok modellje

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


## 6. Követelménylista

<p align="justify"></p>


## 7. Fogalomtár

<p align="justify">
<ul>
     <li><b>Pénzügyi mutató:</b> A pénzügyi mutató egy olyan szám vagy arány, amely a pénzügyi teljesítményt vagy pénzügyi egészséget jellemzi egy vállalat, szervezet vagy egyéni személy esetében.</li>
     <li><b>Ticker:</b> A ticker kód egy részvény részvényjegyzéken használt azonosítója. Minden egyedi kód számokból, betűkből, vagy akár mindkettőből áll.</li>

     <li></li>
     <li></li>
     <li></li>
     <li></li>
     <li></li>
     <li></li>
</ul>

</p>
