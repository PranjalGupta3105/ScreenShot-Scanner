from tkinter import *
#import tkinter as tk
from tkinter.filedialog import askopenfile
from engine import settingImagePath,image_ocr
import io
import os

app = Tk()


select_file_Label = Label(app , text='File Location', 
                        font=('bold', 14) ,pady=20)
select_file_Label.grid(row=0, column=0)

fileUrl = ''

# Set the Scanned Image text to the Text Element
def displayResult():
    # First Remove all of the previous Content in the Text Widget
    scannedImageViewer.delete("1.0",END)

    with open('scannedImage.txt', 'r', encoding="utf8") as f:
        scannedImageViewer.insert(INSERT, f.read())
        
    # Remove the File after file data has been displayed in the Text Widget
    os.remove('scannedImage.txt')

# To Open the Chose File Dialog Box
def FetchFile_DoOCR_DisplayResult():
    select_file_Dialog = askopenfile(mode ='r')
    if select_file_Dialog:
        #print(select_file_Dialog.name)
        fName = StringVar()
        fName = select_file_Dialog.name
        fileNameLabel = Label(app , text=fName, 
                        font=('bold', 14) ,pady=20)
        fileNameLabel.grid(row=0, column=3)
        fileUrl = settingImagePath(select_file_Dialog.name)
        DoOcrForImage(fileUrl)
        displayResult()


def DoOcrForImage(imageFile):
    image_ocr(imageFile,'scannedImage.txt')


chose_file_Button = Button(app, 
                        text='Select File',
                        width=14, 
                        padx=50, 
                        command=FetchFile_DoOCR_DisplayResult)
chose_file_Button.grid(row=0, column=2)


scannedImageViewer = Text(app, wrap=WORD, width=45, height= 20 )
scannedImageViewer.grid(row=1, column =0)

# Setting the Title of the application
app.title('Make My Notes')

# Set the Size of the Application Window
app.geometry('700x700')


#Start Program
app.mainloop()