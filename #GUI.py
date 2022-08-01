import datetime
import tkinter
from tkinter import*
from tkinter import messagebox
import random
import time
import sqlite3


def OK():
    uname=txtusername.get()
    password=txtpassword.get()
    if(uname ==""and password==""):
        messagebox.showinfo("","blank Not allowed")

    elif(uname=="Admin" and password=="1234"):
        messagebox.showinfo("","Login Success ")
        root.destroy()

    else:
        messagebox.showinfo("","Incorrect Username and Password")

def reset():
    username.set("")
    password.set("")



#======= Login page

root = Tk()
root.geometry("400x300+0+0")
root.title("Login User")

#=====lable
LF=Frame(root, width=750, height=600,bd=16, relief="raise")
LF.pack()

lblUserName = Label(root,font=('Times New Roman',12, 'bold'),text="User Name",
                        fg="black", bd=10, anchor='w')
lblUserName.place(x=20,y=10)

lblpassword = Label(root,font=('Times New Roman',12, 'bold'),text="Password",
                        fg="black", bd=10, anchor='w')
lblpassword.place(x=20,y=48)


#========txt box
username= StringVar()
txtusername = Entry(root,font=('Times New Roman', 12,'bold'), bd=10, width=20,
                        bg="white",textvariable =username)
txtusername.place(x=140,y=25)

password= StringVar()
txtpassword = Entry(root,font=('Times New Roman', 12,'bold'), bd=10, width=20,
                        bg="white",textvariable =password)
txtpassword.place(x=140,y=55)

txtpassword.config(show="*")


#=======button

btnlogin=Button(root,padx=8, bd=8,fg="Black",font=('arial', 10,'bold'),width=8,
                      text="Login",bg="white", command=OK).place(x=20, y=150)

btnexit=Button(root,padx=8, bd=8,fg="Black",font=('arial', 10,'bold'),width=8,
                      text="Exit",bg="white", command=exit).place(x=250, y=150)

btnResetSystem=Button(root,padx=8, bd=8,fg="Black",font=('arial', 10,'bold'),width=8,
                      text="Reset",bg="white", command=reset).place(x=130, y=150)

root.mainloop()


def clear():
    EmployeeName.set("")
    Address.set("")
    Reference.set("")
    EmployerName.set("")
    Age.set("")
    PhoneNo.set("")
    Gender.set("")

connection = sqlite3.connect("Employeepayroll.db")
connection.commit()

with connection:
    connection.execute("CREATE TABLE IF NOT EXISTS Employeepayroll( id INTEGER PRIMARY KEY ,EmployeeName text, Address text,Reference text,EmployerName text,Age text,PhoneNo text,Gender text)")
    connection.commit()

def savedata():
    connection=sqlite3.connect('Employeepayroll.db')
    C=connection.cursor()
    C.execute('INSERT INTO Employeepayroll (EmployeeName, Address,Reference,EmployerName,Age,PhoneNo ,Gender)VALUES (?,?,?,?,?,?,?)',(EmployeeName.get(), Address.get(),Reference.get(),EmployerName.get(),Age.get(),PhoneNo.get(),Gender.get()))
    connection.commit()

    employeenam = EmployeeName.get()
    addres=Address.get()
    reference=Reference.get()
    employername=EmployerName.get()
    age=Age.get()
    phoneno=PhoneNo.get()
    gender=Gender.get()
    if (employeenam=="" and addres=="" and reference=="" and employername=="" and age==""and phoneno==""and gender==""):
     messagebox.showinfo("", "blank Not allowed")
    else:
      messagebox.showinfo("", "added Success ")
      clear()


payroll = Tk()
payroll.geometry("1350x600+0+0")
payroll.title("Payroll Management System")

def exit():
    payroll.destroy()

def Reset():
    EmployeeName.set("")
    Address.set("")
    Reference.set("")
    EmployerName.set("")
    CityWeighting.set("")
    BasicSalary.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPay.set("")
    Tax.set("")
    Pension.set("")
    StudentLoan.set("")
    NIPayment.set("")
    Deductions.set("")
    PhoneNo.set("")
    Gender.set("")
    PayDate.set("")
    TaxPeriod.set("")
    NINumber.set("")
    NICode.set("")
    TaxablePay.set("")
    PensionablePay.set("")
    OtherPaymentDue.set("")


def PayRef():
    PayDate.set(time.strftime("%x"))
    RefPay = random.randint(20000, 709467)
    RefPaid = str("PR" + str(RefPay))
    Reference.set(RefPaid)

    NIPay = random.randint(4200, 9467)
    NIPaid = str("NI" + str(RefPay))
    NINumber.set(NIPaid)


