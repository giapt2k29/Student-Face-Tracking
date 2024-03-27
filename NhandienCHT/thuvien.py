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

vl = "\ "
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1,text = 'Giới thiệu')
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab2, text = 'Nhập sách')
tab_control.add(tab3, text = 'Lấy thông tin bạn đọc')
tab_control.pack(expand = 2,fill = 'both')
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4,text = 'Mượn/trả sách')
tab5 = ttk.Frame(tab_control)
tab_control.add(tab5,text = 'Tra cứu')
message = tk.Label(window, text="PHẦN MỀM QUẢN LÍ MƯỢN/TRẢ SÁCH THƯ VIỆN TRƯỜNG TRUNG HỌC"  ,fg = "dark blue",font=('times', 22,'bold')) 
tab6 = ttk.Frame(tab_control)
tab_control.add(tab6,text = 'Thống kê')
message.place(x=150, y=40)

lbl = tk.Label(tab3, text="NHẬP MÃ HS",width=20 ,fg = "dark green" ,height=2  ,font = ('helvetica',15,'bold')) 
lbl.place(x=400, y=150)

txt = tk.Entry(tab3,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=600, y=165)

lbl2 = tk.Label(tab3, text="NHẬP TÊN",width=20 ,fg = "dark green"   ,height=2 ,font=('helvetica', 15, ' bold ')) 
lbl2.place(x=400, y=250)

txt2 = tk.Entry(tab3,width=20  ,bg="white"  ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=600, y=265)

lbl3 = tk.Label(tab3, text="GMAIL",width=20 ,fg = "dark green"   ,height=2 ,font=('helvetica', 15, ' bold ')) 
lbl3.place(x=400, y=350)

