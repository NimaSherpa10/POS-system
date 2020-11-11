from tkinter import *
from tkinter import ttk
from datetime import date 
window = Tk()
window.title("POINT OF SALE")

#menu
menu = ["Americano", "Latte", "Mocha", "Hot Choclate"]
size = ["Large","Small"]
itemVariable = StringVar()
sizeVariable = StringVar()
sizeVariable.set(size[1])
quantityvar = StringVar()
quantityvar.set("0")
i = 0
sum = 0
#Tree view
billTv = ttk.Treeview(window,height = 15, column = ('items','size','quantity','Total cost'))
today = date.today()

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
    
def addItem():
    global itemVariable
    global billTv
    global quantityvar
    global costVar
    global sizeVariable
    global i
    global sum
    billTv.insert(parent = '',index= 'end',iid= i,text = ">     ",values = (itemVariable.get(),sizeVariable.get()+ "                        ",quantityvar.get(),total()))
    sum  += total()
    i = i + 1    

 
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
   # newWindow = Toplevel(window)
    newWindow = Tk()
    newWindow.title("Bill")
    newWindow.geometry("600x800")
    intro1 = Label(newWindow,text = "                    म्याग दाई को चिया पसल !!                 ", fg = "green", font = "10000")
    intro1.grid(row = 0, column = 4,padx = 100)
    d2 = today.strftime("%B %d, %Y")
    date = Label(newWindow, text = d2)
    date.grid(row = 1, column = 5, padx= 10, pady = 10)
#Function for main Window 
def MainWindow():
    intro = Label(window,text = "Laure Local COFEE SHOP", fg = "red", font = "10000")
    intro.grid(row = 0, column = 3,padx = 50)
    
    #option to add new item on the cart.
    addnewItem = Button(window,text = "Add Item",width = 7, height = 1,command = addItem)
    addnewItem.grid(row = 6, column = 1,padx = 10,pady = 10)
    
    
    #option to checkout
    checkout = Button(window,text = "Checkout",width = 7, height = 1, command = bill)
    checkout.grid(row =9,  column = 5, padx = 12, pady = 10)
    
    #exit button
    logout  = Button(window,text = "Exit",width = 7,height = 1,command = window.destroy)
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
    
    quantity = Label(window,text = "Quantity")
    quantity.grid(row = 4, column = 0,padx = 10, pady = 2)    
    
    quantityEntry = Entry(window,textvariable = quantityvar )
    quantityEntry.grid(row = 4, column = 1, padx = 5, pady = 10)
    
    
    billLabel = Label(window, text = "Bills")
    billLabel.grid(row = 7, column = 1)
    billTv.grid(row = 8, columnspan = 5)
    
    scrollbar = Scrollbar(window, orient  = "vertical",command = billTv.yview)
    scrollbar.grid(row = 8, column = 5,sticky = "NSE")
  
    
    billTv.configure(yscrollcommand = scrollbar.set)
    
    billTv.column("#0", width  = 0, minwidth = 25)
    billTv.column("#1", anchor  = W, minwidth = 120)
    billTv.column("#2", anchor  = CENTER, minwidth = 80)
    billTv.column("#3", anchor  = W, minwidth = 80)
    billTv.column("#4", anchor = CENTER, minwidth = 80)
    
    billTv.heading("#0", text = "I",anchor = W)
    billTv.heading("#1", text = "Item Name",anchor = W)
    billTv.heading("#2", text = "Size",anchor = CENTER)
    billTv.heading("#3", text = "Quantity",anchor = W)
    billTv.heading("#4", text = "Cost $",anchor = CENTER)
    
    
                   
    



###main
MainWindow()
window.mainloop()