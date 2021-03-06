from tkinter import *
import locale
import threading
import time
import requests
import json
import traceback
import feedparser

#import RPi.GPIO as GPIO

import datetime
import iso8601
import rfc3339

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from PIL import Image, ImageTk
from contextlib import contextmanager

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
LOCALE_LOCK = threading.Lock()

with open('./credentials.json') as data:
    cred = json.load(data)
    weather_api_token = cred['weather_token']
    ip_token = cred['ip_token']
    xlarge_text_size = cred['xlarge_text_size']
    large_text_size = cred['large_text_size']
    medium_text_size = cred['medium_text_size']
    small_text_size = cred['small_text_size']
    smaller_text_size = cred['smaller_text_size']
    smallish_text_size = cred['smallish_text_size']

ui_locale = ''
time_format = 12 
date_format = "%b %d, %Y"
news_country_code = 'us'

weather_lang = 'en' 
weather_unit = 'us'
latitude = None 
longitude = None 


@contextmanager
def setlocale(name): #thread proof function to work with locale
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)

icon_lookup = {
    'clear-day': "assets/Sun.png",                  # clear sky day
    'wind': "assets/Wind.png",                      #wind
    'cloudy': "assets/Cloud.png",                   # cloudy day
    'partly-cloudy-day': "assets/PartlySunny.png",  # partly cloudy day
    'rain': "assets/Rain.png",                      # rain day
    'snow': "assets/Snow.png",                      # snow day
    'snow-thin': "assets/Snow.png",                 # sleet day
    'fog': "assets/Haze.png",                       # fog day
    'clear-night': "assets/Moon.png",               # clear sky night
    'partly-cloudy-night': "assets/PartlyMoon.png", # scattered clouds night
    'thunderstorm': "assets/Storm.png",             # thunderstorm
    'tornado': "assests/Tornado.png",               # tornado
    'hail': "assests/Hail.png"                      # hail
}


