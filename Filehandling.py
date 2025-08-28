def file_read_write_challenge():
    try:
        # Ask user for input file
        input_filename = input("Enter the name of the file to read: ")

        # Open and read content
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify the content (for example: make it uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File has been modified and saved as '{output_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read/write this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Run the program
file_read_write_challenge()
