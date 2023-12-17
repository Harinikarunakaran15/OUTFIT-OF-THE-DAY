from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import webbrowser

root=Tk()
root.title("Weather")
root.geometry("1360x1000")
root['bg'] = '#953553'

Heading=LabelFrame(root,bd=2,relief="groove",bg='white')
Heading.place(x=0,y=0,width=1380,height=100)
Wind_image=PhotoImage(file="cloud.png")
name=Label(Heading,text="Weather App",font="arial 40 bold italic",fg="black",bg='white').grid(row=0,column=1,padx=50,pady=15)
Suggestion_frame=LabelFrame(root,bd=2,relief="groove",text="Suggestion",font="arial 16 bold",fg="black",bg='white')
Suggestion_frame.place(x=850,y=100,width=500,height=470)

def getWeather():
    try:
        city=textfield.get()

        geolocator=Nominatim(user_agent="GetLoc")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        print(result)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT TIME")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=c2c68eb037b158dd0ef5cede8ed07758"
        
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

                
    except Exception as e:
        messagebox.showerror('Error','Invalid Entry!!!')

def HideAllFrames():
    for widget in Suggestion_frame.winfo_children():
        widget.destroy()

def get_suggestion():
        city=textfield.get()

        geolocator=Nominatim(user_agent="GetLoc")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        print(result)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT TIME")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=c2c68eb037b158dd0ef5cede8ed07758"
        
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)


        def suggest_clothing(temp):
                HideAllFrames()
                if temp > 25:
                        e = Label(Suggestion_frame, fg = 'black',bg='white', font=("arial",9,"bold"),text= "1.Clothing:\n* Loose-fitting, lightweight cotton or linen shirt:Opt for a light-colored shirt with\n short sleeves or roll up the sleeves for better airflow.\n* Linen or cotton shorts: Choose comfortable and breathable shorts that allow \nfor easy movement and ventilation.\n* Flowy sundress (for women): A loose- fitting sundress made of lightweight fabric\n like cotton or linen would beideal.")
                        e.grid(row = 1, column = 1)
                        
                elif temp > 15:
                        q = Label(Suggestion_frame, fg = 'black',bg='white', font=("arial",9,"bold"),text = "1.Clothing:\n*Light jackets or cardigans: Spring can have fluctuating temperatures,\n so having a lightweight jacket or cardigan is essential \n* T-shirts and blouses: Opt for breathable and comfortable tops in pastel or\n floral prints.\n* Jeans and lightweight pants: You can still wear jeans, but consider lighter \n materials like cotton or linen.\n* Dresses and skirts: Flowy, floral dresses and skirts are perfect for springtime.")
                        q.grid(row = 1, column = 1)
                               
                elif temp > 5:
                        w = Label(Suggestion_frame, fg = 'black',bg='white', font=("arial",9,"bold"),text = "1.Clothing:\n* Top: A classic peacoat in a neutral color like navy or black for both \nmen and women. Peacoats are warm and timeless.\n* Bottoms (Women): Dark wash skinny jeans or tailored trousers \n* Bottoms (Men): Slim-fit charcoal gray dress pants.")
                        w.grid(row = 1, column = 1)
                        
        b0 = Button(text='outfit',command=suggest_clothing(temp))
        b0.place(x=20000,y=10000)
Outfit_icon=PhotoImage(file="clothe_pgn.png")
myimage_icon=Button(image=Outfit_icon,borderwidth=0,bg='white',cursor="hand2",command=get_suggestion)
myimage_icon.place(x=880,y=25)

