import speech_recognition as sr
import sys

# initialize the recognizer
r = sr.Recognizer()
print("Please talk")
# offset=4,
response = {
        "success": True,
        "error": None,
        "transcription": None
    }
while 1:
	with sr.Microphone() as source:
	    # read the audio data from the default microphone
	    audio_data = r.record(source, duration=5)
	    print("Recognizing...")
	    try:
	        response["transcription"] = r.recognize_google(audio_data)
	    except sr.RequestError:
	        # API was unreachable or unresponsive
	        response["success"] = False
	        response["error"] = "API unavailable"
	    except sr.UnknownValueError:
	        # speech was unintelligible
	        response["error"] = "Unable to recognize speech"
	    print(response["transcription"])
	    text = response["transcription"]
	    if text == "hello":
	    	print("bat den")
	    else: 
	    	print("den chua duoc bat")
	    # return response
	    

