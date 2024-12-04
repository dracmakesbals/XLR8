from googletrans import Translator

# Initialize the translator
translator = Translator()

# Function to translate text to Hindi
def translate_to_hindi(text):
    # Translate the text
    translated = translator.translate(text, src='en', dest='hi')
    print(f"Original Text: {text}")
    print(f"Translated Text (in Hindi): {translated.text}")

# Main function
def main():
    # Get text input from the user
    text = input("Enter the text to translate into Hindi: ")
    
    # Translate the input text to Hindi
    translate_to_hindi(text)

# Run the program
if __name__ == "__main__":
    main()
