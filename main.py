import tkinter as tk
from tkinter import messagebox


def checkf():
    m1 = userid_entry.get()
    m2 = userpwd_entry.get()
    if m1 == "LA1" and m2 == "123":
        submitf()
    else:
        userid_entry.delete(0 , "end")
        userpwd_entry.delete(0 , "end")
        messagebox.showwarning("warning", "Login Error!!! Wrong ID or Password")


def submitf():
    win2 = tk.Tk()
    win2.minsize(width=400, height=400)
    title_label = tk.Label(win2, text="Please select on the concentration term you wan't to calculate", width=100)
    title_label.pack()
    molarity_button = tk.Button(win2, text="Molarity", width=20, command=molarityf)
    molality_button = tk.Button(win2, text="Molality", width=20, command=molalityf)
    normality_button = tk.Button(win2, text="Normality", width=20, command=normalityf)
    molefraction_button = tk.Button(win2, text="Mole Fraction", width=20, command=mole_fractionf)
    weightbyweight_button = tk.Button(win2, text="Weight By weight", width=25, command=weightbyweightf)
    weigthbyvolume_button = tk.Button(win2, text="Weight By Volume", width=25, command=weightbyvolumef)
    volumebyvolume_button = tk.Button(win2, text="Volume by Volume", width=25, command=volumebyvolumef)
    molarity_button.place(x=10, y=35)
    molality_button.place(x=180, y=35)
    normality_button.place(x=360, y=35)
    molefraction_button.place(x=540, y=35)
    weightbyweight_button.place(x=50, y=70)
    weigthbyvolume_button.place(x=250, y=70)
    volumebyvolume_button.place(x=450, y=70)
    exit2_button = tk.Button(win2, text="Exit", width=15, command=win2.destroy)
    exit2_button.place(x=300, y=120)


def molarityf():
    win3 = tk.Tk()
    win3.minsize(width=400, height=400)
    molarity_label = tk.Label(win3, text="Molarity")
    molarity_label.pack()

    def calculatef():
        m1 = int(moles_entry.get())
        m2 = int(volume_entry.get())
        a = m1/m2
        answer_label.configure(text=a)

    moles_label = tk.Label(win3, text="Enter number of moles")
    moles_entry = tk.Entry(win3, width=25)
    volume_label = tk.Label(win3, text="Enter volume (in litres)")
    volume_entry = tk.Entry(win3, width=25)
    molarity_label = tk.Label(win3, text="Molarity")
    answer_label = tk.Label(win3)
    moles_label.place(x=10, y=45)
    moles_entry.place(x=200, y=45)
    volume_label.place(x=10, y=80)
    volume_entry.place(x=200, y=80)
    molarity_label.place(x=10, y=115)
    answer_label.place(x=200, y=115)
    calculate_button = tk.Button(win3, text="Calculate", command=calculatef)
    calculate_button.place(x=100, y=150)
    exit3_button = tk.Button(win3, text="Exit", command=win3.destroy)
    exit3_button.place(x=200, y=150)


def molalityf():
    win4 = tk.Tk()
    win4.minsize(height=400, width=400)
    molality_label = tk.Label(win4, text="Molality")
    molality_label.pack()

    def calculate():
        m1 = int(moles_entry.get())
        m2 = int(weight_entry.get())
        a = m1/m2
        answer_label.configure(text=a)

    moles_label = tk.Label(win4, text="Enter no. of moles")
    moles_entry = tk.Entry(win4, width=25)
    weight_label = tk.Label(win4, text="Enter weight(in kg)")
    weight_entry = tk.Entry(win4, width=25)
    molality_label = tk.Label(win4, text="Molality")
    answer_label = tk.Label(win4)
    moles_label.place(x=10, y=45)
    moles_entry.place(x=200, y=45)
    weight_label.place(x=10, y=80)
    weight_entry.place(x=200, y=80)
    molality_label.place(x=10, y=115)
    answer_label.place(x=200, y=115)
    calculate_button = tk.Button(win4, text="Calculate", command=calculate)
    exit_button = tk.Button(win4, text="Exit", command=win4.destroy)
    # calculate_button.pack()
    # exit_button.pack()
    calculate_button.place(x=100, y=150)
    exit_button.place(x=200, y=150)



