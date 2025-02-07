import argparse
import subprocess
import os
from rich.console import Console
from rich.tree import Tree
from utils import *
from vulnerable_functions import *
import colorama

colorama.init()
console = Console()
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

def print_cool_name():
    top_border = Fore.YELLOW + "┌" + "─" * 100 + "┐" + Style.RESET_ALL
    side_border = Fore.YELLOW + "│" + Style.RESET_ALL + " " * 100 + Fore.YELLOW + "│" + Style.RESET_ALL
    bottom_border = Fore.YELLOW + "└" + "─" * 100 + "┘" + Style.RESET_ALL

    print(top_border)
    print(side_border)
    print(Fore.YELLOW+"│" + " " * 34 + Fore.CYAN + "Welcome to the WhiteHouse!" + Style.RESET_ALL + " " * 40 + Fore.YELLOW+"│")
    print(side_border)
    print(side_border)
    print(Fore.YELLOW+"│" + " " * 32 +Fore.WHITE+ "Created by " + Fore.GREEN + "Malachias Theodoros" + Style.RESET_ALL + " " * 38 + Fore.YELLOW+"│")
    print(side_border)
    print(bottom_border)
    print(r'''
 __      __     __                 __               __  __                                      
/\ \  __/\ \   /\ \         __    /\ \__           /\ \/\ \                                     
\ \ \/\ \ \ \  \ \ \___    /\_\   \ \ ,_\     __   \ \ \_\ \     ___    __  __    ____     __   
 \ \ \ \ \ \ \  \ \  _ `\  \/\ \   \ \ \/   /'__`\  \ \  _  \   / __`\ /\ \/\ \  /',__\  /'__`\ 
  \ \ \_/ \_\ \  \ \ \ \ \  \ \ \   \ \ \_ /\  __/   \ \ \ \ \ /\ \L\ \\ \ \_\ \/\__, `\/\  __/ 
   \ `\___x___/   \ \_\ \_\  \ \_\   \ \__\\ \____\   \ \_\ \_\\ \____/ \ \____/\/\____/\ \____\
    '\/__//__/     \/_/\/_/   \/_/    \/__/ \/____/    \/_/\/_/ \/___/   \/___/  \/___/  \/____/
                                                                                                
                                                                                                  
    ''')
    print(bottom_border)

# Call the function to print the cool name
print_cool_name()


LANGUAGES = [
    "Python",
    "Java",
    "C#",
    "PHP",
    "Node.js",
]

VULNERABILITIES = {
    "SQL Injection": "💉",
    "Path Traversal": "📁",
    "Server-Side Request Forgery (SSRF)": "🔁",
    "Command Injection": "🚀",
    "Insecure Deserialization": "🧪",
    "XML External Entity (XXE)": "📜",
    "Server-Side Template Injection (SSTI)": "🎯",
    "Open Redirect": "🔄",
}

def generate_language_tree():
    tree = Tree(":computer: Programming Language Menu", guide_style="bright_blue")

    for index, language in enumerate(LANGUAGES, start=1):
        tree.add(f"{index}. {language}")

    return tree

def choose_language(last_choice):
    console.print(f"Last choice was: {last_choice.get('language')}")

    language_choice = get_input_range(len(LANGUAGES) + 1)
    last_choice["language"] = language_choice

    return language_choice

def generate_vulnerability_tree():
    tree = Tree(":fire: Vulnerabilities Menu", guide_style="bright_blue")

    for index, (name, icon) in enumerate(VULNERABILITIES.items(), start=1):
        tree.add(f"{index}. {name} [{icon}]")

    return tree

def choose_vulnerability(last_choice):
    console.print(f"Last choice was: {last_choice.get('vulnerability')}")

    vulnerability_choice = get_input_range(len(VULNERABILITIES) + 1)
    last_choice["vulnerability"] = vulnerability_choice

    return vulnerability_choice

def scan_files_for_vulnerability(directory, language, vulnerability):
    vulnerable_functions = get_vulnerable_functions(language)
    vulnerability_names = list(VULNERABILITIES.keys())
    vulnerability_index = int(vulnerability) - 1
    vulnerability_name = vulnerability_names[vulnerability_index]
    functions = vulnerable_functions.get(vulnerability_name, [])

    if language == "PHP":
        return scan_files_php(directory, functions)
    elif language == "Node.js":
        return scan_files_nodejs(directory, functions)
    else:
        return scan_files(directory, functions)

def generate_files_tree(attack_type, files):
    tree = Tree(f":file_folder: Files possibly vulnerable to {attack_type}", guide_style="bright_blue")

    for index, file in enumerate(files, start=1):
        tree.add(f"{index}. {file}")

    return tree

def print_files_menu(attack_type, files, last_choice):
    files_tree = generate_files_tree(attack_type, files)
    console.print(files_tree)
    console.print()
    console.print("Enter the number of the file you want to inspect (or 0 to go back to the vulnerabilities menu):")
    console.print("h. Help", style="yellow")

def choose_file(files, last_choice):
    console.print("Last choice was: {}".format(last_choice.get("file")))

    file_choice = get_input_range(len(files) + 1)
    if file_choice != 'h':
        last_choice["file"] = file_choice

    return int(file_choice) if file_choice.isdigit() else file_choice

