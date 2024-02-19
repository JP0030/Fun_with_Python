﻿# JP0030

import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

def getNotification():
    cityName=place.get() 
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?" 
    try:

        url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
        response = requests.get(complete_url) 
        x = response.json() 
        y = x["main"] 
 
        temp = y["temp"]

        pres = y["pressure"]

        hum = y["humidity"]

        z = x["weather"]

        weather_desc = z[0]["description"]

        info="Here is the eather description of "+ cityName+ ":"+" \nTemperature = " +str(temp) +"°C"+"\n atmospheric pressure = " + str(pres) + "hPa"+"\n humidity = " +str(hum) +"%"+"\n description of the weather= " + str(weather_desc)

      
        notification.notify(
                    title = "YOUR WEATHER REPORT",
                    message=info ,

                    timeout=2)

        time.sleep(7)
    
    except Exception as e:
        mb.showerror('Error',e)
        
wn = Tk()
wn.title("PythonGeeks Weather Desktop Notifier")
wn.geometry('700x200')
wn.config(bg='azure')

Label(wn, text="PythonGeeks Weather Desktop Notifier", font=('Courier', 15), fg='grey19',bg='azure').place(x=100,y=15)

Label(wn, text='Enter the Location:', font=("Courier", 13),bg='azure').place(relx=0.05, rely=0.3)

