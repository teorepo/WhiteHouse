# WhiteHouse Vulnerability Scanner

A command-line Python utility for scanning source code directories and identifying potentially vulnerable function calls. The script checks for a wide range of security pitfalls, such as SQL Injection and Path Traversal, across multiple languages (Python, Java, C#, PHP, Node.js). It helps developers and testers rapidly isolate and inspect high-risk code segments.

---

## Key Features

1. Multi-Language Support  
   Automatically parses source code for five popular programming languages:  
   - Python  
   - Java  
   - C#  
   - PHP  
   - Node.js  

2. Vulnerability Detection  
   Flags common security risks, including:  
   - SQL Injection  
   - Path Traversal  
   - Server-Side Request Forgery (SSRF)  
   - Command Injection  
   - Insecure Deserialization  
   - XML External Entity (XXE)  
   - Server-Side Template Injection (SSTI)  
   - Open Redirect  

3. Interactive CLI  
   Guides you through each step to choose a language, select specific vulnerabilities, inspect files, and jump directly to flagged code lines in Visual Studio Code.

4. Rich Console Output  
   Uses [Rich](https://github.com/Textualize/rich) for enhanced terminal visuals—making file trees, vulnerabilities, and menu options easier to navigate.

5. IDE Integration  
   Integrates with Visual Studio Code via command-line calls, so you can open entire projects or specific lines of flagged code instantly.

---

## Requirements & Installation

- Python 3.7+  
- Rich  
- Colorama  

Install Rich and Colorama manually:
```bash
pip install rich colorama
```

After that, simply clone the repository (or place the script in a directory of your choice) and run it.

---

## Usage

1. Basic Command
   ```bash
   python whitehouse_scanner.py <directory>
   ```
   - `<directory>`: The root folder you want to scan for vulnerable code.

2. Language Menu  
   You’ll see a list of available programming languages. Enter the corresponding number to pick one, or `0` to exit.

3. Vulnerability Menu  
   After choosing a language, select a specific vulnerability you want to scan for (e.g., SQL Injection, Path Traversal). Enter its number or `0` to go back.

4. File Inspection  
   Once the script identifies files that contain suspicious function calls, you can:
   - Enter the file’s number to inspect occurrences in detail.  
   - Press `0` to move back to the vulnerabilities menu.  

5. Occurrences & Visual Studio Code  
   For each flagged file, the script displays:
   - Line number  
   - Code snippet  

   You can choose a specific occurrence by number to see more context or select `v` to open the file at the highlighted line in Visual Studio Code.

---

## Example

1. Scan Your `src` Folder for Vulnerabilities  
   ```bash
   python whitehouse_scanner.py src
   ```
2. Pick `1` for Python (or whichever language your code is in).  
3. Pick `1` for SQL Injection (or any other vulnerability).  
4. Review Flagged Files in the console.  
5. Select the File and a specific line occurrence to see surrounding code.  
6. Press `v` to open the suspicious line in VSCode.

---

## Project Structure

```
whitehouse-scanner/
│
├─ utils.py
├─ vulnerable_functions.py
├─ whitehouse_scanner.py      # Main script
└─ README.md                  # You are here!
```

---

## Known Limitations

- Language-Specific Variations  
  While the script covers general function calls (e.g., `exec()` in Python), more advanced or framework-specific vulnerability patterns may not be included.  

- False Positives  
  The tool flags suspicious function usage but cannot guarantee that user input truly flows into those functions unsanitized.  

- Limited Code Parsing  
  Dynamic code constructs or custom templating engines might be missed, especially if they rely on advanced meta-programming.

---

## Contributing

1. Fork this repo and create a new feature branch.  
2. Enhance detection logic in `vulnerable_functions.py` or improve CLI flows in the main script.  
3. Submit a Pull Request describing your changes in detail.

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this tool under the terms specified.

---

## Contact

For questions, issues, or suggestions, please open an Issue or reach out to the project maintainer:

- Author: [Malachias Theodoros](mailto:malachiasth@gmail.com)  
- GitHub: [github.com/teorepo](https://github.com/teorepo)

---

> Disclaimer: This tool is intended for educational and testing purposes only. Always ensure you have explicit permission before scanning a system’s source code. The maintainers assume no responsibility for misuse.
