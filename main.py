import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

def record_text():  
     # Loop in case of errors
     while True:
        try:
             # use the microphone as source for input.
             with sr.Microphone() as source2:
                 # Prepare recognizer to recieve input
                 r.adjust_for_ambient_noise(source2, duration=0.2)

                 #listens for the user's input
                 audio2 = r.listen(source2)

                 # Using google to recognize audio
                 MyText = r.recognize_google(audio2)

                 return MyText


        except sr.RequestError as e:
             print("Could not request result: {}".format(e))
        
        except sr.UnknownValueError:
             print("unknown error occurred")

     return 

def output_text(text):
    f = open ("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while True:
    text = record_text()
    if text == 'exit':
        print('Bye, bye!')
        break
    output_text(text)

    print("Wrote text: ", text)
