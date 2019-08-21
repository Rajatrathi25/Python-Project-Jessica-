import pyttsx3
# pyttsx3 is used to bring the computer available voices 
import datetime
# THIS IS A module to import date and time 
import speech_recognition as sr 
# This is to take commands from user 
#import pyaudio
import wikipedia
import webbrowser
import os
import random
from news import *



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[2].id) # to check the voices 
engine.setProperty('voice',voices[2].id) # this sets the voice type 

sites= {

    'google':'https://www.google.com/',
    'facebook':'https://www.facebook.com/',
    'netflix':'https://www.netflix.com/',
    'hotstar':'https://www.hotstar.com/',
    'gmail':'https://www.gmail.com/',
    'stackoverflow':'https://www.stackoverflow.com/',
    'twitter':'https://www.twitter.com/',
    'youtube':'https://www.youtube.com/',
    'amazon':'https://www.amazon.in/',
    'flipkart':'https://www.flipkart.com/'
}

folders={
    'downloads':'C:\\Users\\LENOVO\\Downloads',
    'photos':'C:\\Users\\LENOVO\\Pictures',
    'desktop':'C:\\Users\\LENOVO\\Desktop'
}

# dict_news={
#     'techincal news':tech('techno4logy'),
#     'sports news':sports('sports'),
#     'movies news':movies('movies'),
#     'trending news' :trending('trending')

# }
greetings={
    'hola':'hola',
    'salut':'salut',        
    'Zdravstvuyte':'Zdravstvuyte' ,
    'Nǐn hǎo':'Nǐn hǎo',
    'Salve':'Salve',
    'Guten Tag':'Guten Tag',
    'Olá':'Olá',
    'Namaste':'Namaste',
    'hello':'hello',
    'knock knock':'yes'
}

regards={
    'welcome':'pleasure ',
    'thank you':'welcome',
    'bye-bye':'bye-bye',
    'bye':'bye',
    'by':'bye',
    'Au Revoir':'Au Revoir',
    'Sayōnara':'Sayōnara',
    'Adios':'Adios',
    'Do svidaniya':'Do svidaniya'
}
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning ')
    elif hour>=12 and hour<18:
        speak('Gud afternoon')
    else :
        speak('Good Evening ')
    speak('Hey,I am jessica . How may i help you ? ')

def close():
    #Flag =False
    exit(0)

def takeCommand():
    '''
    it takes input from user and return string output

    '''
    r= sr.Recognizer() # recognizer is class to recognize the input
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        r.non_speaking_duration=0.2
        audio=r.listen(source)
        try:
            print('Recognizing..')
            query = r.recognize_google(audio,language="en-IN") # error for Unknown value and Request error are occuring and are not handeld by exception class
            #print('user said',query)
    #recognize_google will reconginze our audio 
        except sr.UnknownValueError: 
            print("Sorry I could not understand audio") 
            speak('Sorry I could not understand audio')
            close()
      
        except sr.RequestError: 
            #print("Could not request results from Google  Speech Recognition service. ")
            print('Check your internet Connection. Please')
            speak('Check your internet Connection. Please')
            close()


        except Exception :
            print('Say that again please ')
            return "None"
            exit(0)
        return query


def main_function():
    wishme()
    while True:
        query=takeCommand().lower()
        
    #logic which i want to execute task
        if 'open' in query:
            for key,value in sites.items():
                if key in query:  
                    webbrowser.open(value) 
                    close()

            for key,value in folders.items():
                if key in query:  
                    path=value
                    os.startfile(path) 
                    close()
        
        elif 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=1)
            speak("According to my research")
            print (results)
            speak (results)
            close()
        
        elif 'jessica' in query:
            for key,value in greetings.items():
                if key in query:  
                    speak(value)

            for key,value in regards.items():
                if key in query:  
                    speak(value)
                    close()


        elif 'play song' in query:
            speak("Please ! provide the Location of Song folder")
            music_dir=input('Folder Name ')
            music_dir.replace("\\","\\\\")
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,random.choice(songs)))
            close()

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak ("The time is ")
            speak(strTime)
            close()
        
        elif 'techincal news' in query:
            #Technical_News=
            tech('technology')
            #print(Technical_News)
            close()

        elif 'sports news' in query:
            sports('sports')
            close()
            
           
        elif 'movies news' in query:
            movies('movies')
            close()

        elif 'trending news' in query:
            trending('trending')
            close()
            
        # elif str(greetings.keys()) in query:
        #     for key,value in greetings.items():
        #         if key in query:  
        #             speak(value)        
        
        else:
            print('user said '+query)
            print("sorry i didn't get you")
            close()
            

# add google on any word entered 
main_function()