#Author : Nima Sherpa
#File: Final project.py
#date: November 14, 2020

from tkinter import *
from tkinter import ttk
from datetime import date 
import tkinter.messagebox as box
import math


#initaalizing the main window as window
window = Tk()
window.title("POINT OF SALE")  #title of the window
window.resizable(FALSE,FALSE)  #making the window unresizable

#menu
menu = ["Americano", "Latte", "Mocha", "Hot Choclate"] #menu option as a list
size = ["Large","Small"]   #size option as a list
itemVariable = StringVar()  #setting itemvariable as stringvar() which is choosed by the user.
itemVariable.set(menu[1])
sizeVariable = StringVar() #storing user's choosed size as sizevariable
sizeVariable.set(size[1]) 
quantityvar = StringVar()  #storing quantity entered as a quantity var
quantityvar.set("0")
i = 0
sum = 0
#Tree view
billTv = ttk.Treeview(window,height = 15, column = ('items','size','quantity','Total cost')) # initializeing treeview
today = date.today() #funciton for date

#function for exit button which pops up the message box.
def ex():
    box.showinfo("Thankyou for coming!!", "Next Customer Please")

#function which returns the price of the item when it is small size
def price():
    global itemVariable
    global cost 
    if(itemVariable.get() == 'Americano'):
        return 3.50
    if(itemVariable.get() == 'Latte'):
        return 4.50
    if(itemVariable.get() == 'Mocha'):
        return 5.00
    if(itemVariable.get() == 'Hot Choclate'):
        return 5.00
    else:
        return 0.00;
    
#it calculates the total amount of price of the item 
def total():
    global itemVariable
    global billTv
    global quantityvar
    global item
    global costVar
    global sizeVariable
    total = 0
    if (sizeVariable.get() == "Large"):
        sumlarge = (2.00 +  price())
        total = float(quantityvar.get()) * sumlarge
        return total
        
    if (sizeVariable.get() == "Small"):
        total = (float(quantityvar.get()) *  price())
        return total
    return 0.00
 
#function used to add item on treeview and also calulates the total bill as sum   
def addItem():
    global itemVariable
    global billTv
    global quantityvar
    global costVar
    global sizeVariable
    global i
    global sum
    billTv.insert(parent = '',index= 'end',iid= i,text = str(i + 1) + "      ",values = ("             " + itemVariable.get(),"                   " + sizeVariable.get()+ "                     ","                       " + quantityvar.get(),total()))
    sum  += total()
    i = i + 1    
    
# function to create new window for bill
def bill():
    global sum
    global itemVariable
    global billTv
    global quantityvar
    global costVar
    global sizeVariable
    global i
    global sum
    global today
    newWindow = Tk()
    newWindow.resizable(FALSE,FALSE)
    newWindow.title("Bill")
    newWindow.geometry("600x400")
    intro1 = Label(newWindow,text = "         CWU's LOCAL Cofee shop               ", fg = "green", font = "100")
    intro1.grid(row = 0, column = 2)
    d2 = today.strftime("Date: " + "%B %d, %Y")
    date = Label(newWindow, text = d2)
    date.grid(row = 1, column = 3)
    title1 = Label(newWindow, text = "Your total cost is: ")
    title1.grid(row = 5, column = 1,padx = 10)
    tot = Label(newWindow,text = "$" + str(sum))
    tot.grid(row = 5, column = 2)
    tax = 0.1 * sum
    round(tax,2)
    tax1 = Label(newWindow,text = "                     Tax :")
    tax1.grid(row = 6, column = 1) 
    tax2 = Label(newWindow,text ="$" + str(tax))
    tax2.grid(row = 6,column =2)
    title2 = Label(newWindow, text = "      Your total is: ")
    title2.grid(row = 8, column = 1,padx = 10)
    dash = Label(newWindow, text = "-------------------------------------")
    dash.grid(row = 7, column = 2)
    grand = tax + sum
    grand1 = Label(newWindow, text = "$" + str(grand))
    grand1.grid(row = 8,column = 2)
    empty = Label(newWindow, text = "")
    empty.grid(row = 9,column = 1)
    thank = Label(newWindow, text = "ThankYou for coming !!!",fg = "green",font = "10000")
    thank.grid(row = 11, column = 2)
    
    
    
#Function for main Window 
def MainWindow():
    #intro label
    intro = Label(window,text = "CWU's Local coffee shop", fg = "green", font = "200")
    intro.grid(row = 0, column = 2,padx = 10)
    
    #option to add new item on the cart.
    addnewItem = Button(window,text = "Add Item",width = 7, height = 1,command = addItem)
    addnewItem.grid(row = 6, column = 1,padx = 10,pady = 10)
    
    
    #option to checkout
    checkout = Button(window,text = "Checkout",width = 7, height = 1, command = bill)
    checkout.grid(row =9,  column = 5, padx = 12, pady = 10)
    
    #exit button
    logout  = Button(window,text = "Exit",width = 7,height = 1,command = ex)
    logout.grid(row = 6,column = 4,padx = 10,pady = 10)
    
    #label to select item
    itemLabel = Label(window, text = "Select Item")
    itemLabel.grid(row = 2,column = 0,padx = 5,pady = 10)
    
    #dropdown option to show menu
    dropDownOption = OptionMenu(window, itemVariable, *menu)
    dropDownOption.grid(row = 2,column = 1, padx = 1,pady = 10)
    
    #label size
    itemLabel1 = Label(window, text = "Select Size")
    itemLabel1.grid(row = 3,column = 0,padx = 1,pady = 10)
    
    #drop down option for size
    dropDownsize = OptionMenu(window, sizeVariable, *size)
    dropDownsize.grid(row = 3,column  = 1,padx = 2 ,pady = 1)
    
    #label for quantity
    quantity = Label(window,text = "Quantity")
    quantity.grid(row = 4, column = 0,padx = 10, pady = 2)    
    
    #entry box for quantity
    quantityEntry = Entry(window,textvariable = quantityvar )
    quantityEntry.grid(row = 4, column = 1, padx = 5, pady = 10)
    
    #label for bill
    billLabel = Label(window, text = "Bills")
    billLabel.grid(row = 7, column = 1)
    billTv.grid(row = 8, columnspan = 5)
    
    #setting scroll bar on treeview
    scrollbar = Scrollbar(window, orient  = "vertical",command = billTv.yview)
    scrollbar.grid(row = 8, column = 5,sticky = "NSE")
  
    
    billTv.configure(yscrollcommand = scrollbar.set)
    
    billTv.column("#0", width  = 0, minwidth = 25)
    billTv.column("#1", anchor  = W, minwidth = 120)
    billTv.column("#2", anchor  = CENTER, minwidth = 80)
    billTv.column("#3", anchor  = W, minwidth = 80)
    billTv.column("#4", anchor = CENTER, minwidth = 80)
    
    #headings for the treeview
    billTv.heading("#0", text = "I",anchor = W)
    billTv.heading("#1", text = "Item Name",anchor = W)
    billTv.heading("#2", text = "Size",anchor = CENTER)
    billTv.heading("#3", text = "Quantity",anchor = W)
    billTv.heading("#4", text = "Cost $",anchor = CENTER)
    
    
                   
    



###main
MainWindow()
window.mainloop()