def PayPeriod():
    i = datetime.datetime.now()
    TaxPeriod.set(i.month)

    NCode = random.randint(1200, 1467)
    CodeNI = str("NICode" + str(NCode))
    NICode.set(CodeNI)


def MonthlySalary():
    BS = float(BasicSalary.get())
    CW = float(CityWeighting.get())
    OT = float(OverTime.get())

    MTax = ((BS + CW + OT) * 0.3)
    TTax = "Rs.", str('%.2f' % (MTax))

    Tax.set(TTax)

    MPension = ((BS + CW + OT) * 0.02)
    MMPension = "Rs.", str('%.2f' % (MPension))

    Pension.set(MMPension)

    MStudentLoan = ((BS + CW + OT) * 0.012)
    MMStudentLoan = "Rs.", str('%.2f' % (MStudentLoan))

    StudentLoan.set(MMStudentLoan)

    MNIPayment = ((BS + CW + OT) * 0.011)
    MMNIPayment = "Rs.", str('%.2f' % (MNIPayment))

    NIPayment.set(MMNIPayment)

    Deduct = MTax + MPension + MStudentLoan + MNIPayment
    Deduct_Payment = "Rs.", str('%.2f' % (Deduct))
    Deductions.set(Deduct_Payment)
    Gross_pay = "Rs.", str('%.2f' % (BS + CW + OT))
    GrossPay.set(Gross_pay)

    NetPayAfter = ((BS + CW + OT) - Deduct)
    NetAfter = "Rs.", str('%.2f' % (NetPayAfter))

    TaxablePay.set(TTax)
    PensionablePay.set(MMPension)
    OtherPaymentDue.set("0.00")

    NetPay.set(NetAfter)


EmployeeName =StringVar()
Address =StringVar()
Reference =StringVar()
EmployerName =StringVar()
CityWeighting =StringVar()
BasicSalary =StringVar()
OverTime =StringVar()
GrossPay =StringVar()
NetPay =StringVar()
Tax =StringVar()
Pension =StringVar()
StudentLoan=StringVar()
NIPayment =StringVar()
Deductions=StringVar()
PhoneNo=StringVar()
Gender=StringVar()
PayDate=StringVar()
TaxPeriod=StringVar()
NINumber=StringVar()
NICode=StringVar()
TaxablePay=StringVar()
PensionablePay=StringVar()
OtherPaymentDue=StringVar()
Age = StringVar()

Tops=Frame(payroll, width=1350, height=50,bd=16, relief="raise")
Tops.pack(side=TOP)
LF=Frame(payroll, width=700, height=650,bd=16, relief="raise")
LF.pack(side=LEFT)
RF=Frame(payroll, width=600, height=650,bd=16, relief="raise")
RF.pack(side=RIGHT)

lblInfo = Label(Tops, font=('Berlin Sans FB Demi',45, 'bold'),text="Employee's Payroll System",fg="dark blue", bd=1)
lblInfo.grid(row=0,column=0)

LeftInsideLF=Frame(LF, width=700, height=100,bd=8, relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF, width=325, height=400,bd=8, relief="raise")
LeftInsideLFLF.pack(side=LEFT)
LeftInsideRFRF=Frame(LF, width=325, height=400,bd=8, relief="raise")
LeftInsideRFRF.pack(side=RIGHT)

RightInsideLF=Frame(RF, width=600, height=200,bd=8, relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF, width=300, height=400,bd=8, relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF, width=300, height=400,bd=8, relief="raise")
RightInsideRFRF.pack(side=RIGHT)

#========
lblEmployeeName = Label(LeftInsideLF, font=('Times New Roman',12, 'bold'),text="Employee Name",
                        fg="black", bd=10, anchor='w')
lblEmployeeName.grid(row=0,column=0)
txtEmployeeName = Entry(LeftInsideLF,font=('arial', 12,'bold'), bd=20, width=54,
                        bg="powder blue", justify = 'left',textvariable=EmployeeName)
txtEmployeeName.grid(row=0,column=1)
lblAddress = Label(LeftInsideLF, font=('Times New Roman',12, 'bold'),text="Address ",
                        fg="black", bd=10, anchor='w')
lblAddress.grid(row=1,column=0)
txtAddress = Entry(LeftInsideLF,font=('arial', 12,'bold'), bd=20, width=54,
                        bg="powder blue", justify = 'left',textvariable=Address)
txtAddress.grid(row=1,column=1)

lblReference = Label(LeftInsideLF, font=('Times New Roman',12, 'bold'),text="Reference",
                        fg="black", bd=10, anchor='w')
