import pyautogui 
import webbrowser as wb
import time
import lackey
import pandas as pd
import sys
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

from tkinter.filedialog import askopenfile
import pandas as pd 
root = Tk()
root.geometry('300x400')
imagePath = ""
def open_file():
    global imagePath
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*g')])
    imagePath =  file_path.name[:]
    if file_path is not None:
        pass

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


label = Label(root)
label.pack()


btn = Button(root, text ='Upload .txt file containing messages', command = lambda:open_file_message())
btn.pack(side = TOP, pady = 10)

btn = Button(root, text ='Upload .jpg', command = lambda:open_file())
btn.pack(side = TOP, pady = 10)

Button(root, text= "RUN", command= disable_button, width= 20).pack(pady=20)

root.mainloop()
if selection == '1':
    if 'Name' in list(csv_data.columns.values) :
        Names = list(csv_data['Name'])
    elif 'name' in list(csv_data.columns.values):
        Names = list(csv_data['Name'])
    else:
        messagebox.showerror("Error","The input csv file does not have a Name coloumn")

if 'Phone' in list(csv_data.columns.values):
    phone = list(csv_data['Phone'])
elif 'phone' in list(csv_data.columns.values):
    phone = list(csv_data['phone'])
else:
    messagebox.showerror("Error","The input csv file does not have a Phone coloumn")


lineno= []
x =0
for i in msg:
    if (i.find("__Name__") != -1):
        lineno.append(x)
    x +=1




size = pyautogui.size()
if(size[0] > 40 and size[1] > 40):
    pyautogui.moveTo(30,30)

initial = pyautogui.position()



url = "https://web.whatsapp.com/send?phone="

wb.open('https://www.google.co.in/')
time.sleep(2)


search_symbol = []
type_box = []
search_symbol_better = []

count = 1
for i in range(len(phone)):

    with pyautogui.hold('ctrl'):
        pyautogui.press('l') 
    pyautogui.press("backspace")
    x = url +"91"+ str(phone[i])
    print(x)
    pyautogui.write(x)
    pyautogui.press("enter")
    time.sleep(8)
    
    hover = False

    if(type_box != [] ):
        pyautogui.moveTo(type_box[0],type_box[1])
        hover = True

    elif(hover == False):

        lackey.hover(imagePath)
        type_box = pyautogui.position()
        hover = True

    final = pyautogui.position()
    
    if(count == 1 and initial[0] == final[0] and initial[1] == final[1]):
        messagebox.showerror("Error","UPLOAD WHATSAPP'S TEXT BOX IMAGE")
        sys.exit(0)
        count +=1
        

    
    pyautogui.click()
    time.sleep(0.5)

    line = 0 
    for j in msg:
        if(line not in lineno):
            pyautogui.write(j[:-1])
        else:
            pyautogui.write(j[:-1].replace("__Name__",str(Names[i])))
        with pyautogui.hold('shift'):
            pyautogui.press('enter')
        time.sleep(0.5)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)
    