def get_suggestion1():
        city=textfield.get()

        geolocator=Nominatim(user_agent="GetLoc")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        print(result)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT TIME")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=c2c68eb037b158dd0ef5cede8ed07758"
        
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

        def suggest_footware(temp):
                HideAllFrames()
                if temp > 25:
                        e = Label(Suggestion_frame, fg = 'black', font=("arial",9,"bold"),text= "2.Footwear:\n* Open-toe sandals: Choosecomfortable sandals with breathablematerials that allow\n your feet tobreathe and stay cool.\n* Flip-flops orstrappy sandals are good options.")
                        e.grid(row = 1, column = 1)
                elif temp > 15:
                        q = Label(Suggestion_frame, fg = 'black', font=("arial",9,"bold"),text = "2.Footwear:\n*Sneakers: Comfortable sneakers are versatile and great for walking outdoors.\n*Loafers: These are a stylish choice for both men and women in spring.\n*Rain boots: Spring can be rainy, so waterproof boots are a smart addition.\n*Sandals: As the weather warms up, open-toed sandals are great for casual outings.")
                        q.grid(row = 1, column = 1)
                elif temp > 5:
                        w = Label(Suggestion_frame, fg = 'black', font=("arial",9,"bold"),text = "2.Footwear:\n* Leather lace-up boots for both men and women. \n* Choose a waterproof option if there's a chance of rain or snow.")
                        w.grid(row = 1, column = 1)
        b0 = Button(text='outfit',command=suggest_footware(temp))
        b0.place(x=10000,y=10000)
Outfit_icon1=PhotoImage(file="footwear_pgn.png")
myimage_icon=Button(image=Outfit_icon1,borderwidth=0,bg='white',cursor="hand2",command=get_suggestion1)
myimage_icon.place(x=980,y=20)

def get_suggestion2():
        city=textfield.get()

        geolocator=Nominatim(user_agent="GetLoc")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        print(result)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT TIME")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=c2c68eb037b158dd0ef5cede8ed07758"
        
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

        def suggest_accessories(temp):
                HideAllFrames()
                if temp > 25:
                        e = Label(Suggestion_frame, fg = 'black', font=("arial",9,"bold"),text= "3.Accessories:\n* Sunglasses: Protect your eyes fromthe sun with a stylish pair of sunglasses.\n* Hat or cap: Wear a wide-brimmed hator a cap to shield your face from direct sunlight.\n* Light scarf (for women): A thin, breathable scarf can add style while providing some\n protection from the sun.")
                        e.grid(row = 1, column = 1)
                elif temp > 15:
                        q = Label(Suggestion_frame, fg = 'black', font=("arial",9,"bold"),text = "3.Accessories:\n*Sunglasses: Protect your eyes from the bright spring sun.\n*Scarves: Light scarves can add style and warmth to your outfit.\n*Umbrella: Be prepared for unexpected showers with a compact umbrella.")
                        q.grid(row = 1, column = 1)
                elif temp > 5:
                        w = Label(Suggestion_frame, fg = 'black', font=("arial",9,"bold"),text = "3.Accessories:\n*Scarf: A matching scarf in a complementary color to the coat\n for both men and women. Wool or cashmere for added warmth.\n* Hat: A stylish beanie or fedora for women and a classic wool beanie for men.\n* Gloves: Leather or suede gloves that match the boots for both men and women.\n* Socks: Wool-blend or thermal socks for added warmth.")
                        w.grid(row = 1, column = 1)
        b0 = Button(text='outfit',command=suggest_accessories(temp))
        b0.place(x=10000,y=10000)
Outfit_icon2=PhotoImage(file="accessories_pgn.png")
myimage_icon=Button(image=Outfit_icon2,borderwidth=0,bg='white',cursor="hand2",command=get_suggestion2)
myimage_icon.place(x=1080,y=20)