txt3 = tk.Entry(tab3,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt3.place(x=600, y=365)

lbl4 = tk.Label(tab3, text="LỚP",width=20 ,fg = "dark green"   ,height=2 ,font=('helvetica', 15, ' bold ')) 
lbl4.place(x=400, y=450)

txt4 = tk.Entry(tab3,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt4.place(x=600, y=465)

lbl5 = tk.Label(tab2, text="MÃ SÁCH",width=20 ,fg = "dark green"   ,height=2 ,font=('helvetica', 15, ' bold ')) 
lbl5.place(x=200, y=200)

txt5 = tk.Entry(tab2,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt5.place(x=400, y=215)

lbl6 = tk.Label(tab2, text="TÊN SÁCH",width=20 ,fg = "dark green"   ,height=2 ,font=('helvetica', 15, ' bold ')) 
lbl6.place(x=800, y=200)

txt6 = tk.Entry(tab2  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt6.place(x=1000, y=215)

lbl7 = tk.Label(tab2, text="NXB",width=20 ,fg = "dark green"   ,height=2 ,font=('helvetica', 15, ' bold ')) 
lbl7.place(x=175, y=300)

txt7 = tk.Entry(tab2,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt7.place(x=400, y=315)

lbl8 = tk.Label(tab2, text="GIÁ SÁCH",width=20 ,fg = "dark green"   ,height=2 ,font=('helvetica', 15, ' bold ')) 
lbl8.place(x=800, y=300)

txt8 = tk.Entry(tab2,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt8.place(x=1000, y=315)

lbl9 = tk.Label(tab5, text="NHẬP MÃ SÁCH",width=20 ,fg = "dark green" ,height=2  ,font = ('helvetica',15,'bold')) 
lbl9.place(x=300, y=250)

txt9 = tk.Entry(tab5,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt9.place(x=550, y=265)

lbl10 = tk.Label(tab5, text="NHẬP TÊN SÁCH",width=20 ,fg = "dark green" ,height=2  ,font = ('helvetica',15,'bold')) 
lbl10.place(x=300, y=365)

txt10 = tk.Entry(tab5,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt10.place(x=550, y=380)


lbl9 = tk.Label(tab4, text="SỐ NGÀY MUỐN MƯỢN : ",width=20 ,fg = "dark green" ,height=2  ,font = ('helvetica',15,'bold')) 
lbl9.place(x=500, y=350)

txt9 = tk.Entry(tab4,width=2  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt9.place(x=750, y=365)

lbl10 = tk.Label(tab4, text="NGÀY" ,fg = "dark green" ,height=2  ,font = ('helvetica',15,'bold')) 
lbl10.place(x=775, y=350)

lbl9 = tk.Label(tab5, text="TÁC PHẨM CỦA TÁC GIẢ : " ,fg = "dark green"   ,font = ('helvetica',15,'bold')) 
lbl9.place(x=250, y=475)

txt11 = tk.Entry(tab5,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt11.place(x=550, y=475)

lbl12 = tk.Label(tab2, text="XÓA SÁCH : " ,fg = "dark green"   ,font = ('helvetica',15,'bold')) 
lbl12.place(x=450, y=500)

txt12 = tk.Entry(tab2,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt12.place(x=600, y=500)

lbl13 = tk.Label(tab4, text="MÃ SÁCH : " ,fg = "dark green"   ,font = ('helvetica',15,'bold')) 
lbl13.place(x=450, y=250)

txt13 = tk.Entry(tab4,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt13.place(x=600, y=250)

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
def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)
def clear4():
    txt4.delete(0,'end')
    res = ""
    message.configure(text =res)
def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)
def clear3():
    txt3.delete(0, 'end')    
    res = ""
    message.configure(text= res)
def TakeImages():        
    Id=(txt.get())
    name=(txt2.get())
    lop = txt4.get()
    gmail = txt3.get()
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
        row1 = [Id , name , gmail , lop]
        with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row1)
        csvFile.close()
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
        if(name.isalpha()):
            res = "Enter Numeric Id"
#train các ảnh đã chụp
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("trainner.yml")

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
def Nhapsach():
    masach = txt5.get()
    tensach = txt6.get()
    NXB = txt7.get()
    giasach = txt8.get()
    row1 = [masach,tensach,NXB,giasach]
    with open('BookDetails\BookDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row1)
    csvFile.close()
def Tracuuma():
    with open('BookDetails\BookDetails.csv','a+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row1)
    csvFile.close()
def Tracuuten():
    with open('BookDetails\BookDetails.csv','a+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row1)
    csvFile.close()
kt = 0
def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time','Sach da muon']
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
                
                now = datetime.datetime.now()
                sampleNum=sampleNum+1
                ts = time.time()
                date2 = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')

                fileName="Attendance\MS" + str(Id) +".csv"
                
                aa=df.loc[df['Id'] == Id]['Name'].values
                
                gg = df.loc[df['Id'] == Id][df['Name']==aa]['Gmail'].values
                tt=str(Id)+"-"+aa
                print(aa)
                attendance.loc[len(attendance)] = [Id,aa,date2,now,txt13.get()]
                if(sampleNum==1):
                    if(kt==0):
                        col_names2 = ['Ma hoc sinh','Ten hoc sinh','Ma sach']
                        thongke = pd.DataFrame(columns = col_names2)
                        kt=1
                    row2 = [ID,aa,txt13.get()]
                    with open(thongke) as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(row2)
                    date = datetime.datetime.fromtimestamp(ts).strftime('%d')
                    month = datetime.datetime.fromtimestamp(ts).strftime('%m')
                    year = datetime.datetime.fromtimestamp(ts).strftime('%Y')
                    res = "Han muon sach cua ban sap het"
                    date1 = str(int(date)+3) + vl[0] + month + vl[0] + year

                    row = [res , Id , date1,gg]
                    with open('Gmail\Gmail.csv','a+') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(row)
                    csvFile.close()
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
message4 = tk.Label(tab1,text="Nhóm thực hiện : "    ,font=('helvetica', 14))
message4.place(x=800,y=170)
message5 = tk.Label(tab1,text = "Nguyễn Văn Giáp",font = ('helvetica',14))
message5.place(x=950,y=170)
message6 = tk.Label(tab1,text = "Trịnh Duy Tài",font = ('helvetica',14))
message6.place(x=950,y=200)
message7 = tk.Label(tab1,text = "Phần mềm hỗ trợ quản lí thư viện trường trung học bằng kĩ thuật nhận diện khuôn mặt là phần mềm miễn phí, dễ cài đặt và dễ ",font = ('helvetica',14))
message7.place(x=200,y=280)
message8 = tk.Label(tab1,text = "sử dụng. Cung cấp công cụ hỗ trợ quản lí thư viện một cách khoa học, chính xác, nhanh chóng.",font = ('helvetica',14))
message8.place(x=200,y=310)
message9 = tk.Label(tab1,text = "Ý kiến - Hỗ trợ",font = ('helvetica',14))
message9.place(x=950,y=400)
message10 = tk.Label(tab1,text = "Email : nhandiencht@gmail.com" ,font = ('helvetica',14))
message10.place(x=950,y=450)
message11 = tk.Label(tab1,text = "SĐT : 0982097315" , font = ('helvetica',14))
message11.place(x=950,y=500)
takeImg = tk.Button(tab3, text="LẤY MẪU ẢNH", command=TakeImages  ,fg="dark green"  ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
takeImg.place(x=300, y=550)
trainImg = tk.Button(tab3, text="XỬ LÍ ẢNH", command=TrainImages  ,fg="dark green"    ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
trainImg.place(x=850, y=550)
clearButton = tk.Button(tab3, text="Xóa", command=clear  ,fg="dark green"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('calibri', 15, ' bold '))
clearButton.place(x=850, y=150)
clearButton2 = tk.Button(tab3, text="Xóa", command=clear2  ,fg="dark green"    ,width=20  ,height=2, activebackground = "Red" ,font=('calibri', 15, ' bold '))
clearButton2.place(x=850, y=250)
clearButton3 = tk.Button(tab3, text="Xóa", command=clear3  ,fg="dark green"    ,width=20  ,height=2, activebackground = "Red" ,font=('calibri', 15, ' bold '))
clearButton3.place(x=850, y=350)
clearButton4 = tk.Button(tab3, text="Xóa", command=clear4  ,fg="dark green"    ,width=20  ,height=2, activebackground = "Red" ,font=('calibri', 15, ' bold '))
clearButton4.place(x=850, y=450)
nhapsach = tk.Button(tab2, text="NHẬP SÁCH", command=Nhapsach  ,fg="dark green"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('calibri', 15, ' bold '))
nhapsach.place(x=650, y=350)
trackImg = tk.Button(tab4, text="MƯỢN SÁCH", command=TrackImages  ,fg="dark green"  ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
trackImg.place(x=400, y=500)
trasach = tk.Button(tab4, text="TRẢ SÁCH", command=TrackImages  ,fg="dark green"  ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
trasach.place(x=800, y=500)
tracuuma = tk.Button(tab5, text="TRA CỨU", command=Tracuuma  ,fg="dark green"  ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
tracuuma.place(x=800, y=240)
tracuuten = tk.Button(tab5, text="TRA CỨU", command=Tracuuten  ,fg="dark green"  ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
tracuuten.place(x=800, y=340)
tracuutacgia = tk.Button(tab5, text="TRA CỨU", command=Tracuuten  ,fg="dark green"  ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
tracuutacgia.place(x=800, y=455)
mavach = tk.Button(tab4, text="QUÉT MÃ SÁCH", command=Tracuuten  ,fg="dark green"  ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
mavach.place(x=850, y=200)
xoasach =tk.Button(tab2, text="XÁC NHẬN", command=Tracuuten  ,fg="dark green"  ,width=20  ,height=3, activebackground = "Red" ,font=('calibri', 15, ' bold '))
xoasach.place(x=850, y=475)
anh2 = os.getcwd() + vl[0] + 'anhthuvien.jpg'
img  = Image.open(anh2) 
photo=ImageTk.PhotoImage(img)
lab=tk.Label(tab1,image=photo).place(x=300,y=400)

window.mainloop()
    
    
