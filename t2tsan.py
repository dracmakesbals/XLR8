from google.cloud import translate_v2 as translate

# Initialize the Google Translate client
translate_client = translate.Client()

def translate_to_santali(text):
    # Translate the text
    result = translate_client.translate(text, target_language='sat')
    print(f"Original Text: {text}")
    print(f"Translated Text (in Santali): {result['translatedText']}")

def main():
    text = input("Enter the text to translate into Santali: ")
    translate_to_santali(text)

if __name__ == "__main__":
    main()