lblReference.grid(row=2,column=0)
txtReference = Entry(LeftInsideLF,font=('arial', 12,'bold'), bd=20, width=54,
                        bg="powder blue", justify = 'left',textvariable=Reference)
txtReference.grid(row=2,column=1)

lblEmployerName = Label(LeftInsideLF, font=('Times New Roman',12, 'bold'),text="Employer Name ",
                        fg="black", bd=10, anchor='w')
lblEmployerName.grid(row=3,column=0)
txtEmployerName = Entry(LeftInsideLF,font=('arial', 12,'bold'), bd=20, width=54,
                        bg="powder blue", justify = 'left',textvariable=EmployerName)
txtEmployerName.grid(row=3,column=1)

lblAge = Label(LeftInsideLF, font=('Times New Roman',12, 'bold'),text="Age ",
                        fg="black", bd=10, anchor='w')
lblAge.grid(row=4,column=0)
txtAge = Entry(LeftInsideLF,font=('arial', 12,'bold'), bd=20, width=54,
                        bg="powder blue", justify = 'left',textvariable=Age)
txtAge.grid(row=4,column=1)

#================

lblCity = Label(LeftInsideLFLF, font=('Times New Roman',12, 'bold'),text="City Weighting",
                        fg="black", bd=10, anchor='w')
lblCity.grid(row=0,column=0)
txtCity = Entry(LeftInsideLFLF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=CityWeighting)
txtCity.grid(row=0,column=1)
#------------------------
lblBasicSalary = Label(LeftInsideLFLF, font=('Times New Roman',12, 'bold'),text="Basic Salary",
                        fg="black", bd=10, anchor='w')
lblBasicSalary.grid(row=1,column=0)
txtBasicSalary = Entry(LeftInsideLFLF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=BasicSalary)
txtBasicSalary.grid(row=1,column=1)

#-------------------
lblOverTime = Label(LeftInsideLFLF, font=('Times New Roman',12, 'bold'),text="Over Time",
                        fg="black", bd=10, anchor='w')
lblOverTime.grid(row=2,column=0)
txtOverTime = Entry(LeftInsideLFLF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=OverTime)
txtOverTime.grid(row=2,column=1)

#-------------------
lblGrossPay = Label(LeftInsideLFLF, font=('Times New Roman',12, 'bold'),text="Gross Pay",
                        fg="black", bd=10, anchor='w')
lblGrossPay.grid(row=3,column=0)
txtGrossPay = Entry(LeftInsideLFLF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=GrossPay)
txtGrossPay.grid(row=3,column=1)

lblNetPay = Label(LeftInsideLFLF, font=('Times New Roman',12, 'bold'),text="Net Pay",
                        fg="black", bd=10, anchor='w')
lblNetPay.grid(row=4,column=0)
txtNetPay = Entry(LeftInsideLFLF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=NetPay)
txtNetPay.grid(row=4,column=1)


#======================================================================================
#=============

lblTax = Label(LeftInsideRFRF, font=('Times New Roman',12, 'bold'),text="Tax",
                        fg="black", bd=10, anchor='w')
lblTax.grid(row=0,column=0)
txtTax = Entry(LeftInsideRFRF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=Tax)
txtTax.grid(row=0,column=1)
#-----------------------

lblPension = Label(LeftInsideRFRF, font=('Times New Roman',12, 'bold'),text="Pension",
                        fg="black", bd=10, anchor='w')
lblPension.grid(row=1,column=0)
txtPension = Entry(LeftInsideRFRF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=Pension)
txtPension.grid(row=1,column=1)
#-----------------------

lblStudentLoan = Label(LeftInsideRFRF, font=('Times New Roman',12, 'bold'),text="Student Loan",
                        fg="black", bd=10, anchor='w')
lblStudentLoan.grid(row=2,column=0)
txtStudentLoan = Entry(LeftInsideRFRF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=StudentLoan)
txtStudentLoan.grid(row=2,column=1)

#---------------------
lblNIPayment = Label(LeftInsideRFRF, font=('Times New Roman',12, 'bold'),text="NI Payment",
                        fg="black", bd=10, anchor='w')
lblNIPayment.grid(row=3,column=0)
txtNIPayment = Entry(LeftInsideRFRF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=NIPayment)
txtNIPayment.grid(row=3,column=1)
#=======================================Right Side======================================

lblPhoneNo = Label(RightInsideLF, font=('Times New Roman',12, 'bold'),text="Phone No",
                        fg="black", bd=10, anchor='w')
