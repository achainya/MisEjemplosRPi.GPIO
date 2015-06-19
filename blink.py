import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

def blink():
		print "Ejecucion iniciada..."
		iteracion = 0
		while iteracion < 30: ## Segundos que durara la funcion
				GPIO.output(17, True) ## Enciendo el 17
				GPIO.output(18, True) ## Enciendo el 18
				time.sleep(1) ## Esperamos 1 segundo
				GPIO.output(17, False) ## Apago el 17
				GPIO.output(18, False) ## Apago el 18
				time.sleep(1) ## Esperamos 1 segundo
				iteracion = iteracion + 2 ## Sumo 2 porque he hecho dos parpadeos
		print "Ejecucion finalizada"
		GPIO.cleanup() ## Hacer una limpieza de los GPIO

blink() ## Hago la llamada a la funcion blink


