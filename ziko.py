import os
import glob
def merge_txt_files():
    global folderTomerge 
    global mergedfile
    folderTomerge = input(f">> Txt Files Path :")
    mergedfile = "FZ"
    # Create the new folder path
    new_folder = os.path.join(folderTomerge, mergedfile)
    
    # Create the ZM folder if it does not exist
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # Generate the output file path in the new folder
    output_file = os.path.join(new_folder, 'merged_file.txt')

    if os.path.exists(folderTomerge):
        # Get a list of all .txt files in the specified folder
        txt_files = glob.glob(os.path.join(folderTomerge, '*.txt'))
        
        # Open the output file in write mode with utf-8 encoding
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Iterate through the list of .txt files
            for txt_file in txt_files:
                try:
                    # Open each file in read mode with utf-8 encoding
                    with open(txt_file, 'r', encoding='utf-8') as infile:
                        # Read the contents of the file and write them to the output file
                        outfile.write(infile.read())
                except UnicodeDecodeError:
                    print(f"{red('UnicodeDecodeError: Unable to decode file ')}{red(txt_file)}")

        print(f"{yellow(' Merged Successfuly >>')} {cyan(output_file)}")
        remove_duplicates(output_file)
    else:
        print(f"Folder {red(folderTomerge)} Not exist or invalid ")
        print(f"{red('---------------------------')} ")
        merge_txt_files()

def remove_duplicates(megedfile=''):
    global input_file
    if megedfile =='' :
        input_file = input("Enter File Path: ")
    else:
        input_file = megedfile

    if os.path.isfile(input_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Remove duplicates while preserving order
        seen_lines = set()
        unique_lines = []
        for line in lines:
            if line not in seen_lines:
                seen_lines.add(line)
                unique_lines.append(line)

        # Write unique lines back to the same input file
        with open(input_file, 'w', encoding='utf-8') as f:
            # Write lines with proper newline characters
            for line in unique_lines:
                if line.endswith('\n'):
                    f.write(line)
                else:
                    f.write(line + '\n')
        # Sort lines in descending order
        sort_lines_descending(input_file)

        print(f"Duplicates removed and lines sorted in descending order for file: {input_file}")
    else:
        print(f"File '{input_file}' does not exist.")
        remove_duplicates()
        
def sort_lines_descending(input_file):
    # Read input file and sort lines in descending order
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception:
        print(f"Error Reading file: {red(input_file)}\n")
    # Sort lines in descending order
    sorted_lines = sorted(lines, reverse=True)

    # Write sorted lines back to the same input file
    try:
        with open(input_file, 'w', encoding='utf-8') as f:
            f.writelines(sorted_lines)
    except Exception:
        print(f"Error Writen in file: {red(input_file)}\n")

    # Step 3: Split into chunks of 50000 lines and save to separate files
    split_and_save(input_file)

def split_and_save(input_file):
    output_folder = str(input("Enter the Output Folder Path : "))
    try:
        os.makedirs(output_folder, exist_ok=True)
        #delete_files_in_folder()
        print(f'{yellow("Folder Created successfully .")}')
    except Exception:
        print("Error Create Folder")
        split_and_save(input_file)


    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    chunk_size = int(input("Enter the Number of ligne to separate : "))
    num_chunks = (total_lines // chunk_size) + 1
    try:
        for i in range(num_chunks):
            start = i * chunk_size
            end = min((i + 1) * chunk_size, total_lines)
            chunk_lines = lines[start:end]
            output_file = os.path.join(output_folder, f"{i+1}.txt")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.writelines(chunk_lines)
                print(f'{cyan("Spliting and saving file [")}{output_folder}/{i+1}.txt{cyan("]")} > {yellow("successfully")}.')
        print(f"{cyan('================= Job Done ==================')}")
        Options()
    except Exception:
        print(f"Error saving file: {red(input_file)}\n")

def RunOption1():
    # Step 1: Remove duplicates from input_file
    remove_duplicates()

def RunOption2():
    print('option 02')

def delete_files_in_folder(folder_path):
    try:
        # List all files in the folder
        files = os.listdir(folder_path)

        # Iterate over the files and delete each one
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted {file_path}")
        
        print(f"All files in {folder_path} have been deleted.")
    
    except Exception as e:
        print(f"Failed to delete files in {folder_path}: {e}")
def Options():
    print(f"{yellow('[')}{red(1)}{yellow(']')} Sort / Remove duplicate and Splite File:")
    print(f"{yellow('[')}{green(2)}{yellow(']')} Merge All txt file and run option {yellow('[')}{red(1)}{yellow(']')}:")
    option = input("Chose option : ")
    if option== "1" or option == "01":
        RunOption1()
    elif option== "2" or option == "02":
        merge_txt_files()
    else:
        print(f"{red('Options invalid')}\n")
        Options()

#COLORS FUNCTIONS =====================
def red(text):
    return(f"\033[1;31m{text}\033[0m")
def green(text):
    return(f"\033[92m{text}\033[0m")
def yellow(text):
    return(f"\033[93m{text}\033[0m")
def blue(text):
    return(f"\033[94m{text}\033[0m")
def magenta(text):
    return(f"\033[95m{text}\033[0m")
def cyan(text):
    return(f"\033[96m{text}\033[0m")
def logo():
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Unix/Linux/MacOS
        os.system('clear')
    print(red("++++++++++++ +++++++  +++      +++  +++++++++"))
    print(red("++++++++++++ +++++++  +++     +++  +++      +++"))
    print(yellow("      +++++     ++    +++    +++  +++        +++"))
    print(yellow("     +++++      ++    +++  +++   +++          +++"))
    print(green("   +++++        ++    +++ +++   +++     FOX    +++"))
    print(green(" +++++          ++    +++ +++   +++            +++"))
    print(yellow("++++            ++    +++   +++  +++          +++"))
    print(red("++++++++++++ ++++++++ +++     +++  +++      +++"))
    print(red("++++++++++++ ++++++++ +++      +++   ++++++++"))
    print("\n ")
if __name__ == "__main__":
    logo()
    Options()
    