def normalityf():
    win5 = tk.Tk()
    win5.minsize(height=400, width=400)
    normality_label = tk.Label(win5, text="Normality")
    normality_label.pack()

    def calculate():
        m1 = int(moles_entry.get())
        m2 = int(gequivalents_entry.get())
        a = m1/m2
        answer_label.configure(text=a)

    moles_label = tk.Label(win5, text="Enter no. of g equivalents")
    moles_entry = tk.Entry(win5, width=25)
    gequivalents_label = tk.Label(win5, text="Enter volume of solution (in litres)")
    gequivalents_entry = tk.Entry(win5, width=25)
    normality_label = tk.Label(win5, text="Normality")
    answer_label = tk.Label(win5)
    moles_label.place(x=10, y=45)
    moles_entry.place(x=200, y=45)
    gequivalents_label.place(x=10, y=80)
    gequivalents_entry.place(x=200, y=80)
    normality_label.place(x=10, y=115)
    answer_label.place(x=200, y=115)
    calculate_button = tk.Button(win5, text="Calculate", command=calculate)
    # calculate_button.pack()
    calculate_button.place(x=100, y=150)
    exit_button = tk.Button(win5, text="Exit", command=win5.destroy)
    # exit_button.pack()
    exit_button.place(x=200, y=150)


def mole_fractionf():
    win6 = tk.Tk()
    win6.minsize(height=400, width=400)
    molefraction_label = tk.Label(win6, text="Mole Fraction")
    molefraction_label.pack()

    def calculate():
        m1 = int(molesofa_entry.get())
        m2 = int(molesofb_entry.get())
        a = m1/(m1+m2)
        b = m2/(m1+m2)
        molefractionofa_label.configure(text=a)
        molefractionofb_label.configure(text=b)

    molesofa_label = tk.Label(win6, text="Moles of component A")
    molesofb_label = tk.Label(win6, text="Moles of component B")
    molesofa_entry = tk.Entry(win6, width=25)
    molesofb_entry = tk.Entry(win6, width=25)
    molesofa_label.place(x=10, y=45)
    molesofa_entry.place(x=200, y=45)
    molesofb_label.place(x=10, y=80)
    molesofb_entry.place(x=200, y=80)
    molefractionofa1_label = tk.Label(win6, text="Mole fraction of A is")
    molefractionofa1_label.place(x=10, y=115)
    molefractionofa_label = tk.Label(win6)
    molefractionofa_label.place(x=200, y=115)
    molefractionofb1_label = tk.Label(win6, text="Mole fraction of B is")
    molefractionofb1_label.place(x=10, y=150)
    molefractionofb_label = tk.Label(win6)
    molefractionofb_label.place(x=200, y=150)
    calculate_button = tk.Button(win6, text="Calculate", command=calculate)
    calculate_button.place(x=100, y=190)
    exit_button = tk.Button(win6, text="Exit", command=win6.destroy)
    exit_button.place(x=200, y=190)


def weightbyweightf():
    win7 = tk.Tk()
    win7.minsize(width=400, height=400)
    weightbyweight_label = tk.Label (win7, text="Weight By Weight")
    weightbyweight_label.pack()

    def calculate():
        m1 = int(weightofsolute_entry.get())
        m2 = int(weightofsolution_entry.get())
        a = (m1/m2)*100
        # b =  + "%"
        answer_label.configure(text=a)

    weightofsolute_label = tk.Label(win7, text="Weight of Solute")
    weightofsolute_entry = tk.Entry(win7, width=25)
    weightofsolution_Label = tk.Label(win7, text="Weight of Solution")
    weightofsolution_entry = tk.Entry(win7, width=25)
    answer_label = tk.Label(win7)
    percentage_label = tk.Label (win7, text="Percentage")
    weightofsolute_label.place(x=10, y=45)
    weightofsolute_entry.place(x=200, y=45)
    weightofsolution_Label.place(x=10, y=80)
    weightofsolution_entry.place(x=200, y=80)
    percentage_label.place(x=10, y=115)
    answer_label.place(x=200, y=115)
    # answer_label.pack()
    calculate_button = tk.Button(win7, text="Calculate", command=calculate)
    # calculate_button.pack()
    exit_button = tk.Button(win7, text="Exit" , command=win7.destroy)
    # exit_button.pack()
    calculate_button.place(x=100, y=150)
    exit_button.place(x=200, y=150)




