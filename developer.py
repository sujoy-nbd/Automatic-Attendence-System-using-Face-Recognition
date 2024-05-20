from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\USER\python_Test_Projects\Images_GUI\dev.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\USER\python_Test_Projects\Images_GUI\developer.jpg")
        bg1=bg1.resize((1366,650),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=650)


        #title section
        title_lb1 = Label(bg_img,text="Developer Pannel",font=("verdana",25,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=35)
##--------------------------------------------

        dev_lbl=Label(self.root,text="My name is Sujoy Nandi",font=("tahoma",14,"bold"),fg="navyblue")
        dev_lbl.place(x=780,y=325)

        dev_lbl=Label(self.root,text="This is my major project based on Machine Learning.",font=("tahoma",12,"bold"),fg="navyblue")
        dev_lbl.place(x=720,y=355)

        hlp_img_btn=Image.open(r"C:\Users\USER\python_Test_Projects\Images_GUI\m1.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(self.root,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=1100,y=250,width=180,height=180)

        hlp_b1_1 = Button(bg_img,text="Sujoy Nandi",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=1100,y=295,width=180,height=35)
        





if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()