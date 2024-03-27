import email,smtplib,ssl
import os
import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import inspect
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
batluc = ""
vl = "\ "
CurDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Trường THPT Chuyên Hà Tĩnh")
dialog_title = 'QUIT'
dialog_text = 'Are you sure?'

#answer = messagebox.askquestion(dialog_title, dialog_text)
 
window.geometry('1450x720')
window.configure(background='gray')


window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1,text = 'Giới thiệu')
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text = 'Lấy mẫu ảnh')
tab_control.pack(expand = 2,fill = 'both')
tab3 = ttk.Frame(tab_control)
tab_control.pack(expand = 2,fill = 'both')
tab_control.add(tab3,text = 'Điểm danh')
tab_control.pack(expand = 2,fill = 'both')
tab_control.pack(expand = 2,fill = 'both')
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4,text = 'Thống kê')
tab5 = ttk.Frame(tab_control)
tab_control.add(tab5,text = 'Điểm diện bằng biển số')
#window.configure(background='medium sea green')
message = tk.Label(window, text="PHẦN MỀM HỖ TRỢ QUẢN LÍ HỌC SINH TRUNG HỌC"  ,fg = "dark green",font=('times', 22,'bold')) 

message.place(x=300, y=40)

message12 = tk.Label(window, text="BẰNG KĨ THUẬT NHẬN DIỆN"   ,fg = "dark green",font=('times', 22 , 'bold')) 
message12.place(x=450,y=80)
lbl = tk.Label(tab2, text="NHẬP ID",width=20 ,fg = "red" ,height=2  ,font = ('helvetica',15,'bold')) 
lbl.place(x=400, y=200)

txt = tk.Entry(tab2,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=600, y=215)

lbl2 = tk.Label(tab2, text="NHẬP TÊN",width=20 ,fg = "red"   ,height=2 ,font=('helvetica', 15, ' bold ')) 
lbl2.place(x=400, y=300)

txt2 = tk.Entry(tab2,width=20  ,bg="white"  ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=600, y=315)

lbl3 = tk.Label(tab2, text="THÔNG BÁO : ",width=20 ,fg= "red"   ,height=2 ,font=('helvetica', 15, ' bold underline ')) 
lbl3.place(x=400, y=400)

message = tk.Label(tab2, text="" ,bg="white"  ,fg="red"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=600, y=400)

lbl4 = tk.Label(tab3, text="THỐNG KÊ KẾT QUẢ ĐIỂM DANH: ",width=30  ,fg="red"   ,height=2 ,font=('times', 15, ' bold  underline')) 
lbl4.place(x=800, y=200)

lbl5 = tk.Label(tab3, text="THỜI GIAN KẾT THÚC THỐNG KÊ",width=35  ,fg="red"    ,height=2 ,font=('times', 15, ' bold  underline')) 
lbl5.place(x=250, y=200)

lbl6 = tk.Label(tab3, text=" GIỜ ",width=4  ,fg="red" ,height=2 ,font=('times', 15)) 
lbl6.place(x=325, y=250)

txt3 = tk.Entry(tab3,width=2  ,bg="white"  ,fg="red",font=('times', 15, ' bold ') )
txt3.place(x=300,y=260)

txt4 = tk.Entry(tab3,width=2  ,bg="white"  ,fg="red",font=('times', 15, ' bold ') )
txt4.place(x=375,y=260)

lbl6 = tk.Label(tab3, text=" PHÚT ",width=4  ,fg="red" ,height=2 ,font=('times', 15)) 
lbl6.place(x=410, y=250)

lbl7 = tk.Label(tab3, text="LỚP : ",width=5  ,fg="red"  ,height=2 ,font=('times', 15, ' bold  underline')) 
lbl7.place(x=300, y=300)

txt5 = tk.Entry(tab3,width=4  ,bg="white"  ,fg="red",font=('times', 15, ' bold ') )
txt5.place(x=380,y=310)

lbl8 = tk.Label(tab4, text="GMAIL CB QUẢN LÍ : ",width=30  ,fg="red"    ,height=2 ,font=('times', 15, ' bold  underline')) 
lbl8.place(x=230, y=200)

lbl9 = tk.Label(tab4, text="THỐNG KÊ KẾT QUẢ ĐIỂM DANH : ",width=30  ,fg="red"   ,height=2 ,font=('times', 15, ' bold  underline')) 
lbl9.place(x=900, y=200)

txt6 = tk.Entry(tab4,width=30  ,bg="white"  ,fg="red",font=('times', 15, ' bold ') )
txt6.place(x=550,y=210)

message2 = tk.Label(tab3, text="" ,fg="red"   ,bg="white",activeforeground = "light grey",width=30  ,height=2  ,font=('times', 10, ' bold ')) 
message2.place(x=800, y=300)
message2.config(width = 60,height = 20)

message3 = tk.Label(tab4, text="" ,fg="red"   ,bg="white",activeforeground = "light grey",width=30  ,height=2  ,font=('times', 10, ' bold ')) 
message3.place(x=900, y=300)
message3.config(width = 60,height = 20)
def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
anh = os.getcwd() + vl[0] + 'unnamed.jpg'
img  = Image.open(anh) 
photo=ImageTk.PhotoImage(img)
lab=tk.Label(tab4,image=photo).place(x=300,y=400)
#chụp ảnh để train
def TakeImages():        
    Id=(txt.get())
    name=(txt2.get())
    # CreateFolder(CurDir+"\\DoneTrain\\"+name)
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>100:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Anh cua ban da duoc luu"
        row = [Id , name]
        with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)
