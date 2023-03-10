# Követelmény specifikáció

## 1. Áttekintés

Az 5.5x csapata meg lett bízva egy tőzsde alkalmazás létrehozásával. Ügyfelünk, Warren Buffet, szeretne egy általánosan felhasználható alkalmazást, amely: 
<ul>
  <li>real-time adatokat tud lekérni a tőzsdéről egy adott ticker alapján</li>
  <li>adott tickerek éves színtű pénzügyi mutatóihoz és dokumentumaihoz hozzáférést tesz lehetővé saját rendszeren keresztül is</li>
  <li>kereskedési javaslatokat tesz pénzügyi mutatók alapján</li>
  <li>bejelentkezési lehetőséget biztosít</li>
  <li>lehetőséget ad más felhasználók által megtekintett tickereket is visszanézni</li>
</ul>
Csapatunk büszkén állt a feladat elé. Nálunk okosabb csapatokkal konzultálva létrehoztuk azt az alkalmazás tervet, amely szerény véleményünk szerint az elfogadhatóan sikeres üzletembert immár Elon Musk-szerű magaslatokra emelheti.

## 2. A jelenlegi helyzet leírása

A Berkshire Hathaway tevékenységi köréből adódóan, fontos, hogy naprakészen nyomon követhesse a tőzsde változását és a világpiac alakulását, hogy a munkájukat hatékonyan tudják végezni. A jelenlegi cégen belül használt keresési és nyomon követési módszereket nem tartják elég gyorsnak és hatékonynak. Ennek legnagyobb háránya, hogy a módszer megköveteli az adatok hosszas keresését, a változások nehézkes nyomonkövetését és az adatok papír alapú cseréjét. Mindez negatív hatással van a cég hatékonyságára és az alkalmazottak munkavégzésére.


## 4. Jelenlegi üzleti folyamatok modellje
Az információgyűjtés egy összetett, bonyodalmas és időigényes manuális folyamat. Ezt jó menedzsmenttel és delegációval kezelte eddig ügyfelünk, azonban ez jelentősen megnövelte létszámukat és költségvetésüket. Továbbá tapasztalatuk szerint, a létszám bővülésével nem növekszik azonos mennyiségben a csoporton belüli hatékonyság. 
<br>
Amint az alábbi diagram mutatja, a kutató csoport feladata több eszköz segítségével beszerezni a ticker-el kapcsolatos információt. Ezek után a dokumentációs csapat ezt feldolgozza, az információ így a fizikai adatállományukba kerül. Az értékelő csoport a fizikai adatállományban szereplő információt használja a menedzsment számára készített reportokhoz és befektetési stratégiákhoz.
<br>
<img src="https://raw.githubusercontent.com/lesheidrich/stock_analysis_afp_II/main/img/docs/kov_spec_jelenlegi_uzleti_folyamatok.jpg" alt="jelenlegi üzleti folyamatok diagram">

## 5. Igényelt üzleti folyamatok modellje
Ügyfélünk úgy döntött, hogy kissebb specializált csapatokat és könnyen szemmel követhető folyamatok kiépítésével javíthatják teljesítményüket. Ezt tovább szeretnék fokozni technológiai újításokkal.<br>
A megrendelői elvárás alapját képezi egy olyan alkalmazás, amely:
<ul>
  <li>fő szolgáltatójuk, az FMP szolgáltatásait elérhetővé teszik saját rendszerükön keresztül</li>
  <li>real-time adatokat tud lekérni a tőzsdéről egy adott ticker alapján</li>
  <li>adott tickerek éves színtű pénzügyi mutatóihoz és dokumentumaihoz hozzáférést tesz lehetővé saját rendszeren keresztül is</li>
  <li>kereskedési javaslatokat tesz pénzügyi mutatók alapján</li>
  <li>bejelentkezési lehetőséget biztosít</li>
  <li>lehetőséget ad más felhasználók által megtekintett tickereket is visszanézni</li>
</ul>

