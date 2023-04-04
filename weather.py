from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder 
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk



root = Tk()

root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)


def getweather():
    city= textfield.get()
    
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj= TimezoneFinder()
    
    result= obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N {round(location.longitude,4)}°E")

    home =pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M-%p")
    clock.config(text=current_time)
    
    #weather
    
    api="https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=1fcbb9d84754539ceb0045c9dbd1b844" 
    json_data=requests.get(api).json()
    
    #current
    
    temp = json_data['current']['temp']
    humidity= json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
    
    print(temp)
    print(humidity)
    print(pressure)
    print(wind)
    print(description)
    
    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)
    
    
    #firstCell
    
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
    photo1 = ImageTk.PhotoImage(file=f"icon\{firstdayimage}@2x.png")
    
    firstImage.config(image=photo1)
    firstImage.image=photo1
    
    #secondcell
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']
    
    img=(Image.open(f"icon\{seconddayimage}@2x.png"))
    resized_image=img.resize(((50,50)))
    photo2= ImageTk.PhotoImage(resized_image)
    secondImage.config(image=photo2)
    secondImage.image=photo2
    
    #Thirdcell
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']
    
    img=(Image.open(f"icon\{thirddayimage}@2x.png"))
    resized_image=img.resize(((50,50)))
    photo3= ImageTk.PhotoImage(resized_image)
    thirdImage.config(image=photo3)
    thirdImage.image=photo3
    
    #Fourthcell
    fourdayimage = json_data['daily'][3]['weather'][0]['icon']
    
    img=(Image.open(f"icon\{fourdayimage}@2x.png"))
    resized_image=img.resize(((50,50)))
    photo4= ImageTk.PhotoImage(resized_image)
    fourImage.config(image=photo4)
    fourImage.image=photo4
    
    #Fifthcell
    fivedayimage = json_data['daily'][4]['weather'][0]['icon']
    
    img=(Image.open(f"icon\{fivedayimage}@2x.png"))
    resized_image=img.resize(((50,50)))
    photo5= ImageTk.PhotoImage(resized_image)
    fiveImage.config(image=photo5)
    fiveImage.image=photo5
    
    tempday1= json_data['daily'][0]['temp']['day']
    tempnight1= json_data['daily'][0]['temp']['night']
    
    day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")
    
    
    #sixcell
    sixdayimage = json_data['daily'][5]['weather'][0]['icon']
    
    img=(Image.open(f"icon\{fivedayimage}@2x.png"))
    resized_image=img.resize(((50,50)))
    photo6= ImageTk.PhotoImage(resized_image)
    sixthImage.config(image=photo6)
    sixthImage.image=photo6
    
    #Sevencell
    sevendayimage = json_data['daily'][6]['weather'][0]['icon']
    
    img=(Image.open(f"icon\{sevendayimage}@2x.png"))
    resized_image=img.resize(((50,50)))
    photo7= ImageTk.PhotoImage(resized_image)
    sevenImage.config(image=photo7)
    sevenImage.image=photo7
    
  #days
  
    first = datetime.now()
    day1.config(text=first.strftime("%A"))
    
    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))
    
    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))
    
    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))
    
    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))
         
    six = first+timedelta(days=5)
    day6.config(text=six.strftime("%A"))
    
    seven = first+timedelta(days=6)
    day7.config(text=seven.strftime("%A"))
       
    
#icon

image_icon = PhotoImage(file="images/logo.png")
root.iconphoto(False,image_icon)

Round_box= PhotoImage(file="images/Rounded Rectangle 1.png")
Label(root,image=Round_box,bg="#57adff").place(x=30,y=110)

#Label
label1=Label(root,text="Temprature",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=50,y=120)

label2=Label(root,text="Humidty",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=50,y=140)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=50,y=160)

label4=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=50,y=180)

label5=Label(root,text="Description",font=('Helvetica',11),fg="white",bg="#203243")
label5.place(x=50,y=200)


#SearchBox

Search_Image= PhotoImage(file='images/Rounded Rectangle 3.png')
myimage=Label(image=Search_Image,bg="#57adff")
myimage.place(x=270,y=120)


weath_image= PhotoImage(file="images/Layer 7.png")
weather_image= Label(root,image=weath_image,bg="#203243")
weather_image.place(x=290,y=127)

