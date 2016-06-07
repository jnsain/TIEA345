import RPi.GPIO as GPIO
import time

AUTOVIHREA=5
AUTOKELTAINEN=6
AUTOPUNAINEN=13
JALKAVIHREA=20
JALKAPUNAINEN=16
PAINIKE=27

GPIO.setmode (GPIO.BCM)
GPIO.setup (AUTOVIHREA, GPIO.OUT)
GPIO.setup (AUTOKELTAINEN, GPIO.OUT)
GPIO.setup (AUTOPUNAINEN, GPIO.OUT)
GPIO.setup (JALKAVIHREA, GPIO.OUT)
GPIO.setup (JALKAPUNAINEN, GPIO.OUT)
GPIO.setup (PAINIKE, GPIO.IN)
GPIO.output(AUTOPUNAINEN, 0)
GPIO.output(AUTOKELTAINEN, 0)
GPIO.output(AUTOVIHREA, 0)
GPIO.output(JALKAPUNAINEN, 0)
GPIO.output(JALKAVIHREA, 0)

def autovalot():
    aika = time.time() + 4
    GPIO.output(AUTOKELTAINEN, 0)
    GPIO.output(JALKAPUNAINEN, 1)
    GPIO.output(AUTOVIHREA, 1)
    while time.time() < aika:
        if GPIO.input(PAINIKE) == 1:
            time.sleep(2.0)
            jalkavalot()

def jalkavalot():
    GPIO.output(AUTOVIHREA, 0)
    GPIO.output(AUTOKELTAINEN, 1)
    time.sleep (1.0)
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
loppu = time.time() + 45

while time.time() < loppu:
    autovalot()


GPIO.cleanup ()