class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        # initialize time label
        self.time1 = ''
        self.timeLbl = Label(self, font=('Helvetica', large_text_size), fg="white", bg="black")
        self.timeLbl.pack(side=TOP, anchor=E)
        # initialize day of week
        self.day_of_week1 = ''
        self.dayOWLbl = Label(self, text=self.day_of_week1, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.dayOWLbl.pack(side=TOP, anchor=E)
        # initialize date label
        self.date1 = ''
        self.dateLbl = Label(self, text=self.date1, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.dateLbl.pack(side=TOP, anchor=E)
        self.tick()

    def tick(self):
        with setlocale(ui_locale):
            if time_format == 12:
                time2 = time.strftime('%I:%M %p') #hour in 12h format
            else:
                time2 = time.strftime('%H:%M') #hour in 24h format

            day_of_week2 = time.strftime('%A')
            date2 = time.strftime(date_format)
            # if time string has changed, update it
            if time2 != self.time1:
                self.time1 = time2
                self.timeLbl.config(text=time2)
            if day_of_week2 != self.day_of_week1:
                self.day_of_week1 = day_of_week2
                self.dayOWLbl.config(text=day_of_week2)
            if date2 != self.date1:
                self.date1 = date2
                self.dateLbl.config(text=date2)
            self.timeLbl.after(200, self.tick)


class Weather(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.temperature = ''
        self.forecast = ''
        self.location = ''
        self.currently = ''
        self.icon = ''
        self.degreeFrm = Frame(self, bg="black")
        self.degreeFrm.pack(side=TOP, anchor=W)
        self.temperatureLbl = Label(self.degreeFrm, font=('Helvetica', xlarge_text_size), fg="white", bg="black")
        self.temperatureLbl.pack(side=LEFT, anchor=N)
        self.iconLbl = Label(self.degreeFrm, bg="black")
        self.iconLbl.pack(side=LEFT, anchor=N, padx=20)
        self.currentlyLbl = Label(self, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.currentlyLbl.pack(side=TOP, anchor=W)
        self.forecastLbl = Label(self, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.forecastLbl.pack(side=TOP, anchor=W)
        self.locationLbl = Label(self, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.locationLbl.pack(side=TOP, anchor=W)
        self.get_weather()

    def get_ip(self):
        try:
            ip_url = "https://api.ipify.org/?format=json"
            req = requests.get(ip_url)
            ip_json = json.loads(req.text)
            return ip_json['ip']
        except Exception as e:
            traceback.print_exc()
            return "Error: %s. Cannot get ip." % e

    def get_weather(self):
        try:

            if latitude is None and longitude is None:
                location_req_url = "http://api.ipstack.com/%s?access_key=%s&format=1" % (self.get_ip(),ip_token)
                r = requests.get(location_req_url)
                location_obj = json.loads(r.text)

                lat = location_obj['latitude']
                lon = location_obj['longitude']

                location2 = "%s, %s" % (location_obj['city'], location_obj['region_code'])

                # get weather
                weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s?lang=%s&units=%s" % (weather_api_token, lat,lon,weather_lang,weather_unit)
            else:
                location2 = ""
                # get weather
                weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s?lang=%s&units=%s" % (weather_api_token, latitude, longitude, weather_lang, weather_unit)

            r = requests.get(weather_req_url)
            weather_obj = json.loads(r.text)

            degree_sign= u'\N{DEGREE SIGN}'
            temperature2 = "%s%s" % (str(int(weather_obj['currently']['temperature'])), degree_sign)
            currently2 = weather_obj['currently']['summary']
            forecast2 = weather_obj["hourly"]["summary"]

            icon_id = weather_obj['currently']['icon']
            icon2 = None

            if icon_id in icon_lookup:
                icon2 = icon_lookup[icon_id]

            if icon2 is not None:
                if self.icon != icon2:
                    self.icon = icon2
                    image = Image.open(icon2)
                    image = image.resize((100, 100), Image.ANTIALIAS)
                    image = image.convert('RGB')
                    photo = ImageTk.PhotoImage(image)

                    self.iconLbl.config(image=photo)
                    self.iconLbl.image = photo
            else:
                # remove image
                self.iconLbl.config(image='')

            if self.currently != currently2:
                self.currently = currently2
                self.currentlyLbl.config(text=currently2)
            if self.forecast != forecast2:
                self.forecast = forecast2
                self.forecastLbl.config(text=forecast2)
            if self.temperature != temperature2:
                self.temperature = temperature2
                self.temperatureLbl.config(text=temperature2)
            if self.location != location2:
                if location2 == ", ":
                    self.location = "Cannot Pinpoint Location"
                    self.locationLbl.config(text="Cannot Pinpoint Location")
                else:
                    self.location = location2
                    self.locationLbl.config(text=location2)
        except Exception as e:
            traceback.print_exc()
            print('Error: %s. Cannot get weather.' %e)

        self.after(600000, self.get_weather)

    @staticmethod
    def convert_kelvin_to_fahrenheit(kelvin_temp):
        return 1.8 * (kelvin_temp - 273) + 32


class News(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'News' # 'News' is more internationally generic
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg="black")
        self.headlinesContainer.pack(side=TOP)
        self.get_headlines()

    def get_headlines(self):
        try:
            # remove all children
            for widget in self.headlinesContainer.winfo_children():
                widget.destroy()
            if news_country_code == None:
                headlines_url = "https://news.google.com/news?ned=us&output=rss"
            else:
                headlines_url = "https://news.google.com/news?ned=%s&output=rss" % news_country_code

            feed = feedparser.parse(headlines_url)

            for post in feed.entries[0:5]:
                headline = NewsHeadline(self.headlinesContainer, post.title)
                headline.pack(side=TOP, anchor=W)
        except Exception as e:
            traceback.print_exc()
            print ("Error: %s. Cannot get news." % e)

        self.after(600000, self.get_headlines)


class NewsHeadline(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg='black')

        image = Image.open("assets/Newspaper.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)

        self.iconLbl = Label(self, bg='black', image=photo)
        self.iconLbl.image = photo
        self.iconLbl.pack(side=LEFT, anchor=N)

        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, width=50, anchor = W, font=('Helvetica', smallish_text_size), fg="white", bg="black")
        self.eventNameLbl.pack(side=LEFT, anchor=N)


class Calendar(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.title = 'Next 5 Events'
        self.calendarLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.calendarLbl.pack(side=TOP, anchor=W)
        self.calendarEventContainer = Frame(self, bg='black')
        self.calendarEventContainer.pack(side=TOP, anchor=E)
        self.get_events()

    def get_events(self):
        for widget in self.calendarEventContainer.winfo_children():
            widget.destroy()

        creds = None
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        week = (datetime.datetime.utcnow() + datetime.timedelta(days=7)).isoformat() + 'Z'
        events_result = service.events().list(calendarId='primary', timeMin=now, timeMax=week,
                                            maxResults=5, singleEvents=True,
                                            orderBy='startTime').execute()

        events = events_result.get('items', [])

        for event in events:
            calEvent = CalendarEvent(self.calendarEventContainer, event)
            calEvent.pack(side=TOP, anchor=W,pady = 3)

        self.after(1000*60*30, self.get_events) #Get Events every half hour



class CalendarEvent(Frame):
    def __init__(self, parent, event):
        Frame.__init__(self, parent, bg='black')

        weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        summary = event['summary']
        day = ''

        try:
            description = event['description']#.replace('\n','; ')
        except:
            description = 'No Description'

        if len(summary) > 30:
            summary = summary[:30]
        while len(summary)<80:
            summary = summary+'.'
        try:
            date = iso8601.parse_date(event['start']['dateTime'])
            start= str(date.time().strftime("%I:%M %p"))
            day = weekdays[date.weekday()]
            if start[0] == '0':
                start = start[1:]
            start='@ '+start
        except:
            try:
                
                start = event['start']['date']
                time = datetime.datetime.strptime(start,"%Y-%m-%d").weekday()
                start = 'All day '+str(weekdays[time])
            except:
                start = 'Time Unknown'
        
        try:
            end = iso8601.parse_date(event['end']['dateTime']).time().strftime("%I:%M %p")
            end= str(end)
            if end[0] == '0':
                end = end[1:]
        except:
            try:
                
                end = event['end']['date']
                time = datetime.datetime.strptime(end,"%Y-%m-%d").weekday()
                end = str(weekdays[time])
            except:
                end = 'Time Unknown'

        image = Image.open("assets/calendar.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)

        self.iconLbl = Label(self, bg='black', image=photo)
        self.iconLbl.image = photo
        self.iconLbl.grid(row=0,column=0)

        self.eventNameLbl = Label(self, text=summary, anchor = W,width = 35,
                                        font=('Helvetica', smaller_text_size), fg="white", bg="black")
        self.eventNameLbl.grid(row=0,column=1)

        self.eventTime = Label(self, text=start+' -- '+end+', '+day, font=('Helvetica', smaller_text_size), fg="white", bg="black")
        self.eventTime.grid(row=0,column=2)

        self.eventDesc = Label(self, text=description,justify=RIGHT,anchor = E,width = 20,font=('Helvetica', smaller_text_size), fg="white", bg="black")
        self.eventDesc.grid(row=1,column=2)
        


class FullscreenWindow:

    def __init__(self):
        self.showNews = False
        self.tk = Tk()
        self.tk.configure(background='black')
        self.topFrame = Frame(self.tk, background = 'black')
        self.bottomFrame = Frame(self.tk, background = 'black')
        self.topFrame.pack(side = TOP, fill=BOTH, expand = YES)
        self.bottomFrame.pack(side = BOTTOM, fill=BOTH, expand = YES)
        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        self.tk.bind("<Tab>",self.toggle_news)
        # clock
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=RIGHT, anchor=N, padx=100, pady=60)
        # weather
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=LEFT, anchor=N, padx=100, pady=60)
        # news
        self.news = News(self.bottomFrame)
        # calender
        self.calendar = Calendar(self.bottomFrame)
        self.calendar.pack(side=LEFT, anchor=S, padx=50, pady=30)
        #self.check()

    def toggle_news(self, event=None):
        self.showNews = not self.showNews
        
        if self.showNews:
            self.news.pack(side=LEFT, anchor=S, padx=50, pady=60)
            self.calendar.pack_forget()
        else:
            self.news.pack_forget()
            self.calendar.pack(side=LEFT, anchor=S, padx=50, pady=30)
        return "break"

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
    
    #def check(self):
        #input_state = GPIO.input(18)
        #if not input_state:
            #self.toggle_news()
        #self.calendar.after(200, self.check)
    

if __name__ == '__main__':
    w = FullscreenWindow()
    w.tk.mainloop()
