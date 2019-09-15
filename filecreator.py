from tkinter import*
import time




def main_funtion():
    screen1 = Tk()
    screen1.geometry("1920x1080")
    screen1.title("Willkommen")
    first_button = Button(text=" Neue Datei erstellen", bg="grey", command= asking)
    first_button.pack(side=TOP)
    screen1.mainloop()



def asking():
    global screen2
    screen2= Tk()
    screen2.geometry("500x500")
    screen2.title("Name der Datei eingeben!")
    global filename_entry
    filename_entry = Entry(screen2)


    Submit_button=Button(screen2, text="Datei erstellen", bg="grey", command =x)
    filename_entry.grid(row=2, column=5)
    Submit_button.grid(row=4, column=5)
    button1 =Button(screen2, text ="Zusätze fürs Dokument hinzufügen:", bg ="grey")
    button1.grid( row= 8, column =5)
    global addition_entry
    addition_entry = Entry(screen2 )
    addition_entry.grid(row=10, column=5)
    screen2.mainloop()






def x():
    screen2.destroy()
    addition = addition_entry.get()
    file_name = filename_entry.get()

    z= time.strftime("%d.%m.%Y %H:%M:%S")
    f=open(file_name + ".txt", 'w')
    f.write('********Current date and time: '+ z+ '*******')
    f.write(addition)
    f.close()
    print(f.closed)
    global screen3
    screen3 = Tk()
    screen3.geometry("500x500")

    message = Label(screen3, text = "Datei wurde erfolgreich erstellt!")
    message.pack(side=TOP)
    ok_button = Button(text = "ok", command = quit)
    ok_button.grid(row=3, column =8)
    screen3.mainloop()


def quit():
    screen3.destroy()


main_funtion()
