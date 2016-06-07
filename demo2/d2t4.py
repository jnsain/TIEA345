import RPi.GPIO as GPIO
import time

LED=19
PAINIKE=4
PIR=24

GPIO.setmode (GPIO.BCM)
GPIO.setup (LED, GPIO.OUT)
GPIO.setup (PAINIKE, GPIO.IN)
GPIO.setup (PIR, GPIO.IN)
status=False
liike=0
loppu = time.time() + 30

while time.time() < loppu:
        if GPIO.input(PIR) is not liike:
                if GPIO.input(PIR) == 1:
                        print "liike alkoi"
                else:
                        print "liike loppui"
        liike = GPIO.input(PIR)                

        if GPIO.input(PAINIKE):
                GPIO.output(LED, not status)
                status = not status
                time.sleep (0.1) # ilman tata prossukaytto 100%

GPIO.cleanup ()
