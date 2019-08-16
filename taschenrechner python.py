



print("Willkommen zu diesem kurzem Programm!")
print("Bitte bestätigen Sie kurz, indem Sie in die Konsole 'weiter' schreiben")



def ende():
    print("Bitte bestätigen Sie den Abbruch des Programms mit 'stop'. "
          "Um das Programm noch einmal durchzuführen, geben Sie 'weiter' ein.")
    z=input("Ihre Eingabe:   ")
    if z=="stop":
        print("Tschüss!")
        exit()
    if z=="weiter":
        program()
    if z !="stop" and z  !="weiter":
        ende()








def program():
        print("Bitte geben Sie jetzt alle Parameter ein!")
        zahl_1 = int(input("Zahl 1 eingeben: "))
        zahl_2 = int(input("Zahl 2 eingeben: "))
        summe= str(zahl_1+zahl_2)
        subtraktion =str(zahl_1-zahl_2)
        rechenoperator = input("Bitte geben sie die gewünschte Rechenoperation ein:   ")
        if rechenoperator=="plus" or rechenoperator=="addition" or rechenoperator=="+":
            print("Die Summe der beiden Zahlen ist " + summe + ".")
            ende()
        if rechenoperator== "minus" or rechenoperator=="subtraktion" or rechenoperator=="-":
            print("Das Ergebnis ist " + subtraktion + ".")
            ende()
        else:
            ende()


x = input("Ihre Eingabe:   ")
if x == "weiter":
        program()
else:
    print("Leider haben Sie eine unzulässige Angabe gemacht!")
    ende()









