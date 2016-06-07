import RPi.GPIO as GPIO
import time

AUTOVIHREA=5
AUTOKELTAINEN=6
AUTOPUNAINEN=13
JALKAVIHREA=20
JALKAPUNAINEN=16
JALKAKELTAINEN=23
PAINIKE=27
PIR=18

GPIO.setmode (GPIO.BCM)
GPIO.setup (AUTOVIHREA, GPIO.OUT)
GPIO.setup (AUTOKELTAINEN, GPIO.OUT)
GPIO.setup (AUTOPUNAINEN, GPIO.OUT)
GPIO.setup (JALKAVIHREA, GPIO.OUT)
GPIO.setup (JALKAPUNAINEN, GPIO.OUT)
GPIO.setup (JALKAKELTAINEN, GPIO.OUT)
GPIO.setup (PAINIKE, GPIO.IN)
GPIO.setup (PIR, GPIO.IN)
GPIO.output(AUTOPUNAINEN, 0)
GPIO.output(AUTOKELTAINEN, 0)
GPIO.output(AUTOVIHREA, 0)
GPIO.output(JALKAPUNAINEN, 0)
GPIO.output(JALKAVIHREA, 0)
GPIO.output(JALKAKELTAINEN, 0)

def liikkeentunnistus(aika):
    vilkkuaika = time.time() + 10
    while time.time() < vilkkuaika:
        if GPIO.input(PIR) == 0:
            print "Ei liiku saa menna!!!"
            return
        GPIO.output(JALKAKELTAINEN, 1)
        time.sleep(0.1)
        GPIO.output(JALKAKELTAINEN, 0)
        time.sleep(0.1)
            
def vilkku(aika):
    vilkkuaika = time.time() + aika
    while time.time() < vilkkuaika:
        GPIO.output(JALKAKELTAINEN, 1)
        time.sleep(0.1)
        GPIO.output(JALKAKELTAINEN, 0)
        time.sleep(0.1)

def autovalot():
    aika = time.time() + 4
    GPIO.output(AUTOKELTAINEN, 0)
    GPIO.output(JALKAPUNAINEN, 1)
    GPIO.output(AUTOVIHREA, 1)
    while time.time() < aika:
        if GPIO.input(PAINIKE) == 1:
            liikkeentunnistus(4)
            jalkavalot()

def jalkavalot():
    GPIO.output(AUTOVIHREA, 0)
    GPIO.output(AUTOKELTAINEN, 1)
    vilkku(1)
    GPIO.output(JALKAPUNAINEN, 0)
    GPIO.output(AUTOKELTAINEN, 0)
    GPIO.output(AUTOPUNAINEN, 1)
    GPIO.output(JALKAVIHREA, 1)
    time.sleep(4.0)
    GPIO.output(AUTOPUNAINEN, 0)
    GPIO.output(AUTOKELTAINEN, 1)
    time.sleep(1.0)
    GPIO.output(JALKAVIHREA, 0)

painettu = 0
loppu = time.time() + 30

while time.time() < loppu:
    autovalot()

GPIO.cleanup()
