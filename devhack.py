import pyautogui 
import webbrowser as wb
import time
import lackey
import pandas as pd

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

print(msg)
print(phone)
print(lineno)




size = pyautogui.size()
if(size[0] > 40 and size[1] > 40):
    pyautogui.moveTo(20,20)



url = "https://web.whatsapp.com/send?phone="

wb.open('https://www.google.co.in/')
time.sleep(2)


search_symbol = []
type_box = []
search_symbol_better = []


for i in range(len(phone)):

    with pyautogui.hold('ctrl'):
        pyautogui.press('l') 
    pyautogui.press("backspace")
    x = url +"91"+ str(phone[i])
    print(x)
    pyautogui.write(x)
    pyautogui.press("enter")
    time.sleep(6)
    
    hover = False

    if(search_symbol != []):
        pyautogui.moveTo(search_symbol[0],search_symbol[1])
        time.sleep(2)
        pyautogui.scroll(-1000)
        time.sleep(0.5)


    if(type_box != [] ):
        print("i am using\n\n\n\n")
        print(type_box)
        pyautogui.moveTo(type_box[0],type_box[1])
        hover = True
        # lackey.newRegion(type_box,400,100)
        # if(lackey.exists("target1.jpg")):
        #     print("hi1")
        #     lackey.hover("target1.jpg")
        #     type_box = pyautogui.position()
        # elif(lackey.exists("targetd1.jpg")):
        #     lackey.hover("targetd1.jpg")
        #     type_box = pyautogui.position()

    elif(hover == False):
        print("\n\n\n\n\n\nF\n\n\n\n\n")
        if(lackey.exists("target1.jpg")):
            lackey.hover("target1.jpg")
            type_box = pyautogui.position()
        elif(lackey.exists("targetd1.jpg")):
            print(x)
            lackey.hover("targetd1.jpg")
            type_box = pyautogui.position()
        else:

            if(lackey.exists("search.jpg")):
                lackey.hover("search.jpg")
                search_symbol = type_box = pyautogui.position()
            elif(lackey.exists("searchd.jpg")):
                lackey.hover("searchd.jpg")
                search_symbol = type_box = pyautogui.position()
            
            pyautogui.scroll(-1000)

            if(lackey.exists("target1.jpg")):
                lackey.hover("target1.jpg")
                type_box = pyautogui.position()
            elif(lackey.exists("targetd1.jpg")):
                lackey.hover("targetd1.jpg")
                type_box = pyautogui.position()
            elif(lackey.exists("targetd.jpg")):
                lackey.hover("targetd.jpg")
                type_box = pyautogui.position()
            elif(lackey.exists("target.jpg")):
                lackey.hover("target.jpg")
                type_box = pyautogui.position()
    
    
    pyautogui.click()
    time.sleep(0.5)
    # pyautogui.write("hi bro")
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
    print("\n\n\n\n\n\n\n\n\n\n")
    time.sleep(1)
    

