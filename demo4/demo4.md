# Demo 4

## Oppimispäiväkirja
Näiden tehtävien kanssa tuli aika isoja ongelmia, sillä onnistuin hieman pieleen
menneellä skriptillä varaamaan kameran jolloin uudet koodipätkät eivät päässeetkään
käyttämään sitä. Turhauttava, mutta ihan hyvä opetus käyttöjärjestelmän toiminnasta.
Sinänsä Motionin kanssa oli helppo tehdä juttuja, kun conf-tiedosto oli niin
kattavasti dokumentoitu.

## Tehtävät
- **[x] Tehtävä 11**, Motion asennettu, sujui ongelmitta.
- **[x] Tehtävä 12**, Motion tallentaa kuvat ja lokin eri tiedostoon kuin oletustiedosto.
  - Vaihdoin Motionin tallennuskansiota vaihtamalla seuraavan rivin:
'''python
target_dir home/pi/Motion
'''
- **[x] Tehtävä 13**, Motion tallentaa 2 kuvaa ennen liikettä ja 5 sekuntia
liikkeen jälkeen
  - Tässä tehtävässä Motionin dokumentaatio oli hyvä apu. Muutin conf-tiedostosta
seuraavat rivit:
'''python
pre_capture 2
post_capture 10
'''
  - Jälkimmäisessä luku on 10, sillä olin asettanut motionin kuvaamaan 2 kuvaa
sekunnissa ja näin sain 5 sekunnin ajalta "videota".
- **[x] Tehtävä 14**
  - Yritin tehdä tehtävän laittamalla skriptin on_motion_detected -riville, mutta
tässä kohtaa tuli ongelmia resurssien kanssa. Lopulta tein sen sitten "helpolla"
tavalla ja muutin vain seuraavaa riviä, jolloin videon pituudeksi tulee 10 s:
'''python
max_movie_time 10
'''