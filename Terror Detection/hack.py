from pytube import YouTube
import cv2
def printtext():
    global e
    string = e.get()
    a=str(string)
    yt=YouTube(a)
    videos=yt.get_videos()
    s=1
    for v in videos:
        print(str(s) + ". "+str(v))
        s+=1
    n=int(input("Enter your choice to download"))
    vid=videos[n-1]
    destination='C:/Users/Aditya/Desktop/force'
    vid.download(destination)
    print(yt.filename+"\nHas Successfully Been Downloaded")

    cascade_src="gun.xml"
    video_src="gunvideoo.mp4"
    #video_src="Guns.mp4"
          
    cap=cv2.VideoCapture(video_src)
    #fgbg=createBackgroundSubtractorMOG2()
    car_cascade=cv2.CascadeClassifier(cascade_src)
    while True:
          ret,img=cap.read()
          #fgbg.apply(img)
          if(type(img)==type(None)):
              break
          gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
          count=0
          cars=car_cascade.detectMultiScale(gray,1.1,2)

          for(x,y,w,h) in cars:
                  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
                  count=count+1
          #cv2.imshow(vid,img)
          if cv2.waitKey(33)==27:
              break
          if count>2:
              print("Atleast 5 objects detected sending mail to the cyberpolice")

          import smtplib
          server = smtplib.SMTP('smtp.gmail.com', 587)
          server.starttls()
          #Next, log in to the server
          server.login("email_id@gmail.com", "password")
          
          #Send the mail
          msg = "Video Has High Amount of threat detected" 
          server.sendmail("y@gmail.com", "x@gmail.com", msg)
          print("Mail is successfully sent")
          exit()
          cv2.destroyAllWindows()
from tkinter import *
root=Tk()
root.title("Force One")
root.geometry("200x200")
logo=PhotoImage(file="army.gif")
w1=Label(root,image=logo).pack()
w = Label(root,text="Force One",font=("Helvetica",80),fg='#FF981D',bg='#8c0095')
w.place(relx=0.5,rely=0.1,anchor='n')

e=Entry(root)
e.place(relx=0.5,rely=0.5,anchor='n')
e.focus_set()
t=Label(root,text="Enter your link here",font=("Helvetica",15),fg='#FF981D',bg='#8c0095')
t.place(relx=0.5,rely=0.4,anchor='n')
b=Button(root,text='okay',command=printtext,fg='red')
b.pack(side='bottom')
b.place(relx=0.5,rely=0.6,anchor='n')


root.mainloop()
          
          













          
          
