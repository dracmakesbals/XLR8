import speech_recognition as sr

def listen_and_convert_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Set up the microphone
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait!")
        recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        print("Listening for your command... (Please speak into the microphone)")

        try:
            # Listen to the user's voice input
            audio = recognizer.listen(source, timeout=10)  # Timeout after 10 seconds of no speech
            print("Processing your input...")

            # Use Google's speech recognition API to convert audio to text
            text = recognizer.recognize_google(audio)
            print(f"Converted Text: {text}")

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")

if __name__ == "__main__":
    listen_and_convert_to_text()