lblPhoneNo.grid(row=0,column=0)
txtPhoneNo = Entry(RightInsideLF,font=('arial', 12,'bold'), bd=20, width=48,
                        bg="powder blue", justify = 'left',textvariable=PhoneNo)
txtPhoneNo.grid(row=0,column=1)

lblGender = Label(RightInsideLF, font=('Times New Roman',12, 'bold'),text="Gender",
                        fg="black", bd=10, anchor='w')
lblGender.grid(row=1,column=0)
txtGender = Entry(RightInsideLF,font=('arial', 12,'bold'), bd=20, width=48,
                        bg="powder blue", justify = 'left',textvariable=Gender)
txtGender.grid(row=1,column=1)

#============================================================
lblPayDate = Label(RightInsideLFLF, font=('Times New Roman',12, 'bold'),text="Pay Date",
                        fg="black", bd=10, anchor='w')
lblPayDate.grid(row=0,column=0)
txtPayDate = Entry(RightInsideLFLF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=PayDate)
txtPayDate.grid(row=0,column=1)

lblTaxPeriod = Label(RightInsideLFLF, font=('Times New Roman',12, 'bold'),text="Tax Period",
                        fg="black", bd=10, anchor='w')
lblTaxPeriod.grid(row=1,column=0)
txtTaxPeriod = Entry(RightInsideLFLF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=TaxPeriod)
txtTaxPeriod.grid(row=1,column=1)

lblNINumber = Label(RightInsideLFLF, font=('Times New Roman',12, 'bold'),text="NI Number",
                        fg="black", bd=10, anchor='w')
lblNINumber.grid(row=2,column=0)
txtNINumber = Entry(RightInsideLFLF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=NINumber)
txtNINumber.grid(row=2,column=1)

lblNICode = Label(RightInsideLFLF, font=('Times New Roman',12, 'bold'),text="NI Code",
                        fg="black", bd=10, anchor='w')
lblNICode.grid(row=3,column=0)
txtNICode = Entry(RightInsideLFLF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=NICode)
txtNICode.grid(row=3,column=1)

lblTaxablePay = Label(RightInsideLFLF, font=('Times New Roman',12, 'bold'),text="Taxable Pay",
                        fg="black", bd=10, anchor='w')
lblTaxablePay.grid(row=4,column=0)
txtTaxablePay = Entry(RightInsideLFLF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=TaxablePay)
txtTaxablePay.grid(row=4,column=1)

lblPensionablePay = Label(RightInsideLFLF, font=('Times New Roman',12, 'bold'),text="Pensionable Pay",
                        fg="black", bd=10, anchor='w')
lblPensionablePay.grid(row=5,column=0)
txtPensionablePay = Entry(RightInsideLFLF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=PensionablePay)
txtPensionablePay.grid(row=5,column=1)

lblOtherPaymentDue = Label(RightInsideLFLF, font=('Times New Roman',12, 'bold'),text="Other Payment Due",
                        fg="black", bd=10, anchor='w')
lblOtherPaymentDue.grid(row=6,column=0)
txtOtherPaymentDue = Entry(RightInsideLFLF,font=('arial', 12,'bold'), bd=10, width=18,
                        bg="powder blue", justify = 'left',textvariable=OtherPaymentDue)
txtOtherPaymentDue.grid(row=6,column=1)

#==================== Butten ________________________

btnWagePayment=Button(RightInsideRFRF,padx=8, bd=8,fg="Black",font=('arial', 12,'bold'),width=18,
                      command=MonthlySalary,text="Wage Payment",bg="white").grid(row=0,column=0)

btnResetSystem=Button(RightInsideRFRF,padx=8, bd=8,fg="Black",font=('arial', 12,'bold'),width=18,
                      text="Reset System ",bg="white", command=Reset).grid(row=1,column=0)

btnPayRef=Button(RightInsideRFRF,padx=8, bd=8,fg="Black",font=('arial', 12,'bold'),width=18,
                      text="Pay Reference",bg="white", command=PayRef).grid(row=2,column=0)

btnPayCode=Button(RightInsideRFRF,padx=8, bd=8,fg="Black",font=('arial', 12,'bold'),width=18,
                      text="Pay Code",bg="white", command=PayPeriod).grid(row=3,column=0)

btnAdd=Button(RightInsideRFRF,padx=8, bd=8,fg="Black",font=('arial', 12,'bold'),width=18,
                   text="Add ",bg="white",command=savedata ).grid(row=4,column=0)

btnExit=Button(RightInsideRFRF,padx=8, bd=8,fg="Black",font=('arial', 12,'bold'),width=18,
                      text="Exit",bg="white", command=exit).grid(row=5,column=0)

payroll.mainloop()