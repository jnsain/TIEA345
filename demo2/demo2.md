# Demo 2

## Oppimispäiväkirja
Tehtävät tuntuivat aluksi vaikeilta, koska siitä kun olen kytkentöjä tehnyt on
pitkä aika ja silloin tuntui vaikealta. Parin ekan tehtävän mallit auttoivat
kuitenkin saamaan juonesta kiinni, joten viimeiset liikennevalotehtävät
sujuivat nopeasti. Mielestäni tehtävä oli todella hyvin suunniteltu myös niitä
ajatellen, joilla asiat olivat unohtuneet. Liikkeentunnistimen käyttäminen
vaikutti omissa ajatuksissa vaikealta, mutta se olikin yllättävän 
yksinkertaista.

## Tehtävät
- **[x] Tehtävä 3**, ledi, [t3.fzz](https://github.com/jnsain/TIEA345/blob/master/demo2/t3.fzz) [d2t3.py](https://github.com/jnsain/TIEA345/blob/master/demo2/d2t3.py)
- **[x] Tehtävä 4**, lue painiketta ja liikkeentunnistinta, [t4.fzz](https://github.com/jnsain/TIEA345/blob/master/demo2/t4.fzz) [d2t4.py](https://github.com/jnsain/TIEA345/blob/master/demo2/d2t4.py)
- **[x] Tehtävä 5**, liikennevalot, [t5.fzz](https://github.com/jnsain/TIEA345/blob/master/demo2/t5.fzz) [d2t5.py](https://github.com/jnsain/TIEA345/blob/master/demo2/d2t5.py)
  - Liikennevalot tein melko pitkälti samaan tapaan kuin kahdessa aiemmassa
  tehtävässä. Yhdistin joka ledin omaan pinniinsä ja käytin tehtävä 4:n
  nappulan toteutusta sellaisenaan. Sitten raspin puolella annoin virtaa
  oikeisiin pinneihin.
- **[x] Bonus 3**, merkkivalo, [bonus3.fzz](https://github.com/jnsain/TIEA345/blob/master/demo2/bonus3.fzz) [d2bonus3.py](https://github.com/jnsain/TIEA345/blob/master/demo2/d2bonus3.py)
- **[x] Bonus 4**, liikkeentunnistin liikennevaloihin, [bonus4.fzz](https://github.com/jnsain/TIEA345/blob/master/demo2/bonus4.fzz) [d2bonus4.py](https://github.com/jnsain/TIEA345/blob/master/demo2/d2bonus4.py)
  - Toteutin edellistehtävän valon vilkuttamisen silmukalla johon tässä
  vaiheessa lisäsin myös liikkeen tunnistamisen. Pieneksi ngelmaksi muodostui se,
  että valon piti vilkkua niin kauan, että vihreä valo on syttynyt, jolloin
  olisi (ainakin tällä toteutuksella) pitänyt samaan aikaan pyörittää silmukkaa 
  ja suorittaa jo toista aliohjelmaa. Toteutin siis vilkutuksen "kahdessa osassa",
  jolloin vilkkujen väliin jää pari riviä koodia, mutta ihmissilmä ei kuitenkaan
  huomaa viivettä. Tähän olisi varmaan voinut olla parempikin ratkaisu :-)