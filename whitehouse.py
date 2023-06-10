import argparse
import subprocess
from rich.console import Console
from rich.tree import Tree
from utils import *
from vulnerable_functions import *
import colorama

colorama.init()
console = Console()


def generate_vulnerability_tree():
    tree = Tree(":fire: Vulnerabilities Menu", guide_style="bright_blue")

    branches = [
        ("Open Redirect", "🔄"),  # Use the repeat icon to signify redirection
        ("SQL Injection", "💉"),  # A needle for injection
        ("Local File Inclusion (LFI)", "📁"),  # A folder to represent files
        ("Remote Code Execution (RCE)", "🚀"),  # A rocket for executing
        ("Server Side Template Injection (SSTI)", "🎯"),  # Target symbol for injection
        ("PHP Object Injection (POI)", "🧪"),  # Test tube to represent a sort of 'injection'
        ("XML External Entity (XXE)", "📜"),  # A scroll to represent XML
        ("Server-Side Request Forgery (SSRF)", "🔁"),  # A return arrow can represent the request forgery
        ("Cross-Site Scripting (XSS)", "👾"),  # An alien symbol for the 'foreign' script
        ("Privilege Escalation", "🎢"),  # Roller coaster, because why not? It's an escalation!
        ("Exit", "🚪"),  # Door symbol is quite relevant for exit
        ("Help", "🆘"),  # SOS signal for help
    ]

    for index, (name, icon) in enumerate(branches, start=1):  # Start index from 1
        tree.add(f"{index}. {name} [{icon}]")

    return tree


def choose_vulnerability(last_choice):
    console.print(f"Last choice was: {last_choice.get('vulnerability')}")

    vulnerability_choice = get_input(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "h"])
    last_choice["vulnerability"] = vulnerability_choice

    return vulnerability_choice


def scan_directory(directory, vulnerability_choice):
    if vulnerability_choice == "1":
        return scan_files(directory, open_redirect_functions)
    elif vulnerability_choice == "2":
        return scan_files(directory, sqli_functions, remove_prepare=True)
    elif vulnerability_choice == "3":
        return scan_files(directory, lfi_functions)
    elif vulnerability_choice == "4":
        return scan_files(directory, rce_functions)
    elif vulnerability_choice == "5":
        return scan_files(directory, ssti_functions)
    elif vulnerability_choice == "6":
        return scan_files(directory, poi_functions)
    elif vulnerability_choice == "7":
        return scan_files(directory, xxe_functions)
    elif vulnerability_choice == "8":
        return scan_files(directory, ssrf_functions)
    elif vulnerability_choice == "9":
        return scan_files(directory, xss_functions, mode='xss')
    elif vulnerability_choice == "10":
        return scan_files(directory, auth_functions)
    else:
        console.print("Invalid vulnerability type choice.")
        return {}


def generate_files_tree(attack_type, files):
    tree = Tree(f":file_folder: Files possibly vulnerable to {attack_type}", guide_style="bright_blue")

    for index, file in enumerate(files, start=1):  # Start index from 1
        tree.add(f"{index}. {file}")

    return tree


def print_files_menu(attack_type, files, last_choice):
    files_tree = generate_files_tree(attack_type, files)
    console.print(files_tree)
    console.print()

    console.print("Enter the number of the file you want to inspect (or 0 to go back to the vulnerabilities menu):")
    console.print("h. Help", style="yellow")

    console.print(f"Last choice was: {last_choice.get('file')}")


def choose_file(files, last_choice):
    file_choice = get_input_range(len(files) + 1)
    last_choice["file"] = file_choice
    return int(file_choice) if file_choice.isdigit() else file_choice


def generate_occurrences_tree(file_path, occurrences):
    tree = Tree(f":clipboard: Occurrences in {file_path}", guide_style="bright_blue")

    for index, (line_number, line) in enumerate(occurrences, start=1):  # Start index from 1
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
    if(occurrence_choice!='v'):
        last_choice["occurrence"] = occurrence_choice
    return int(occurrence_choice) if occurrence_choice.isdigit() else occurrence_choice


def load_file_in_visual_studio_code(file_path, line_number=None):
    if line_number is not None:
        subprocess.run(["code", "-g", f"{file_path}:{line_number}"])
    else:
        subprocess.run(["code", file_path])


def open_in_visual_studio_code(file_path, occurrences, last_choice):
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

    if last_choice.get("file") is not None:
        load_file_in_visual_studio_code(file_path, line_number)
    elif occurrences:
        load_file_in_visual_studio_code(file_path, line_number)
    else:
        console.print("No occurrences found in the selected file.")


def main():
    parser = argparse.ArgumentParser(description="Scan PHP files for potential vulnerabilities")
    parser.add_argument("directory", help="The directory to scan")
    args = parser.parse_args()

    last_choice = {
        "vulnerability": None,
        "file": None,
        "occurrence": None,
    }

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

        vulnerability_map = {
            "1": "Open Redirect",
            "2": "SQL Injection",
            "3": "Local File Inclusion (LFI)",
            "4": "Remote Code Execution (RCE)",
            "5": "Server Side Template Injection (SSTI)",
            "6": "PHP Object Injection (POI)",
            "7": "XML External Entity (XXE)",
            "8": "Server-Side Request Forgery (SSRF)",
            "9": "Cross-Site Scripting (XSS)",
            "10": "Privilege Escalation",
        }

        attack_type = vulnerability_map.get(vulnerability_choice)
        if not attack_type:
            console.print("Invalid vulnerability type choice.")
            continue

        results = scan_directory(args.directory, vulnerability_choice)

        files = list(results.keys())

        if not files:
            console.print("No PHP files found in the specified directory.")
            continue

        while True:
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
                    print_help_message_occurrences_menu(attack_type)
                    continue
                elif occurrence_choice == "v":
                    open_in_visual_studio_code(file_path, occurrences, last_choice)
                    continue

                occurrence_index = occurrence_choice - 1
                if occurrence_index < 0 or occurrence_index >= len(occurrences):
                    console.print("Invalid occurrence number. Please try again.2")
                    continue

                line_number, line = occurrences[occurrence_index]
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                start, end = find_function(lines, line_number - 1)

                print_code_details(file_path, line_number, line, lines, start, end)


if __name__ == "__main__":
    main()
