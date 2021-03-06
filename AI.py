import os
import playsound
import speech_recognition 
import time
import sys
import ctypes
import wikipedia
from datetime import datetime, date
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
import pyttsx3
from pyowm import OWM
import pyaudio
import random


AI_ear = speech_recognition.Recognizer()
AI_mouth = pyttsx3.init()
language = 'vi'


while True:
	with speech_recognition.Microphone() as mic:
		print("AI: I'm listening")
		audio = AI_ear.listen(mic, phrase_time_limit=8)
	try:
		you = AI_ear.recognize_google(audio)  
	except:
		you = ""

	print("You:" + you)

	if you == "":
		AI = "I can't hear you!"
		print(AI)
	elif "hello" in you:
		date_time = int(strftime('%H'))
		while True:
			if date_time < 12:
				AI = "Good morning! Have a good day. How can I help you?"
				print("AI:" + AI)
				tts = gTTS(you, lang=language, slow=False)
				tts.save("sound.mp3")
				playsound.playsound("sound.mp3", False)
				os.remove("sound.mp3")	
				break
			elif 12 <= date_time < 18:
				AI = "Good afternoon! What have you planned for this afternoon?"
				print("AI:" + AI)
				AI_mouth = pyttsx3.init()
				AI_mouth.say(AI)
				AI_mouth.runAndWait()	
				break
			elif 18 <= date_time <= 24:
				AI = "Good evening! Have you had dinner yet?"
				print("AI:" + AI)
				AI_mouth = pyttsx3.init()
				AI_mouth.say(AI)
				AI_mouth.runAndWait()	
				break	
	elif "introduce yourself" in you:
		AI = """Tôi có thể làm các việc sau đây:
		1. Chào hỏi
		2. Cho biết ngày, giờ hiện tại
		3. Mở excel, word, powerpoint
		4. Mở các website như Google, Youtube, Gmail,...
		5. Xem thời tiết hiện tại của bất cứ thành phố nào
		6. Nhắc nhở bạn các công việc cần làm
		7. Tìm kiếm một thông tin bất kì từ Wikipedia
		8. Nói một câu nói vui cho bạn
		9. Tắt màn hình khi không dùng nữa """
		print("AI:" + AI)
		time.sleep(20)
	elif "word" in you:
		AI = "Ok! I'm opening "
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
		time.sleep(1)
		os.startfile('C:\\Program Files (x86)\\Microsoft Office\\Office16\\WINWORD.EXE')
	elif "Microsoft" in you:
		AI = "Ok! I'm opening "
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
		time.sleep(1)
		os.startfile("C:\\Program Files (x86)\\Microsoft Office\\Office16\\EXCEL.EXE") 
	elif "open" in you:
		AI = "Ok! I'm opening "
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
		time.sleep(1)
		os.startfile('C:\\Program Files (x86)\\Microsoft Office\\Office16\\POWERPNT.EXE')
	elif "team" in you:
		AI = "Ok! I'm opening "
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
		os.startfile('C:\\Users\\Admin\\OneDrive\\Desktop\\Microsoft Teams.lnk')
	elif "today" in you:
		today = date.today()
		AI = today.strftime("%B %d, %Y")
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "time" in you:
		now = datetime.now()
		AI = now.strftime("%H hours %M minutes %S seconds")
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "bye" in you:
		AI = "Bye Kiệt"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "America" in you:
		AI = "Joe Biden"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "Russia" in you:
		AI = "Vladimir Putin"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif 'how are you' in you:
		AI="I'm fine, thank you!"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif 'how old are you' in you:
		AI="I'm zero year old"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "thank you" in you:
		AI='You are welcome'
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "name" in you:
		AI="My name is AI"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "do you know me" in you:
		AI = "Yes, I know. You are Kiệt"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif 'sleep 5 second' in you:
		AI='Finish'
		time.sleep(5)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif 'shut down' in you:
		os.system('shutdown -s')
	elif 'restart' in you:
		os.system('shutdown -r')
	elif "YouTube" in you:
		webbrowser.open('https://www.youtube.com',new=2)
		AI="Ok!Bye"	
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "Google" in you:
		webbrowser.open('https://www.google.com.vn/',new=2)
		AI="Ok!Bye"	
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "music" in you:
		webbrowser.open('https://www.youtube.com/results?search_query=music',new=2)
		AI="Ok!Bye"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "remix" in you:
		webbrowser.open('https://www.youtube.com/results?search_query=nh%E1%BA%A1c+remix',new=2)
		AI="Ok!Bye"	
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "Apple" in you:
		webbrowser.open('https://www.apple.com/',new=2)
		AI="Ok!Bye"	
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "Facebook" in you:
		webbrowser.open('https://www.facebook.com/',new=2)
		AI="Ok!Bye"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "Gmail" in you:
		webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=2)
		AI="Ok!Bye"
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()
	elif "temperature" in you:
		while True:
			AI = "Where do you want to see the weather?"
			print("AI:" + AI)
			AI_mouth = pyttsx3.init()
			AI_mouth.say(AI)
			AI_mouth.runAndWait()
			time.sleep(3)
			ow_url = "http://api.openweathermap.org/data/2.5/weather?"
			city = input()
			if not city:
				pass
			api_key = "fe8d8c65cf345889139d8e545f57819a"
			call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
			response = requests.get(call_url)
			data = response.json()
			if data["cod"] != "404":
				city_res = data["main"]
				current_temperature = city_res["temp"]
				current_pressure = city_res["pressure"]
				current_humidity = city_res["humidity"]
				suntime = data["sys"]
				wthr = data["weather"]
				weather_description = wthr[0]["description"]
				now = date.today()
				content = """
				Hôm nay là ngày {day} tháng {month} năm {year}
				Nhiệt độ trung bình là {temp} độ C
				Áp suất không khí là {pressure}Pa
				Độ ẩm là {humidity}%
				""".format(day = now.day,month = now.month, year= now.year,	                                                                           	   
	                       temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
				print(content)
			else:
				AI = "Your address could not be found!"
				print(AI)
				AI_mouth = pyttsx3.init()
				AI_mouth.say(AI)
				AI_mouth.runAndWait()
			break
	elif "alarm" in you:
		hour = int(input("Hour:"))
		minutes = int(input("Minutes:"))
		print("Nhắc nhở đã được cài")
		while True:
			if hour == int(datetime.today().strftime("%H")) and minutes == int(datetime.today().strftime("%M")):
				AI = "It's time!"
				print(AI)					
				AI_mouth = pyttsx3.init()
				AI_mouth.say(AI)
				AI_mouth.runAndWait()
				os.system("start iphone.mp3")
				break
	elif "Wikipedia" in you:
		AI_ear = speech_recognition.Recognizer()
		with speech_recognition.Microphone() as mic:
			print("Wikipedia: ...")
			audio = AI_ear.listen(mic)
		try:
			wiki = AI_ear.recognize_google(audio)
		except:
			AI = "I don't understand, can you say it again?"
			print("AI:" + AI)
			AI_mouth = pyttsx3.init()
			AI_mouth.say(AI)
			AI_mouth.runAndWait()
		wikipedia.set_lang("vi")
		wiki=wikipedia.summary(wiki)
		print(wiki)
		AI = wiki
		time.sleep(3)	
		break	
	elif "tell me" in you:
		with open('joke.txt', 'r') as file:
			jokelist = file.read().split("\n*")
		joke = str(random.choice(jokelist))
		AI = joke
		print("AI:" + AI)
		AI_mouth = pyttsx3.init()
		AI_mouth.say(AI)
		AI_mouth.runAndWait()	
		break
	break

	
	