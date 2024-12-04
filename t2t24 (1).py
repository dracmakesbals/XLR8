from googletrans import Translator

# Initialize the translator
translator = Translator()

# Function to translate a Hindi text file to English
def translate_file(input_file, output_file):
    try:
        # Open the input file with Hindi sentences
        with open(input_file, 'r', encoding='utf-8') as file:
            hindi_text = file.readlines()
        
        # Prepare the output list for translations
        translated_text = []

        for sentence in hindi_text:
            # Strip leading/trailing whitespaces and newlines
            sentence = sentence.strip()
            
            # Skip empty lines
            if sentence:
                # Translate the Hindi sentence to English
                translation = translator.translate(sentence, src='hi', dest='en')
                translated_text.append(translation.text)
            else:
                translated_text.append("")  # Add an empty line for blank lines

        # Write the translated text to the output file
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write("\n".join(translated_text))

        print(f"Translation completed! The translated text is saved in '{output_file}'.")

    except Exception as e:
        print(f"Error: {e}")

# Main function
def main():
    # Input and output file paths
    input_file = input("Enter the path to the Hindi text file: ")
    output_file = input("Enter the path for the output translated file (e.g., translated.txt): ")
    
    # Call the function to translate the file
    translate_file(input_file, output_file)

# Run the script
if __name__ == "__main__":
    main()
