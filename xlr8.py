import numpy as np
import argparse
import noisereduce as nr
import speech_recognition as sr
import sqlite3
import time

# def reduce_noise(audio_data, sample_rate=16000):
#     audio_np = np.frombuffer(audio_data.get_raw_data(), dtype=np.int16)
#     reduced_noise = nr.reduce_noise(y=audio_np, sr=sample_rate)
#     return sr.AudioData(reduced_noise.tobytes(), sample_rate, 2)

def save_to_database(text):
    conn = sqlite3.connect("transcriptions.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS transcriptions (id INTEGER PRIMARY KEY, text TEXT)")
    cursor.execute("INSERT INTO transcriptions (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()

def real_time_transcription(language="en-US"):
    recognizer = sr.Recognizer()
    
    # Create a new file for each session, with timestamp in the filename
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"transcriptions_{timestamp}.txt"
    
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait!")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print(f"Listening for speech in {language}... (Press Ctrl+C to stop)")

        try:
            while True:
                print("Say something...")
                audio = recognizer.listen(source, timeout=20)  # Timeout if no speech
                try:
                    # audio = reduce_noise(audio)  # Optionally, enable noise reduction
                    text = recognizer.recognize_google(audio, language=language)
                    print(f"Real-time Transcription: {text}")

                    # Save to the individual text file with the session's name
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{text}\n")
                    
                    # Save to database
                    save_to_database(text)
                    
                except sr.UnknownValueError:
                    print("Could not understand the audio.")
                except sr.RequestError as e:
                    print(f"Google API Error: {e}")
        except KeyboardInterrupt:
            print("\nStopped listening.")
            print(f"Transcriptions saved in: {filename}")

def choose_language():
    print("Select a language for transcription:")
    print("1. Spanish (es-ES)")
    print("2. French (fr-FR)")
    print("3. English (en-US)")
    print("4. German (de-DE)")
    print("5. Italian (it-IT)")
    print("6. Portuguese (pt-PT)")
    print("7. Hindi (hi-IN)")
    print("8. Japanese (ja-JP)")
    print("9. Russian (ru-RU)")
    print("10. Bengali (bn-BD)")
    print("11. Arabic (ar-SA)")
    print("12. Chinese (zh-CN)")
    
    while True:
        choice = input("Enter the number corresponding to your choice: ")
        
        if choice == "1":
            return "es-ES"  # Spanish
        elif choice == "2":
            return "fr-FR"  # French
        elif choice == "3":
            return "en-US"  # English
        elif choice == "4":
            return "de-DE"  # German
        elif choice == "5":
            return "it-IT"  # Italian
        elif choice == "6":
            return "pt-PT"  # Portuguese
        elif choice == "7":
            return "hi-IN"  # Hindi
        elif choice == "8":
            return "ja-JP"  # Japanese
        elif choice == "9":
            return "ru-RU"  # Russian
        elif choice == "10":
            return "bn-BD"  # Bengali
        elif choice == "11":
            return "ar-SA"  # Arabic
        elif choice == "12":
            return "zh-CN"  # Chinese
        else:
            print("Invalid choice. Please select a valid number between 1 and 12.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Real-time transcription script with language selection.")
    parser.add_argument(
        "--language", 
        type=str, 
        default=None, 
        help="Language code for transcription (default: None). You can specify it directly or choose interactively."
    )
    
    args = parser.parse_args()
    if args.language:
        language = args.language
    else:
        language = choose_language()  

    real_time_transcription(language=language)