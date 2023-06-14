import os
import re
import sys
import termios
import tty
from colorama import Fore, Style
from tqdm import tqdm
from rich.progress import Progress

def count_php_files(directory):
    count = 0
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".php"):
                count += 1
    return count

def count_files(directory):
    count = 0
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            count += 1
    return count



def scan_files_php(directory, vulnerable_functions, mode="default", remove_prepare=False):
    results = {}
    total_files = count_php_files(directory)

    with Progress() as progress:
        task = progress.add_task("[cyan]Scanning files...", total=total_files)

        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith(".php"):
                    filepath = os.path.join(foldername, filename)
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            lines = f.readlines()
                            for i, line in enumerate(lines, start=1):
                                for func in vulnerable_functions:
                                    # Using regex to find the exact function call
                                    match = re.search(r'\b' + re.escape(func), line)
                                    if match:
                                        # Manage the parenthesis and the arguments
                                        parenthesis_counter = 1  # Adjust this line
                                        start = match.end()
                                        args = ''
                                        for index in range(i-1, len(lines)):
                                            line = lines[index]
                                            start = start if index == i-1 else 0  # reset the start for the next lines
                                            for char in line[start:]:
                                                if char == '(':
                                                    parenthesis_counter += 1
                                                elif char == ')':
                                                    parenthesis_counter -= 1
                                                args += char
                                                if parenthesis_counter == 0:
                                                    break
                                            if parenthesis_counter == 0:
                                                break

                                        if remove_prepare and ("prepare" in line or (i > 1 and "prepare" in lines[i-2])):
                                            continue
                                        if mode=='xss':
                                            if '$' in line and 'esc' not in line and 'wp_kses' not in line:
                                                if "$" in args:
                                                    if filepath not in results:
                                                        results[filepath] = []
                                                    results[filepath].append((i, line))
                                        else:
                                            if "$" in args:
                                                if filepath not in results:
                                                    results[filepath] = []
                                                results[filepath].append((i, line))
                    except Exception as e:
                        print(f"Error processing file {filepath}: {str(e)}")

                    progress.update(task, advance=1)
    print("\n")
    return results

def scan_files(directory, vulnerable_functions, mode="default", remove_prepare=False):
    results = {}
    total_files = count_files(directory)

    with Progress() as progress:
        task = progress.add_task("[cyan]Scanning files...", total=total_files)

        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                if not filename.endswith(".js") and not filename.endswith(".jpg"):
                    filepath = os.path.join(foldername, filename)
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            lines = f.readlines()
                            for i, line in enumerate(lines, start=1):
                                for func in vulnerable_functions:
                                    # Using regex to find the exact function call
                                    match = re.search(r'\b' + re.escape(func), line)
                                    if match:
                                        # Manage the parenthesis and the arguments
                                        parenthesis_counter = 1  # Adjust this line
                                        start = match.end()
                                        args = ''
                                        for index in range(i-1, len(lines)):
                                            line = lines[index]
                                            start = start if index == i-1 else 0  # reset the start for the next lines
                                            for char in line[start:]:
                                                if char == '(':
                                                    parenthesis_counter += 1
                                                elif char == ')':
                                                    parenthesis_counter -= 1
                                                args += char
                                                if parenthesis_counter == 0:
                                                    break
                                            if parenthesis_counter == 0:
                                                break

                                        if remove_prepare and ("prepare" in line or (i > 1 and "prepare" in lines[i-2])):
                                            continue
                                        if mode == 'xss':
                                            if filepath not in results:
                                                results[filepath] = []
                                            results[filepath].append((i, line))
                                        else:
                                            if filepath not in results:
                                                results[filepath] = []
                                            results[filepath].append((i, line))
                    except Exception as e:
                        print(f"Error processing file {filepath}: {str(e)}")

                progress.update(task, advance=1)

    print("\n")
    return results

def scan_files_nodejs(directory, vulnerable_functions, mode="default", remove_prepare=False):
    results = {}
    total_files = count_files(directory)

    with Progress() as progress:
        task = progress.add_task("[cyan]Scanning files...", total=total_files)

        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines, start=1):
                            for func in vulnerable_functions:
                                # Using regex to find the exact function call
                                match = re.search(r'\b' + re.escape(func), line)
                                if match:
                                    # Manage the parenthesis and the arguments
                                    parenthesis_counter = 1  # Adjust this line
                                    start = match.end()
                                    args = ''
                                    for index in range(i-1, len(lines)):
                                        line = lines[index]
                                        start = start if index == i-1 else 0  # reset the start for the next lines
                                        for char in line[start:]:
                                            if char == '(':
                                                parenthesis_counter += 1
                                            elif char == ')':
                                                parenthesis_counter -= 1
                                            args += char
                                            if parenthesis_counter == 0:
                                                break
                                        if parenthesis_counter == 0:
                                            break

                                    if remove_prepare and ("prepare" in line or (i > 1 and "prepare" in lines[i-2])):
                                        continue
                                    if mode == 'xss':
                                        if filepath not in results:
                                            results[filepath] = []
                                        results[filepath].append((i, line))
                                    else:
                                        if filepath not in results:
                                            results[filepath] = []
                                        results[filepath].append((i, line))
                except Exception as e:
                    print(f"Error processing file {filepath}: {str(e)}")

                progress.update(task, advance=1)

    print("\n")
    return results



