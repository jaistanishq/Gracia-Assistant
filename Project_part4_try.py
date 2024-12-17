                                #Speech to Text Recognition
    
import speech_recognition as sr
from datetime import datetime
import webbrowser as wb
import os
import wikipedia
import pyjokes
import subprocess
import time
import pyautogui
import psutil
import winshell
import socket
import imdb
from GoogleNews import GoogleNews
import string
import random
from calendar import *
from tkinter import Tk, Label, Entry, Button
import Project_part5_try

def convert_speech_to_text():
    """Converts user speech to text using Google Speech Recognition."""

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        user_data = recognizer.recognize_google(audio)
        print("You said: " + user_data)
        return user_data
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def text_to_speech(text):
    """Converts text to speech using pyttsx3."""

    import pyttsx3
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # Adjust speech rate if desired
    engine.setProperty('rate', 'rate-70')

    # Ensure voice selection and availability
    voices = engine.getProperty('voices')
    if len(voices) > 1:  # Check for multiple voices
        engine.setProperty('voice', voices[1].id)  # Select the second voice (if available)
    else:
        print("Only one voice available. Using the default voice.")

    engine.say(text)
    engine.runAndWait()
    
def cpu():
    usage=str(psutil.cpu_percent())
    text_to_speech("CPU is at"+ usage)
    print("CPU is at",usage)
    return(usage)
    
def cpubattery():
    battery=str(psutil.sensors_battery())
    text_to_speech("Your "+ battery)
    print("Your ",battery)
    return(battery)

def movie_summary():
    moviesdb = imdb.IMDb()
    text_to_speech("Please tell me the movie name.")
    text = convert_speech_to_text()
    text_to_speech("Searching for " + text)
    movies = moviesdb.search_movie(text)
    try:
        if not movies:
            text_to_speech("No result found.")
        else:
            first_movie = movies[0]
            title = first_movie['title']
            year = first_movie.get('year', 'Unknown')  # Default to 'Unknown' if year is missing
            movie_details = moviesdb.get_movie(first_movie.movieID)
            rating = movie_details.get('rating', 'Not available')
            plot = movie_details.get('plot outline', 'No plot available')
            current_year = int(datetime.now().strftime("%Y"))
            if year != 'Unknown' and year < current_year:
                summary=(f"{title} was released in {year} and has an IMDb rating of {rating}. The plot summary is: {plot}.")
            elif year != 'Unknown' and year >= current_year:
                summary=(f"{title} will release in {year} and has an IMDb rating of {rating}. The plot summary is: {plot}.")
            else:
                summary=(f"{title} has no release year information. IMDb rating: {rating}. Plot: {plot}.")
        text_to_speech(summary)
        return summary
    
    except Exception as e:
        error_message = "An error occurred while fetching movie details."
        text_to_speech(error_message)
        print("Error:", e)
        return error_message

def get_news(news_limit=3):
    news = GoogleNews(period='1d')
    news.search("India")
    result = news.result()
    if not result:
        print("No news found.")
        return []
    limited_result = result[:news_limit]
    text_to_speech(f"Here are today's top {news_limit} news headlines for India:\n")
    for item in limited_result:
        title = item['title']
        date = item['date']
        link = item['link']
        print(f"Title: {title}")
        print(f"Date/Time: {date}")
        print(f"Link: {link}\n")
    return limited_result


def generate_password():
    char = string.ascii_letters + string.digits
    ret = ''.join(random.choice(char) for _ in range(8))
    return ret

def show_password():
    password = generate_password()
              
if 1<0:
    user_data = convert_speech_to_text().lower()
     
