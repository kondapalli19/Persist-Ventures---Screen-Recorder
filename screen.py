import cv2
import numpy as np
import pyautogui
from tkinter import messagebox
from tkinter import *
import json
import requests
import threading
from PIL import ImageTk, Image

#Define the user interface
voice_rec = Tk()
voice_rec.geometry("360x200")
voice_rec.config(bg="#107dc2")

# Set the "topmost" attribute to True
voice_rec.wm_attributes("-topmost", True)

# Get the size of the screen using pyautogui
SCREEN_SIZE = tuple(pyautogui.size())




# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (SCREEN_SIZE))
def jojo():
    while True:
        # Capture the screen
        img = pyautogui.screenshot()

        # Convert the image into numpy array
        img = np.array(img)

        # Convert the color space from BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        

        # Write the frame into the file 'output.avi'
        out.write(img)



def stop_rec():
    headers = {"Authorization": "Bearer ya29.a0AWY7Ckl65XNy1pNO_4S6Kvaq2Rq0lqAzDuc_L1qmYf69zHBzf3RicfmijhbvcCFyFjEcLtP7aNzx2q2MXINSByuZcKMC6dGp8uUAlctMnkLx2aGsv99-GJZ9t21-mUIgj_XRCC_JXK0CuePJEpu44euQcBlvaCgYKAb4SARISFQG1tDrpWzuw1PMrQkUq3aEu3G1R6g0163"}
    para = {
        "name": "output.avi",
        "parents": ["1JNet7fCNdJTqD8F3D5X7qwoh2d6FMupH"]
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("./output.avi", "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )



img_file = "./logo.png"
img = Image.open(img_file)

# Resize the image if needed
img = img.resize((70, 70), Image.ANTIALIAS)

# Convert the image to a PhotoImage object
img_tk = ImageTk.PhotoImage(img)

# Create a label to display the image
img_label = Label(voice_rec, image=img_tk)
img_label.grid(row=0, column=0, rowspan=3, padx=10, pady=20)

# Added Manually
record_btn = Button(voice_rec, text="Screen Record", command=threading.Thread(target=jojo).start)
#Stop button
stop_btn = Button(voice_rec, text= "Upload to Cloud", command=threading.Thread(target=stop_rec).start)



#Position buttons
record_btn.grid(row=5,column=2, rowspan=3, padx=10, pady=20)
stop_btn.grid(row=5,column=3, rowspan=3, padx=10, pady=20)

voice_rec.mainloop()



out.release()
cv2.destroyAllWindows()