textfield= tk.Entry(root,justify='center', width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

Search_icon = PhotoImage(file="images/Layer 6.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getweather)
myimage_icon.place(x=645,y=125)

#Bottom Box

frame= Frame(root, width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

#Bottom Boxes

firstbox= PhotoImage(file="images/Rounded Rectangle 2.png")
secondbox= PhotoImage(file="images/Rounded Rectangle 2 copy.png")

Label(frame,image=firstbox, bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox, bg="#212120").place(x=300,y=20)
Label(frame,image=secondbox, bg="#212120").place(x=400,y=20)
Label(frame,image=secondbox, bg="#212120").place(x=500,y=20)
Label(frame,image=secondbox, bg="#212120").place(x=600,y=20)
Label(frame,image=secondbox, bg="#212120").place(x=700,y=20)
Label(frame,image=secondbox, bg="#212120").place(x=800,y=20)


#Clock

clock=Label(root,font=("Helvetica",30,"bold"),fg="white",bg="#57adff")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)


#thpwd  

t = Label(root,font=("Helvetica",10),fg="white",bg="#203243")
t.place(x=150,y=120) 

h = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=150,y=140) 

p = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=150,y=160) 

w = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=150,y=180) 

d = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=150,y=200) 

#Firstcell

firstFrame= Frame(root,width=230,height=132,bg="#282829")
firstFrame.place(x=35,y=315)

day1= Label(firstFrame,font=("Helvetica",20),fg="#fff",bg="#282829")
day1.place(x=100,y=5)

firstImage= Label(firstFrame,bg="#282829")
firstImage.place(x=1,y=15)

day1temp=Label(firstFrame,bg="#282829",fg="#07adff",font="arial 15 bold")
day1temp.place(x=100,y=50)


#secondCell

secondFrame= Frame(root,width=70,height=115,bg="#282829")
secondFrame.place(x=305,y=315)

day2= Label(secondFrame,fg="#fff",bg="#282829")
day2.place(x=10,y=5)

secondImage= Label(secondFrame,bg="#282829")
secondImage.place(x=7,y=20)

day2temp=Label(secondFrame,bg="#282829",fg="#07adff",font="arial 15 bold")
day2temp.place(x=10,y=70)

#ThirdCell

thirdFrame= Frame(root,width=70,height=115,bg="#282829")
thirdFrame.place(x=405,y=315)

day3= Label(thirdFrame,fg="#fff",bg="#282829")
day3.place(x=10,y=5)

thirdImage= Label(thirdFrame,bg="#282829")
thirdImage.place(x=7,y=20)

day3temp=Label(thirdFrame,bg="#282829",fg="#07adff",font="arial 15 bold")
day3temp.place(x=10,y=70)


#FourthCell

fourthFrame= Frame(root,width=70,height=115,bg="#282829")
fourthFrame.place(x=505,y=315)

day4= Label(fourthFrame,fg="#fff",bg="#282829")
day4.place(x=10,y=5)

fourImage= Label(fourthFrame,bg="#282829")
fourImage.place(x=7,y=20)

day4temp=Label(fourthFrame,bg="#282829",fg="#07adff",font="arial 15 bold")
day4temp.place(x=10,y=70)

#FifthCell

fifthFrame= Frame(root,width=70,height=115,bg="#282829")
fifthFrame.place(x=605,y=315)

day5= Label(fifthFrame,fg="#fff",bg="#282829")
day5.place(x=10,y=5)

fiveImage= Label(fifthFrame,bg="#282829")
fiveImage.place(x=7,y=20)

day5temp=Label(fifthFrame,bg="#282829",fg="#07adff",font="arial 15 bold")
day5temp.place(x=10,y=70)


#sixthCell

sixthFrame= Frame(root,width=70,height=115,bg="#282829")
sixthFrame.place(x=705,y=315)

day6= Label(sixthFrame,fg="#fff",bg="#282829")
day6.place(x=10,y=5)

sixthImage= Label(sixthFrame,bg="#282829")
sixthImage.place(x=7,y=20)
day6temp=Label(sixthFrame,bg="#282829",fg="#07adff",font="arial 15 bold")
day6temp.place(x=10,y=70)

#sevenCell

sevenFrame= Frame(root,width=70,height=115,bg="#282829")
sevenFrame.place(x=805,y=315)

day7= Label(sevenFrame,fg="#fff",bg="#282829")
day7.place(x=10,y=5)

sevenImage= Label(sevenFrame,bg="#282829")
sevenImage.place(x=7,y=20)
day7temp=Label(sevenFrame,bg="#282829",fg="#07adff",font="arial 15 bold")
day7temp.place(x=10,y=70)


#SecondCell


root.mainloop() 

