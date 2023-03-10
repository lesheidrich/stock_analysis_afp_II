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

Megrendelőnk, Warren Buffet, öregszik. Remeg a keze néha, nehéz neki begépelni a túlnagyított Chrome alkalmazásba egyenként az áhított pénzügyi információkat. OCD-je révén ezt napi többször meg kell tennie.
<br>
Továbbá feledékeny, így újra és újra ki kell keresse ezt az információt. Ez óriási bandwith-t igényel. A nagy embernek rengeteg ideje elmegy így fölöslegesen. Továbbá meg van győződve, hogy figyelik. Így szüksége lenne arra, hogy lássa milyen pénzügyi információ volt kikeresve a rendszerből eddig.
<br>
Egy biztonságos rendszerre lenne szüksége, ahol előző információkat meg lehet jeleníteni. 
