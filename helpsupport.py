from tkinter import*
from PIL import Image,ImageTk
import webbrowser


class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")
# first header image.................  
        img=Image.open(r"C:\Users\USER\python_Test_Projects\Images_GUI\banner.jpg")
        img=img.resize((1366,135),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

 # backgorund image................ 
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        bg1=Image.open(r"C:\Users\USER\python_Test_Projects\Images_GUI\helpdesk.jpg")
        bg1=bg1.resize((1366,648),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=648)


#title section..................

        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",25,"bold"),bg="Red",fg="#b6fff4")
        title_lb1.place(x=0,y=0,width=1366,height=42)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"C:\Users\USER\python_Test_Projects\Images_GUI\insta.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.insta,image=self.std_img1,cursor="hand2")
        std_b1.place(x=300,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.insta,text="Instagram",cursor="hand2",font=("tahoma",15,"bold"),bg="darkblue",fg="#b6fff4")
        std_b1_1.place(x=300,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\USER\python_Test_Projects\Images_GUI\fb.png")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=530,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="darkblue",fg="#b6fff4")
        det_b1_1.place(x=530,y=380,width=180,height=45)


         # Help  Support  button 4
        hlp_img_btn=Image.open(r"C:\Users\USER\python_Test_Projects\Images_GUI\gmail.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=760,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="darkblue",fg="#b6fff4")
        hlp_b1_1.place(x=760,y=380,width=180,height=45)


        # create function for button 
    
    
    def insta(self):
        self.new = 1
        self.url = "https://instagram.com/sujoynandi01?igshid=ZDdkNTZiNTM="
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/profile.php?id=100012124987341&mibextid=ZbWKwL"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.open(self.url,new=self.new)






if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()