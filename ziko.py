import os

def remove_duplicates():
    # Read input file and remove duplicate lines
    input_file = input("Enter File Path : ")
    if os.path.exists(input_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # Use a set to remove duplicates while preserving order
        unique_lines = list(set(lines))
        
        # Write unique lines back to the same input file
        with open(input_file, 'w', encoding='utf-8') as f:
            f.writelines(unique_lines)
        # Step 2: Sort lines in descending order
        sort_lines_descending(input_file)
    else:
        print("Path incorrect ")
        

def sort_lines_descending(input_file):
    # Read input file and sort lines in descending order
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Sort lines in descending order
    sorted_lines = sorted(lines, reverse=True)

    # Write sorted lines back to the same input file
    with open(input_file, 'w', encoding='utf-8') as f:
        f.writelines(sorted_lines)

    # Step 3: Split into chunks of 50000 lines and save to separate files
    split_and_save(input_file)

def split_and_save(input_file):
    output_folder = input("Enter the Output Folder Path : ")
    try:
        os.makedirs(output_folder, exist_ok=True)
        #delete_files_in_folder()
        print(f'{yellow("Folder Created successfully .")}')
    except Exception:
        print("Error Create Folder")

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    chunk_size = int(input("Enter the Number of ligne to separate : "))
    num_chunks = (total_lines // chunk_size) + 1
    
    for i in range(num_chunks):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, total_lines)
        chunk_lines = lines[start:end]
        output_file = os.path.join(output_folder, f"{i+1}.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(chunk_lines)
            print(f'{cyan("Spliting file [")}{i}.txt{cyan(']')} >{yellow('successfully')} \n')
    
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
    print(f'{yellow('[')}{red(1)}{yellow(']')} Sort / Remove duplicate and Splite File:')
    print(f'{yellow('[')}{green(2)}{yellow(']')} Merge All txt file and run option {yellow('[')}{red(1)}{yellow(']')}:')
    option = input("Chose option : ")
    if option== "1" or option == "01":
        RunOption1()
    elif option== "2" or option == "02":
        RunOption2()
    else:
        __name__

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
    print(red("+++++++++++++++ +++++++  ++++      +++  +++++++++"))
    print(red("+++++++++++++++ +++++++  ++++     +++  +++      +++"))
    print(yellow("         +++++     ++    ++++    +++  +++        +++"))
    print(yellow("        +++++      ++    ++++  +++   +++          +++"))
    print(green("      +++++        ++    ++++ +++   +++            +++"))
    print(green("    +++++          ++    ++++ +++   +++            +++"))
    print(yellow("  +++++            ++    ++++   +++  +++          +++"))
    print(yellow(" +++++             ++    ++++    +++  +++        +++"))
    print(red("+++++++++++++++ ++++++++ ++++     +++  +++      +++"))
    print(red("+++++++++++++++ ++++++++ ++++      +++   ++++++++"))
    print("\n ")
if __name__ == "__main__":
    logo()
    Options()
    

