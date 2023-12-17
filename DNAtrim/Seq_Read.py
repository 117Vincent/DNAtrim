import os  # Don't forget to include this line at the beginning of your script

# Function to read a sequence file and return its content
def read_sequence(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Prompt user to input source and output directories
source_directory = input("Enter the source directory path: ")
output_directory = input("Enter the output directory path: ")

# Ensure output directory exists or create it if not
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all files in the source directory
files = os.listdir(source_directory)

# Prompt user to input letters to filter files
search_letters = input("Enter the sequence of letters to search for: ")

# Process each file in the source directory
for file_name in files:
    file_path = os.path.join(source_directory, file_name)
    
    # Check if it's a file (not a directory) and has .seq extension
    if os.path.isfile(file_path) and file_name.endswith('.seq'):
        # Read content of .seq file
        file_content = read_sequence(file_path)
        
        # Check if the content contains the specified sequence of letters
        found = False
        for line_index, line in enumerate(file_content):
            if search_letters in line:
                found = True
                # Create the output file with modified content
                output_file_path = os.path.join(output_directory, file_name)
                with open(output_file_path, 'w') as output_file:
                    # Write the first line (header) from the original file
                    output_file.write(file_content[0])
                    
                    # Find the position of search letters in the line
                    search_pos = line.index(search_letters)
                    
                    # Write content starting from the line where search letters are found
                    output_file.write(line[search_pos:])
                    
                    # Write content from subsequent lines
                    for next_line in file_content[line_index + 1:]:
                        output_file.write(next_line)
                
                print(f"Processed: {file_name} - Saved in {output_directory}")
                break  # Stop further search in this file once found
        
        if not found:
            print(f"Skipped: {file_name} - Sequence not found")