#train các ảnh đã chụp
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("trainner.yml")
    res = "Hoan thanh" #+",".join(str(f) for f in Id)
    message.configure(text= res)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)  

    # for imageDone in os.listdir('TrainingImage\\'):
    #     MoveFile(CurDir+"\\TrainingImage\\"+imageDone,CurDir+"\\DoneTrain\\"+str(txt2.get())+"\\")
    return faces,Ids
#nhận diện khuôn mặt trên CAMERA
def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time','Nhan xet']
    attendance = pd.DataFrame(columns = col_names)
    sampleNum = 0
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            if(conf < 50):
                gio = int(txt3.get())
                phut = int(txt4.get())
                now = datetime.datetime.now()
                today6h45 = now.replace(hour = gio , minute = phut , second = 0)
                lop = txt5.get()
                sampleNum=sampleNum+1
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                fileName="Attendance\lop" + txt5.get() + date+".csv"
                batluc=fileName
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                if(today6h45<now):
                    res = "Muon hoc"
                    attendance.loc[len(attendance)] = [Id,aa,date,now,res]
                else:
                    attendance.loc[len(attendance)] = [Id,aa,date,now]
                if(sampleNum==1):
                    message2.configure(text= attendance)
                    message3.configure(text = attendance)
                    attendance.to_csv(fileName,index=False)
                    sampleNum = 2
                #sampleNum=sampleNum+1
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
        cv2.imshow('im',im)
        if (cv2.waitKey(1)==ord('q')):
            break
        elif(sampleNum > 15):
            break
    cam.release()
    cv2.destroyAllWindows()
def guigmail():
    batluc="Attendance\lop" + txt5.get() + date+ ".csv"
    subject = "Bao cao thoi gian den truong lop " + txt5.get()
    body = "Bao cao thoi gian den truong"
    sender_email = "nhandiencht@gmail.com"
    receiver_email = txt6.get()
    password = "giap10t2"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email
    message.attach(MIMEText(body, "plain"))
    filename = os.getcwd() + vl[0] + batluc  
    with open(filename, "rb") as attachment:
   
         part = MIMEBase("application", "octet-stream")
         part.set_payload(attachment.read())

 
    encoders.encode_base64(part)


    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )


    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
message4 = tk.Label(tab1,text="Nhóm thực hiện : "    ,font=('helvetica', 14))
message4.place(x=800,y=170)
message5 = tk.Label(tab1,text = "Nguyễn Văn Giáp",font = ('helvetica',14))
message5.place(x=950,y=170)
message6 = tk.Label(tab1,text = "Trịnh Duy Tài",font = ('helvetica',14))
message6.place(x=950,y=200)
message7 = tk.Label(tab1,text = "Phần mềm hỗ trợ quản lí học sinh trung học bằng kĩ thuật nhận diện khuôn mặt là phần mềm miễn phí, dễ cài đặt và dễ ",font = ('helvetica',14))
message7.place(x=200,y=280)
message8 = tk.Label(tab1,text = "sử dụng. Cung cấp công cụ hỗ trợ quản lí học sinh một cách khoa học, chính xác, nhanh chóng.",font = ('helvetica',14))
message8.place(x=200,y=310)
message9 = tk.Label(tab1,text = "Ý kiến - Hỗ trợ",font = ('helvetica',14))
message9.place(x=950,y=400)
message10 = tk.Label(tab1,text = "Email : nhandiencht@gmail.com" ,font = ('helvetica',14))
message10.place(x=950,y=450)
message11 = tk.Label(tab1,text = "SĐT : 0982097315" , font = ('helvetica',14))
message11.place(x=950,y=500)
clearButton = tk.Button(tab2, text="Xóa", command=clear  ,fg="red"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('calibri', 15, ' bold '))
clearButton.place(x=850, y=200)
clearButton2 = tk.Button(tab2, text="Xóa", command=clear2  ,fg="red"    ,width=20  ,height=2, activebackground = "Red" ,font=('calibri', 15, ' bold '))
clearButton2.place(x=850, y=300)    
takeImg = tk.Button(tab2, text="LẤY MẪU ẢNH", command=TakeImages  ,fg="red"  ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
takeImg.place(x=300, y=500)
trainImg = tk.Button(tab2, text="XỬ LÍ ẢNH", command=TrainImages  ,fg="red"    ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
trainImg.place(x=850, y=500)
trackImg = tk.Button(tab3, text="NHẬN DIỆN", command=TrackImages  ,fg="red"  ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
trackImg.place(x=300, y=380)
quitWindow = tk.Button(tab4, text="GỬI GMAIL", command=guigmail  ,fg="red"  ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
quitWindow.place(x=300, y=300)
copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,font=('times', 30, 'italic bold underline'))
copyWrite.tag_configure("superscript", offset=10)
copyWrite.insert("insert", "Developed by NguyenGiap","", "CHT")
copyWrite.configure(state="disabled",fg="red"  )
copyWrite.pack(side="left")
copyWrite.place(x=800, y=750)
window.mainloop()