def handle_user_request(user_data):
    if user_data is None:  # Handle cases where speech recognition fails
         text_to_speech("Sorry, Unable to recognize your voice. Please try again.")
         return "Sorry, Unable to recognize your voice. Please try again."


    if "Hello" in user_data or "hello" in user_data or "Hii" in user_data or "hii" in user_data:
         current_time = datetime.now()
         if current_time.hour>=0 and current_time.hour<12:
             text_to_speech("Hii! ,Good morning mam!,How may I help you?")
             return "Hii! ,Good morning mam!,How may I help you?"
         elif current_time.hour>=12 and current_time.hour<16:
             text_to_speech("Hii! ,Good Afternoon mam!,How may I help you?")
             return "Hii! ,Good Afternoon mam!,How may I help you?"
         elif current_time.hour>=16 and current_time.hour<20:
             text_to_speech("Hii! ,Good Evening mam!,How may I help you?")
             return "Hii! ,Good Evening mam!,How may I help you?"
         else:
             text_to_speech("Hii!, How may I help you")
             return "Hii!, How may I help you"
         
    elif "what is your name" in user_data or "What is your name" in user_data:
         text_to_speech("My name is Gracia AI Assistant")
         return "My name is Gracia AI Assistant"

    elif "good morning" in user_data or "good afternoon" in user_data or "good evening" in user_data or "Good morning" in user_data or "Good afternoon" in user_data or "Good evening" in user_data :
         current_time = datetime.now()
         if current_time.hour>=0 and current_time.hour<12:
             text_to_speech("Good morning mam!,How may I assist you?")
             return "Good morning mam!,How may I assist you?"
         elif current_time.hour>=12 and current_time.hour<16:
             text_to_speech("Good Afternoon mam!,How may I assist you?")
             return "Good Afternoon mam!,How may I assist you?"
         elif current_time.hour>=16 and current_time.hour<20:
             text_to_speech("Good Evening mam!,How may I assist you?")
             return "Good Evening mam!,How may I assist you?"
         else:
             text_to_speech("Good Night mam!,Have pleasant dreams")
             return "Good Night mam!,Have pleasant dreams"
         
    elif "How are you" in user_data or "how are you" in user_data:
        text_to_speech("I am fine! & you?")
        return "I am fine! & you?"
    
    elif "Happy" in user_data or "happy" in user_data:
        text_to_speech("Nice to hear, Keep smile forever")
        return "Nice to hear, Keep smile forever"
    
    elif "Fine" in user_data or "fine" in user_data:
        text_to_speech("Nice!, Feel free to ask me if you need something")
        return "Nice!, Feel free to ask me if you need something"
    
    elif "Not well" in user_data or "not well" in user_data or "Not ok" in user_data or "not ok" in user_data or "Sad" in user_data or "sad" in user_data:
        text_to_speech("Sorry to hear that you're not feeling fine. But don't worry Time heals everything ")
        return "Sorry to hear that you're not feeling fine. But don't worry Time heals everything"
            
    elif "Who I am" in user_data or "who I am" in user_data or "who i am" in user_data:
        text_to_speech("If you can talk then surely you are aa human.")
        return "If you can talk then surely you are a human."
    
    elif "Thank you" in user_data or "thank you" in user_data:
        text_to_speech("You're welcome")
        return "You're welcome"
            
    elif "time now" in user_data or "the time" in user_data or "Time now" in user_data:
         current_time = datetime.now()
         time_string = f"It is {current_time.hour}:{current_time.minute}"  # Simplified time formatting
         text_to_speech(time_string)
         print(time_string)
         return (time_string)
     
    elif "Weather" in user_data or "weather" in user_data:
        ans = Project_part5_try.weather()
        weather_string = f"It is {ans}"
        text_to_speech(weather_string)
        print(weather_string)
        return (weather_string)
    
    elif  'Wikipedia' in user_data or "wikipedia" in user_data:
             text_to_speech('Searching Wikipedia...')
             user_data = user_data.replace("wikipedia","")
             results = wikipedia.summary(user_data,sentences=2)
             text_to_speech("According to Wikipedia")
             print(results)
             text_to_speech(results)
             return("According to Wikipedia ,"+ results)
         
    elif "Open free encyclopaedia" in user_data or "Encyclopaedia" in user_data or "encyclopaedia" in user_data or "open free encyclopaedia" in user_data or "Open free Encyclopaedia" in user_data or "open free Encyclopaedia" in user_data:
           wb.open("https://www.wikipedia.org")
           text_to_speech("The Free Encyclopaedia-Wikipedia is now ready for you")
           return "The Free Encyclopaedia-Wikipedia is now ready for you"
            

    elif "Play music" in user_data or "play music" in user_data:
         wb.open("https://gaana.com/")
         text_to_speech("gaana.com is now ready for you")
         return "gaana.com is now ready for you"

    elif "Open Google" in user_data or "open google" in user_data or "open Google" in user_data or "Open google" in user_data:
         wb.open('https://www.google.com')
         text_to_speech("google.com is now ready for you")
         return "google.com is now ready for you"
        
    elif "Open YouTube" in user_data or "open youtube" in user_data or "open YouTube" in user_data or "Open youtube" in user_data:
         wb.open('https://www.youtube.com')
         text_to_speech("youtube.com is now ready for you")
         return "youtube.com is now ready for you"
    
    elif "Open code" in user_data or "open code" in user_data:
             codePath = "D:\\Microsoft VS Code\\Code.exe"
             os.startfile(codePath)
             text_to_speech("visual studio code is now ready for you")
             return "visual studio code is now ready for you"
         
    elif "Open PowerPoint" in user_data or "open powerpoint" in user_data or "open PowerPoint" in user_data or "Open powerpoint" in user_data:
             codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
             os.startfile(codePath)
             text_to_speech("PowerPoint is now ready for you")
             return "PowerPoint is now ready for you"
         
    elif "Open Excel" in user_data or "open excel" in user_data or "Open excel" in user_data or "open Excel" in user_data:
             codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
             os.startfile(codePath)
             text_to_speech("Excel is now ready for you")
             return "Excel is now ready for you"
         
    elif "open Notepad" in user_data or "Open notepad" in user_data or "open notepad" in user_data or "Open Notepad" in user_data: 
             nPath = "D:\\Gracia_Assistant.txt"
             os.startfile(nPath)
             text_to_speech("Notepad is now ready for you")
             return "Notepad is now ready for you"
             
    elif "Open Moodle" in user_data or "open moodle" in user_data or "Open moodle" in user_data or "open Moodle" in user_data:
         wb.open('https://cet.iitp.ac.in/moodle/login/index.php')
         text_to_speech("Moodle is now ready for you, It's time to attend the classes.")
         return "Moodle is now ready for you, It's time to attend the classes."
             
    elif "Open Amazon" in user_data or "open amazon" in user_data or "Open amazon" in user_data or "open Amazon" in user_data:
         wb.open('https://www.amazon.in')
         text_to_speech("Amazon is now ready for you, It's time to shop.")
         return "Amazon is now ready for you, It's time to shop."     
     
    elif "Open Flipkart" in user_data or "open flipkart" in user_data or "Open flipkart" in user_data or "open Flipkart" in user_data:
         wb.open('https://www.flipkart.com')
         text_to_speech("Flipkart is now ready for you, It's time to shop.")
         return "Flipkart is now ready for you, It's time to shop."
     
    elif "where is" in user_data or "Where is" in user_data:
         user_data=user_data.replace("where is","")
         location=user_data
         text_to_speech("Locating...")
         text_to_speech(location)
         wb.open("https://www.google.co.in/maps/place/"+location+"")

    elif "write a note" in user_data:
        text_to_speech("What should I write?")
        note = convert_speech_to_text()

        if note is None:
            text_to_speech("I couldn't hear what you said. Please try again.")
        else:
            text_to_speech("Should I include date and time as well?")
            sn = convert_speech_to_text()

            if sn is None:
                sn = "" 

            with open('Gracia_Assistant.txt', 'w') as file:
                if 'yes' in sn.lower() or 'sure' in sn.lower() or 'yeah' in sn.lower():
                    current_time = datetime.now()
                    strTime = f"{current_time.hour}:{current_time.minute}"
                    file.write(f"{strTime}: {note}\n")
                else:
                    file.write(f"{note}\n")

    elif "showing notes" in user_data:
        text_to_speech("Showing notes")
        try:
            with open("Gracia_Assistant.txt", "r") as file:
                notes = file.read()
        
            if notes:
                print(notes)
                text_to_speech(notes)
            else:
                text_to_speech("The note file is empty.")
        except FileNotFoundError:
            text_to_speech("No notes found. Please write a note first.")

    elif "joke" in user_data:
        jk=(pyjokes.get_joke(language="en"))      
        text_to_speech("This joke is for you")
        print(jk)
        text_to_speech(jk)
        return ("This joke is for you,"+ jk)
    
    elif "Switch window" in user_data or "switch window" in user_data:
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.keyUp('alt')
        
    elif "CPU" in user_data or "cpu" in user_data or "Cpu" in user_data:
        return ("Your CPU is at "+cpu())
    
    elif "Battery" in user_data or "battery" in user_data:
        return ("Your "+cpubattery())
            
    elif "bye" in user_data or "Bye" in user_data:
         text_to_speech("Byee! Have a nice day!")
         return "Byee! Have a nice day!"
     
    elif  "Quit" in user_data or "quit" in user_data or "Close" in user_data or "close" in user_data or "Shutoff" in user_data or "shutoff" in user_data:
         text_to_speech("Ok mam. Have a good day!")
         return "Ok mam. Have a good day!" 
     
    elif "shutdown" in user_data or "turnoff" in user_data:
        text_to_speech("Hold on a second! Your system is on its way to shutdown")
        text_to_speech("Make sure all of your applications are closed")
        time.sleep(5)
        subprocess.call(["shutdown","/s"])
        
    elif "restart" in user_data:
        subprocess.call(["shutdown","/r"])
        
    elif "hibernate" in user_data:
        text_to_speech("Hibernating...")
        subprocess.call(["shutdown","/h"])
        
    elif "empty recycle bin" in user_data or "Empty recycle bin" in user_data:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        text_to_speech("recycle bin recycled")
        return "recycle bin recycled"
    
    elif "ip" in user_data or "IP" in user_data or "Ip" in user_data:
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        text_to_speech("Your IP Address is "+ ip)
        return ("Your IP Address is "+ ip)
        
    elif "bmi" in user_data or "BMI" in user_data or "Bmi" in user_data:
        text_to_speech("Please tell your height in centimeteres.")
        height = convert_speech_to_text()  #*
        text_to_speech("Please tell your weight in kilograms")
        weight = convert_speech_to_text()
        height = float(height)/100
        BMI = float(weight)/(height*height)
        text_to_speech("Your body mass index is "+ str(BMI))
        print("Your body mass index is "+ str(BMI))
        if (BMI>0):
            if (BMI<=16):
                text_to_speech("You are severly underweighted person.")
                return "You are severly underweighted person."
            elif (BMI<=18.5):
                text_to_speech("You are underweighted person.")
                return "You are underweighted person."
            elif (BMI<=25):
                text_to_speech("You are healthy person.")
                return "You are healthy person."
            elif (BMI<=30):
                text_to_speech("You are severly overweighted person.")
                return "You are severly overweighted person."
        else:
            text_to_speech("Enter valid details")
            return "Enter valid details"
                
    
    elif "movie" in user_data or "Movie" in user_data:
        return ("The summary of this movie is "+movie_summary())
    
    
    elif "news" in user_data or "News" in user_data:
        news_data = get_news(news_limit=3)
        news_summary = "Today's news: "
        for item in news_data:
            news_summary += f"\nTitle: {item['title']}, Date: {item['date']}"
        text_to_speech(news_summary)
        print(news_summary)
        return (news_summary)
    
    elif "password" in user_data or "Password" in user_data:
        password = generate_password()
        text_to_speech("Showing password, " + password)
        return("Showing password: "+ password)
        result_password = show_password()
        text_to_speech(result_password)
        return(result_password)
    
    elif "calendar" in user_data or "Calendar" in user_data:
        try:
            year = int(year_field.get())  
            result_calendar = calendar.TextCalendar().formatyear(year)  
            root = Tk()
            root.config(background="blue")
            root.title(f'Calendar - {year}')
            root.geometry('600x700')
            cal_label = Label(root, text=result_calendar, font=("Courier", 10, "bold"), bg="white", anchor="w", justify="left")
            cal_label.pack(pady=20, padx=20, fill="both")
            root.mainloop()

        except ValueError:
            error_label.config(text="Invalid year. Please enter a valid year.")

        new = Tk()
        new.config(background="blue")
        new.title('Calendar')
        new.geometry('400x300')
        cal_label = Label(new, text="Calendar", bg="blue", font=("Times", 25, "bold"), fg="white")
        cal_label.grid(row=0, column=1, pady=10)
    
        year_label = Label(new, text="Enter Year:", bg="blue", fg="white", font=("Times", 14))
        year_label.grid(row=1, column=0, padx=10, pady=10)
        year_field = Entry(new, font=("Times", 14))
        year_field.grid(row=1, column=1, padx=10, pady=10)

        show_button = Button(new, text='Show Calendar', fg="black", bg="white", command=show_calendar, font=("Times", 14))
        show_button.grid(row=2, column=1, pady=20)

        error_label = Label(new, text="", bg="blue", fg="red", font=("Times", 12))
        error_label.grid(row=3, column=1, pady=10)
        new.mainloop()
        if result_calendar:
            print("Generated Calendar:\n")
            print(result_calendar)
        else:
            print("No calendar was generated.")
    
    # elif "rock" in user_data or "Rock" in user_data:
    #     you = int(input("Please enter your choice:- \n 1-Rock \n2-Paper \n3-Scissor"))
    #     text_to_speech(int(input("Please enter your choice:- \n 1-Rock \n2-Paper \n3-Scissor")))
    #     shapes = {1-'rock', 2-'paper', 3-'scissor'}
    #     text_to_speech(" 1-'rock', 2-'paper', 3-'scissor' ")
        
    #     if you not in shapes:
    #         print("Please enter a valid number")
    #         text_to_speech("Please enter a valid number")
    #         exit()
    #     comp = random.randint(1,3)
    #     print("You choose", you)
    #     text_to_speech("You choose",you)
    #     print("Computer choose", comp)
    #     text_to_speech("Computer choose", comp)
    #     if (you==1) and (comp==3) or (you==2) and (comp==1) or (you==3) and (comp==2):
    #         text_to_speech("Congratulations you won!")
    #         print("Congratulations you won!")
    #     elif(you==comp):
    #         text_to_speech("Match tied")
    #         print("Match tied")
    #     else:
    #         text_to_speech("You loose!")
    #         print("You loose!")
    
    else:
         text_to_speech("I'm still learning, but I can't assist with that yet. How can I help you otherwise?")
         return "I'm still learning, but I can't assist with that yet. How can I help you otherwise?"

if __name__ == "__main__":
    while True:
        user_data = convert_speech_to_text()
        handle_user_request(user_data)
        
        
    
    
    
    