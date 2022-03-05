import pyautogui 
import webbrowser as wb
import time
import lackey
import pandas as pd

# name = input("name of csv file :")
message = input("name of message txt file :")

# csv_data = pd.read_csv(name)

# csv_data = csv_data.to_numpy()
# print(csv_data)
# phone = list(csv_data[:,2])

# print(phone)

with open(message, 'r') as file:
    msg = file.readlines()


size = pyautogui.size()
if(size[0] > 40 and size[1] > 40):
    pyautogui.moveTo(20,20)

# phone = ["917539996785","919823290363"]
phone = ["917539996785","919823290363","919740776505","918660925038"]
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
    x = url + phone[i]
    pyautogui.write(x)
    pyautogui.press("enter")
    time.sleep(5)
    
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
    for i in msg:
        pyautogui.write(i[:-1])
        with pyautogui.hold('shift'):
            pyautogui.press('enter')
        time.sleep(0.5)
    time.sleep(0.5)
    pyautogui.press("enter")
    print("\n\n\n\n\n\n\n\n\n\n")
    time.sleep(1)
    