def load_project_in_visual_studio_code(directory):
    subprocess.run(["code", directory])


def load_file_in_visual_studio_code(file_path, line_number=None, project_directory=None):
    if project_directory:
        subprocess.run(["code", project_directory])


    if line_number is not None:
        subprocess.run(["code", "-g", f"{file_path}:{line_number}"])
    else:
        subprocess.run(["code", file_path])


def open_in_visual_studio_code(file_path, occurrences, last_choice, project_directory):
    occurrence_choice = last_choice.get("occurrence")

    if occurrence_choice == "v":
        occurrence_index = len(occurrences) - 1
    elif occurrence_choice is not None:
        occurrence_index = int(occurrence_choice) - 1
    else:
        occurrence_index = None

    if occurrence_index is not None and (occurrence_index < 0 or occurrence_index >= len(occurrences)):
        console.print("Invalid occurrence number. Please try again.")
        return

    if occurrence_index is None:
        line_number, _ = occurrences[0]
    else:
        line_number, _ = occurrences[occurrence_index]

    if project_directory is not None:
        subprocess.run(["code", project_directory, "--add"])

    if last_choice.get("file") is not None:
        load_file_in_visual_studio_code(file_path, line_number)
    elif occurrences:
        load_file_in_visual_studio_code(file_path, line_number)
    else:
        console.print("No occurrences found in the selected file.")


def generate_occurrences_tree(file_path, occurrences):
    tree = Tree(f":clipboard: Occurrences in {file_path}", guide_style="bright_blue")

    for index, (line_number, line) in enumerate(occurrences, start=1):
        tree.add(f"{index}. Line {line_number}: {line.strip()}")

    return tree

def print_occurrences_menu(file_path, occurrences, last_choice):
    if occurrences:
        occurrences_tree = generate_occurrences_tree(file_path, occurrences)
        console.print(occurrences_tree)
        console.print()
        console.print("Enter the number of the occurrence you want to inspect (or 0 to go back to the files menu):")
        console.print("v. Open in Visual Studio Code", style="yellow")
        console.print("h. Help", style="yellow")
        console.print(f"Last choice was: {last_choice.get('occurrence')}")
    else:
        console.print("No occurrences found in the selected file.")
        console.print()

def choose_occurrence(occurrences, last_choice):
    occurrence_choice = get_input_range(len(occurrences) + 1)
    if occurrence_choice != 'v':
        last_choice["occurrence"] = occurrence_choice

    return int(occurrence_choice) if occurrence_choice.isdigit() else occurrence_choice

def main():
    parser = argparse.ArgumentParser(description="Scan backend files for potential vulnerabilities")
    parser.add_argument("directory", help="The directory to scan")
    args = parser.parse_args()

    last_choice = {
        "language": None,
        "vulnerability": None,
        "file": None,
        "occurrence": None,
    }

    while True:
        language_tree = generate_language_tree()
        console.print(language_tree)
        console.print()

        language_choice = choose_language(last_choice)

        if language_choice == "0":
            break
        elif language_choice == "h":
            print_help_message()
            continue

        language = LANGUAGES[int(language_choice) - 1]

        while True:
            vulnerability_tree = generate_vulnerability_tree()
            console.print(vulnerability_tree)
            console.print()

            vulnerability_choice = choose_vulnerability(last_choice)

            if vulnerability_choice == "0":
                break
            elif vulnerability_choice == "h":
                print_help_message_vulnerability_menu()
                continue

            results = scan_files_for_vulnerability(args.directory, language, vulnerability_choice)

            files = list(results.keys())

            if not files:
                console.print(f"No {language} files found with the selected vulnerability in the specified directory.\n")
                continue

            while True:
                attack_type = list(VULNERABILITIES.keys())[int(vulnerability_choice) - 1]
                print_files_menu(attack_type, files, last_choice)

                file_choice = choose_file(files, last_choice)

                if file_choice == 0:
                    break
                elif file_choice == "h":
                    print_help_message_files_menu()
                    continue

                file_index = file_choice - 1

                if file_index < 0 or file_index >= len(files):
                    console.print("Invalid file number. Please try again.")
                    continue

                file_path = files[file_index]

                occurrences = results[file_path]

                while True:
                    print_occurrences_menu(file_path, occurrences, last_choice)

                    occurrence_choice = choose_occurrence(occurrences, last_choice)

                    if occurrence_choice == 0:
                        break
                    elif occurrence_choice == "h":
                        print_help_message_occurrences_menu()
                        continue
                    elif occurrence_choice == "v":
                        project_directory = args.directory if language == "Node.js" else None
                        open_in_visual_studio_code(file_path, occurrences, last_choice, args.directory)
                        continue

                    occurrence_index = occurrence_choice - 1
                    if occurrence_index < 0 or occurrence_index >= len(occurrences):
                        console.print("Invalid occurrence number. Please try again.")
                        continue

                    line_number, line = occurrences[occurrence_index]
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()
                    start, end = find_function(lines, line_number - 1)

                    print_code_details(file_path, line_number, line, lines, start, end)

if __name__ == "__main__":
    main()
