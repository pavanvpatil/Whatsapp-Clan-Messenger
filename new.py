import imp
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

from tkinter.filedialog import askopenfile
import pandas as pd 
root = Tk()
root.geometry('300x400')

def sel():
   global selection
   selection = str(var.get())
   if(selection == "1"):
       btn = Button(root, text ='Upload .csv file containing phone numbers with names', command = lambda:open_file_phone_numbers())
       btn.pack(side = TOP, pady = 10)
   elif(selection == "2"):
        btn = Button(root, text ='Upload .csv file containing phone numbers', command = lambda:open_file_phone_numbers())
        btn.pack(side = TOP, pady = 10)
        

def open_file_phone_numbers():
    global csv_data
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.csv')])
    if file is not None:
        csv_data = pd.read_csv(file)
  
def open_file_message():
    global msg
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.txt')])
    if file is not None:
        msg = file.readlines()

        

def disable_button():
    root.destroy()


var = IntVar()
R1 = Radiobutton(root, text="Does your csv file contain name in first coloumn", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Excluding names", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )
Button(root, text= "Quit", command= disable_button, width= 20).pack(pady=20)

label = Label(root)
label.pack()
print(R1)

btn = Button(root, text ='Upload .txt file containing messages', command = lambda:open_file_message())
btn.pack(side = TOP, pady = 10)

print()
root.mainloop()
if selection == '1':
    if 'Name' in list(csv_data.columns.values) :
        Names = csv_data['Name'].to_numpy()
    elif 'name' in list(csv_data.columns.values):
        Names = csv_data['Name'].to_numpy()
    else:
        messagebox.showerror("Error","The input csv file does not have a Name coloumn")

if 'Phone' in list(csv_data.columns.values):
    Phone = csv_data['Phone'].to_numpy()
elif 'phone' in list(csv_data.columns.values):
    Phone = csv_data['phone'].to_numpy()
else:
    messagebox.showerror("Error","The input csv file does not have a Phone coloumn")



    
    
