# Write a Python script to:
# Read the contents of input.txt.
def filehandling(inputfile, outputfile):
    try:
        print("Input File:\n")
        with open("WEEK4/input.txt", "r") as file:
            content = file.read()
            print(content)
             
# Count the number of words in the file.
            word_count = len(content.split())
            print(f"\nWord Count: {word_count}\n")
# Convert all text to uppercase.
            upper_case = content.upper()
            print("Text To UPPERCASE:")
            print(upper_case)
# Write the processed text and the word count to a new file called output.txt.
            with open(outputfile, "w") as output:
                output.write(upper_case)
                output.write("\n\n")
                output.write(f"WORD COUNT: {word_count}\n")
# Print a success message once the new file is created.
            print(f"\nSuccess! '{outputfile}' has been created with processed content.")
            print("\nOutput.txt:\n")
            with open(outputfile, "r") as output:
                print(output.read())

    except FileNotFoundError:
        print(f"Error: The file '{inputfile}' was not found.")


filehandling("input.txt", "output.txt")