def find_function(lines, index):
    # Search backwards to find the start of the function
    start = index
    while start > 0 and 'function' not in lines[start]:
        start -= 1

    # Search forwards to find the end of the function
    end = index
    open_brackets = 1  # Assume we're inside the function
    while end < len(lines) - 1:
        end += 1
        line = lines[end].strip()
        for char in line:
            if char == '{':
                open_brackets += 1
            elif char == '}':
                open_brackets -= 1
                if open_brackets == 0:
                    return start, end

    return start, end

def print_framed_list(title, items, color):
    print(f"{color}+" + "-" * (len(title) + 2) + "+")
    print(f"{color}| {title} |")
    print(f"{color}+" + "-" * (len(title) + 2) + "+")
    for i, item in enumerate(items, start=1):
        print(f"{color}{i}. {item}")
    print(f"{color}+" + "-" * (len(title) + 2) + "+")

def get_input(choices):
    choice = input("Enter your choice: ").lower()

    while choice not in choices:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice: ").lower()
    print("\n")

    return choice

def print_help_message_vulnerability_menu():
    print(f"\n🆘Help for vulnerability menu:")
    print("Press the corresponding number to make a selection.")
    print("h. Show this help message.")
    print("0. Go back to the files menu.\n")

def print_help_message_files_menu():
    print(f"\n🆘Help for files menu:")
    print("Press the corresponding number to make a selection.")
    print("h. Show this help message.")
    print("0. Go back to the files menu.\n")


def print_help_message_occurrences_menu():
    print(f"\n🆘Help for occurrences menu:")
    print("Press the corresponding number to make a selection.")
    print("v. Open the selected file in Visual Studio Code.")
    print("h. Show this help message.")
    print("0. Go back to the files menu.\n")


def print_code_details(file_path, line_number, line, lines, start, end):
    print(Fore.LIGHTYELLOW_EX + f"\nFile: {file_path}\n" + Style.RESET_ALL +
          Fore.LIGHTMAGENTA_EX + f"Line: {line_number}\n" + Style.RESET_ALL +
          Fore.RED + f"Code: {line.strip()}\n" + Style.RESET_ALL +
          "Function:\n")

    print(Fore.WHITE + "+" + "-" * 78 + "+")
    for i in range(start, end + 1):
        if i == start:
            print(Fore.WHITE + "|" + " " * 78 + "|")
        if i == line_number - 1:  # Highlight the vulnerable line
            highlighted_line = Fore.RED + lines[i].rstrip().ljust(77) + Style.RESET_ALL
            print(Fore.WHITE + "" + highlighted_line)
        else:
            highlighted_line = re.sub(r'(\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)',
                                      f'{Fore.GREEN}\\1{Style.RESET_ALL}',
                                      lines[i].rstrip().ljust(78))
            print(Fore.WHITE + highlighted_line)
    print("+" + "-" * 78 + "+")

    print()


def get_input_range(num_choices):
    choice = input("Enter your choice: ").lower()

    if choice == "h":
        return choice
    elif choice == "v":
        return choice

    while not choice.isdigit() or int(choice) < 0 or int(choice) > num_choices:
        print("Invalid choice. Please enter a valid number.")
        choice = input("Enter your choice: ").lower()
    print("\n")
    return choice

def print_help_message():
    print("Press the corresponding number to make a selection.")
    print("Press 'h' to display this help message.")
    print()
    print("In the vulnerability menu, enter the number corresponding to the vulnerability type you want to check.")
    print("In the files menu, enter the number of the file you want to inspect or '0' to go back to the vulnerabilities menu.")
    print("In the occurrences menu, enter the number of the occurrence you want to inspect or '0' to go back to the files menu.")
    print("In the code details, you can view the file, line number, code snippet, and the function where the vulnerability occurs.")
    print("To navigate the menus, use the corresponding numbers or 'h' for help.")
