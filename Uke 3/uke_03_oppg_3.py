enhet = input ("Angi enhet: ")
verdi = input ("Angi verdi: ")
if enhet == ("nm"):
    if float(verdi) >= pow(float(10), 9):
        print ("Dette er radiobølger.")
    if float(verdi) >= pow(float(10), 6) and float(verdi) < pow(float(10), 9):
        print ("Dette er mikrobølger.")
    if float(verdi) >= pow(float(740), 1) and float(verdi) < pow(float(10), 6):
        print ("Dette er infrarød stråling.")
    if float(verdi) >= pow(float(380), 1) and float(verdi) < pow(float(740), 1):
        print ("Dette er synlig lys.")
    if float(verdi) >= pow(float(10), 1) and float(verdi) < pow(float(380), 1):
        print ("Dette er ultrafiolett stråling.")
    if float(verdi) >= pow(float(10), -2) and float(verdi) < pow(float(10), 1):
        print ("Dette er røntgenstråling.")
    if float(verdi) < pow(float(10), -2):
        print ("Dette er gammastråling.")

if enhet == ("THz"):
    if float(verdi) >= 3*pow(float(10), 7):
        print ("Dette er gammastråling.")
    if float(verdi) >= 3*pow(float(10), 4) and float(verdi) < 3*pow(float(10), 7):
        print ("Dette er røntgenstråling.")
    if float(verdi) >= pow(float(790), 1) and float(verdi) < 3*pow(float(10), 4):
        print ("Dette er ultrafiolett stråling.")
    if float(verdi) >= pow(float(405), 1) and float(verdi) < pow(float(790), 1):
        print ("Dette er synlig lys.")
    if float(verdi) >= pow(float(3), -1) and float(verdi) < pow(float(405), 1):
        print ("Dette er infrarød stråling.")
    if float(verdi) >= 3*pow(float(10), -4) and float(verdi) < pow(float(3), -1):
        print ("Dette er mikrobølger.")
    if float(verdi) < pow(float(10), -4):
        print ("Dette radiobølger.")

    # Mangler at tallene oppgis i e!