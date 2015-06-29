import sys, os, os.path, time, string, dialog
import RPi.GPIO as GPIO

PIN1 = 36
PIN2 = 11
PIN3 = 12
PIN4 = 35
PIN5 = 38
PIN6 = 40
PIN7 = 15
PIN8 = 16

FAST_DELAY = 0
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)
GPIO.setup(PIN5, GPIO.OUT)
GPIO.setup(PIN6, GPIO.OUT)
GPIO.setup(PIN7, GPIO.OUT)
GPIO.setup(PIN8, GPIO.OUT)

def handle_exit_code(d, code):
    if code in (d.DIALOG_CANCEL, d.DIALOG_ESC):
        if code == d.DIALOG_CANCEL:
            msg = "Quieres salir de esta aplicacion?"
        else:
            msg = "Quieres salir de esta aplicacion?"
        if d.yesno(msg) == d.DIALOG_OK:
            sys.exit(0)
        return 0
    else:
        return 1                        # code is d.DIALOG_OK

def yesno_demo(d):
    # Return the answer given to the question (also specifies if ESC was
    # pressed)
    return d.yesno("Do you like this demo?")
    

def msgbox_demo(d, answer):
    if answer == d.DIALOG_OK:
        d.msgbox("Excellent! Press OK to see the source code.")
    else:
        d.msgbox("Well, feel free to send your complaints to /dev/null!")


def textbox_demo(d):
    d.textbox("demo.py", width=76)

def inputbox_demo(d):
    while 1:
        (code, answer) = d.inputbox("Ingrese numero de iteraciones:")
        if handle_exit_code(d, code):
            break
    return answer

def gauge_demo(d):
    d.gauge_start("Progreso: 0%", title="Por favor espere...")
    for i in range(1, 101):
#        if i < 50:
        d.gauge_update(i, "Progreso: %d%%" % i, update_text=1)
#        elif i == 50:
#            d.gauge_update(i, "Over %d%%. Good." % i, update_text=1)
#        elif i == 80:
#            d.gauge_update(i, "Yeah, this boring crap will be over Really "
#                           "Soon Now.", update_text=1)
#        else:
#            d.gauge_update(i)

        if FAST_DELAY:
            time.sleep(0.01)
        else:
            time.sleep(0.1)
    d.gauge_stop()

def blink(d, ni):
    d.gauge_start("Progreso: 0%", title="Por favor espere...")
    iteracion = 0
    while iteracion < int(ni): ## Segundos que durara la funcion
        GPIO.output(PIN1, True)
        GPIO.output(PIN2, False)
        GPIO.output(PIN3, True)
        GPIO.output(PIN4, False) 
        GPIO.output(PIN5, True)
        GPIO.output(PIN6, False) 
        GPIO.output(PIN7, True) 
        GPIO.output(PIN8, False)
        if FAST_DELAY:
            time.sleep(0.2) ## Esperamos 1 segundo
        else:
            time.sleep(0.5)
        GPIO.output(PIN1, False) 
        GPIO.output(PIN2, True)
        GPIO.output(PIN3, False) 
        GPIO.output(PIN4, True)
        GPIO.output(PIN5, False) 
        GPIO.output(PIN6, True)
        GPIO.output(PIN7, False) 
        GPIO.output(PIN8, True)
        if FAST_DELAY:
            time.sleep(0.2) ## Esperamos 1 segundo
        else:
            time.sleep(0.5)
        iteracion = iteracion + 1 ## Sumo 1 porque he hecho dos parpadeos
        it = float(100/float(ni))
        d.gauge_update(round(it,2)*iteracion, "Progreso: %d%%" % (round(it,2)*iteracion), update_text=1)

    GPIO.cleanup() ## Hacer una limpieza de los GPIO
    d.gauge_stop()

def demo():
    d = dialog.Dialog(dialog="dialog")
    #gauge_demo(d)
    niteraciones = inputbox_demo(d)
    blink(d, niteraciones)

def main():
    try:
        demo()
    except dialog.error, exc_instance:
        sys.stderr.write("Error:\n\n%s\n" % exc_instance.complete_message())
        sys.exit(1)
        
    sys.exit(0)

if __name__ == "__main__": main()

