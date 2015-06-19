#! /usr/bin/env python

# demo.py --- A simple demonstration program for pythondialog
# Copyright (C) 2000  Robb Shecter, Sultanbek Tezadov
# Copyright (C) 2002, 2004  Florent Rougon
#
# This program is in the public domain.

"""Demonstration program for pythondialog.
This is a simple program demonstrating the possibilities offered by
the pythondialog module (which is itself a Python interface to the
well-known dialog utility, or any other program compatible with
dialog).
Please have a look at the documentation for the `handle_exit_code'
function in order to understand the somewhat relaxed error checking
policy for pythondialog calls in this demo.
"""

import sys, os, os.path, time, string, dialog

FAST_DEMO = 0


# XXX We should handle the new DIALOG_HELP and DIALOG_EXTRA return codes here.
def handle_exit_code(d, code):
    """Sample function showing how to interpret the dialog exit codes.
    This function is not used after every call to dialog in this demo
    for two reasons:
       1. For some boxes, unfortunately, dialog returns the code for
          ERROR when the user presses ESC (instead of the one chosen
          for ESC). As these boxes only have an OK button, and an
          exception is raised and correctly handled here in case of
          real dialog errors, there is no point in testing the dialog
          exit status (it can't be CANCEL as there is no CANCEL
          button; it can't be ESC as unfortunately, the dialog makes
          it appear as an error; it can't be ERROR as this is handled
          in dialog.py to raise an exception; therefore, it *is* OK).
       2. To not clutter simple code with things that are
          demonstrated elsewhere.
    """
    # d is supposed to be a Dialog instance
    if code in (d.DIALOG_CANCEL, d.DIALOG_ESC):
        if code == d.DIALOG_CANCEL:
            msg = "You chose cancel in the last dialog box. Do you want to " \
                  "exit this demo?"
        else:
            msg = "You pressed ESC in the last dialog box. Do you want to " \
                  "exit this demo?"
        # "No" or "ESC" will bring the user back to the demo.
        # DIALOG_ERROR is propagated as an exception and caught in main().
        # So we only need to handle OK here.
        if d.yesno(msg) == d.DIALOG_OK:
            sys.exit(0)
        return 0
    else:
        return 1                        # code is d.DIALOG_OK
        

def infobox_demo(d):
    # Exit code thrown away to keey this demo code simple (however, real
    # errors are propagated by an exception)
    d.infobox("One moment, please. Just wasting some time here to "
              "show you the infobox...")
    
    if FAST_DEMO:
        time.sleep(0.5)
    else:
        time.sleep(3)

def gauge_demo(d):
    d.gauge_start("Progress: 0%", title="Still testing your patience...")
    for i in range(1, 101):
        if i < 50:
            d.gauge_update(i, "Progress: %d%%" % i, update_text=1)
        elif i == 50:
            d.gauge_update(i, "Over %d%%. Good." % i, update_text=1)
        elif i == 80:
            d.gauge_update(i, "Yeah, this boring crap will be over Really "
                           "Soon Now.", update_text=1)
        else:
            d.gauge_update(i)

        if FAST_DEMO:
            time.sleep(0.01)
        else:
            time.sleep(0.1)
    d.gauge_stop()
    

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
    # If the user presses Cancel, he is asked (by handle_exit_code) if he
    # wants to exit the demo. We loop as long as he tells us he doesn't want
    # to do so.
    while 1:
        (code, answer) = d.inputbox("What's your name?")
        if handle_exit_code(d, code):
            break
    return answer


def demo():
#   If you want to use Xdialog (pathnames are also OK for the 'dialog'
#   argument)
#   d = dialog.Dialog(dialog="Xdialog", compat="Xdialog")
    d = dialog.Dialog(dialog="dialog")

    #d.add_persistent_args(["--backtitle", "pythondialog demo"])

#    infobox_demo(d)
#    gauge_demo(d)
#    answer = yesno_demo(d)
#    msgbox_demo(d, answer)
#    textbox_demo(d)
    n1 = inputbox_demo(d)
    n2 = inputbox_demo(d)
    print int(n1) + int(n2)

def main():
    """This demo shows the main features of the pythondialog Dialog class.
    """
    try:
        demo()
    except dialog.error, exc_instance:
        sys.stderr.write("Error:\n\n%s\n" % exc_instance.complete_message())
        sys.exit(1)
        
    sys.exit(0)


if __name__ == "__main__": main()