def weightbyvolumef():
    win8 = tk.Tk()
    win8.minsize(height=400, width=400)
    weightbyvolume_label = tk.Label(win8, text="Weight By Volume")
    weightbyvolume_label.pack()

    def calculate():
        m1 = int(weightofsolute_entry.get())
        m2 = int(volumeofsolution_entry.get())
        a = (m1/m2)*100
        # b =  + "%"
        answer_label.configure(text=a)

    weightofsolute_label = tk.Label(win8, text="Weight of Solute")
    volumeofsolution_label = tk.Label(win8, text="Volume of Solution")
    weightofsolute_entry = tk.Entry(win8, width=25)
    volumeofsolution_entry = tk.Entry(win8, width=25)
    percentage_label = tk.Label(win8, text="Percentage")
    answer_label = tk.Label(win8)
    weightofsolute_label.place(x=10, y=45)
    weightofsolute_entry.place(x=200, y=45)
    volumeofsolution_label.place(x=10, y=80)
    volumeofsolution_entry.place(x=200, y=80)
    percentage_label.place(x=10, y=115)
    answer_label.place(x=200, y=115)
    calculate_button = tk.Button(win8, text="Calculate", command=calculate)
    # calculate_button.pack()
    exit_button = tk.Button(win8, text="Exit", command=win8.destroy)
    # exit_button.pack()
    calculate_button.place(x=100, y=150)
    exit_button.place(x=200, y=150)


def volumebyvolumef():
    win9 = tk.Tk()
    win9.minsize(height=400, width=400)
    volumebyvolume_label = tk.Label(win9, text="Volume by Volume")
    volumebyvolume_label.pack()

    def calculate():
        m1 = int(volumeofsolute_entry.get())
        m2 = int(volumeofsolution_entry.get())
        a = (m1/m2)*100
        # b =  + "%"
        answer_label.configure(text=a)

    volumeofsolute_label = tk.Label(win9, text="Volume of Solute")
    volumeofsolution_label = tk.Label(win9, text="Volume of solution")
    volumeofsolute_entry = tk.Entry(win9, width=25)
    volumeofsolution_entry = tk.Entry(win9, width=25)
    percentage_label = tk.Label(win9, text="Percentage")
    answer_label = tk.Label(win9)
    volumeofsolute_label.place(x=10, y=45)
    volumeofsolute_entry.place(x=200, y=45)
    volumeofsolution_label.place(x=10, y=80)
    volumeofsolution_entry.place(x=200, y=80)
    percentage_label.place(x=10, y=115)
    answer_label.place(x=200, y=115)
    calculate_button = tk.Button(win9, text="Calculate", command=calculate)
    # calculate_button.pack()
    exit_button = tk.Button(win9, text="Exit", command=win9.destroy)
    # exit_button.pack()
    calculate_button.place(x=100, y=150)
    exit_button.place(x=200, y=150)


root = tk.Tk()
root.minsize(width=400, height=400)
title_label = tk.Label(root, text="Concentration terms Calculator", width=25)
userid_label = tk.Label(root, text="Enter User Id")
userid_entry = tk.Entry(root, width=25)
userpwd_label = tk.Label(root, text="Enter Your Password")
userpwd_entry = tk.Entry(root, width=25)
submit1_button = tk.Button(root, text="Continue", width=10, command=checkf)
exit1_button = tk.Button(root, text="Exit", width=10, command=root.destroy)
title_label.place(x=110, y=0)
userid_label.place(x=30, y=35)
userid_entry.place(x=200, y=35)
userpwd_label.place(x=30, y=70)
userpwd_entry.place(x=200, y=70)
submit1_button.place(x=100, y=105)
exit1_button.place(x=200, y=105)
root.mainloop()