def get_suggestion3():
        city=textfield.get()

        geolocator=Nominatim(user_agent="GetLoc")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        print(result)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT TIME")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=c2c68eb037b158dd0ef5cede8ed07758"
        
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

        def suggest_tips(temp):
                HideAllFrames()
                if temp > 25:
                        e = Label(Suggestion_frame, fg = 'black', font=("arial",9,"bold"),text= "4.Additional Tips:\n* Apply sunscreen: Regardless of your outfit, it's crucial to protect your exposed\n skin with sunscreen to avoidsunburn.\n* Stay hydrated: Carry a water bottle with you to stay hydrated throughout the day.")
                        e.grid(row = 1, column = 1)
                elif temp > 15:
                        q = Label(Suggestion_frame, fg = 'black', font=("arial",9,"bold"),text = "4.Addition Tips:\n*Layer your clothing for variable temperatures.\n*Embrace pastel and floral patterns.\n*Consider adding a pop of color to your outfit..")
                        q.grid(row = 1, column = 1)
                elif temp > 5:
                        w = Label(Suggestion_frame, fg = 'black', font=("arial",9,"bold"),text = "4.Additional Tips:\n*Layering: Underneath the coat, both men and women can wear a lightweight,\n moisture-wicking base layer to trap heat and stay comfortable.\n* Stay Warm: Layering is key in cooler temperatures. Women can add a turtleneck\n or lightweight sweater under their coat, while men can wear a \ndress shirt and sweater combination.")
                        w.grid(row = 1, column = 1)
        b0 = Button(text='outfit',command=suggest_tips(temp))
        b0.place(x=10000,y=10000)
Outfit_icon3=PhotoImage(file="tips_pgn.png")
myimage_icon=Button(image=Outfit_icon3,borderwidth=0,bg='white',cursor="hand2",command=get_suggestion3)
myimage_icon.place(x=1180,y=20)

#search box
Search_image=PhotoImage(file="search_pgn.png")
myimage=Label(Heading,image=Search_image,bg='white')
myimage.place(x=400,y=8)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"))
textfield.place(x=450,y=28)
textfield.focus()

#search logo
Search_icon=PhotoImage(file="search.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=780,y=22)

#logo
Logo_image=PhotoImage(file="logo_pgn.png")
logo=Label(image=Logo_image,bg='#953553')
logo.place(x=150,y=100)

#Bottom box
'''Frame_image=PhotoImage(file="box_pgn.png")
frame_myimage=Label(image=Frame_image,bg='#953553',fg='#953553')
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)
frame_myimage.place(x=50,y=615)'''

#icon
wind=Label(image=Wind_image,bg='#953553')
wind.place(x=650,y=200)
Hum_image=PhotoImage(file="drop.png")
hum=Label(image=Hum_image,bg='#953553')
hum.place(x=510,y=455)
Des_image=PhotoImage(file="policy.png")
des=Label(image=Des_image,bg='#953553')
des.place(x=200,y=510)
Press_image=PhotoImage(file="pressure.png")
press=Label(image=Press_image,bg='#953553')
press.place(x=15,y=315)

#time
name=Label(root,font=("arial",15,"bold"), fg='#ffffff',bg='#953553')
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20), fg='#ffffff',bg='#953553')
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#953553")
label1.place(x=690,y=315)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#953553")
label2.place(x=530,y=595)

label1=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#953553")
label1.place(x=190,y=650)

label1=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#953553")
label1.place(x=25,y=455)

t=Label(font=("arial",70,"bold"),fg="#ee666d",bg='#953553')
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'), fg='#ffffff', bg='#953553')
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#953553")
w.place(x=690,y=340)
h=Label(text="...",font=("arial",20,"bold"),bg="#953553")
h.place(x=530,y=620)
d=Label(text="...",font=("arial",20,"bold"),bg="#953553")
d.place(x=190,y=675)
p=Label(text="...",font=("arial",20,"bold"),bg="#953553")
p.place(x=25,y=480)

def Amazon():
    webbrowser.open("www.amazon.in")


Amazon_icon=PhotoImage(file="amazon.png")
amazon=Button(image=Amazon_icon,borderwidth=0,bg='#953553',cursor="hand2",command=Amazon)
amazon.place(x=880,y=570)    

def Flipkart():
    webbrowser.open("www.flipkart.com")


Flip_icon=PhotoImage(file="flipkart.png")
flip=Button(image=Flip_icon,borderwidth=0,bg='#953553',cursor="hand2",command=Amazon)
flip.place(x=1050,y=570)    



root.mainloop()
