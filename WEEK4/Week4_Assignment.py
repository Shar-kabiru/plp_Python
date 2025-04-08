import os
def filehandling():
    while True:
        input_file = input("Enter the input filename (e.g., 'input.txt'): ").strip()
        output_file = "output.txt"  

        if not os.path.exists(input_file):
            print(f"\n Error: File '{input_file}' does not exist.")
            break

# Ask user for lines to append
        line1 = input("Enter first line to append: ")
        line2 = input("Enter second line to append: ")
        
        try:

            print("Input File:\n")
            with open(input_file, 'r') as file:
                content = file.read()
                print(content)
                
    # Append the two lines
            updated_file = content + "\n" + line1 + "\n" +line2

    # Write to output file
            with open(output_file, "w") as output:
                    output.write(updated_file)
                    output.write("\n\n")
    # Print a success message once the new file is created.
            print(f"\nSuccess! Modified content saved to '{output_file}'")
            print("Appended lines:")
            print(f"1. {line1}")
            print(f"2. {line2}")
            with open(output_file, 'r') as file:
                content = file.read()
                print(content)
            break

        except Exception as e:
            print(f"\n Unexpected error: {e}")

filehandling()