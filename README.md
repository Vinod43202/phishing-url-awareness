# Phishing URL Awareness Checker

## 1. Project Description
The Phishing URL Awareness Checker is a Python-based educational project that identifies selected suspicious patterns in URLs.

It helps users understand common phishing warning signs before visiting unfamiliar websites.

## 2. Objectives
- Identify URLs containing IP addresses.
- Detect the use of HTTP instead of HTTPS.
- Identify URLs containing the @ symbol.
- Detect unusually long hostnames.
- Identify punycode in hostnames.
- Display warnings with explanations.

## 3. Technologies Used
- Programming Language: Python
- Modules: re, urllib.parse
- IDE/Editor: Visual Studio Code or any text editor
- Operating System: Windows

## 4. Project Structure
```text
phishing-url-awareness/
├── phishing_checker.py
├── requirements.txt
├── README.md
├── screenshots/
│   ├── sample_run.png
│   ├── test_results1.png
│   └── test_results2.png
└── tests/
    └── test_samples.md
```

## 5. How to Run the Project

1. Install Python 3.
2. Open PowerShell in the project folder.
3. Run:

```bash
python phishing_checker.py
```

4. Enter a URL when prompted.
5. Read the warning signs and explanations.
6. Enter `q` to exit.

## 6. Testing
The program was tested using five sample URLs.

All five test cases passed successfully.

Refer to the `tests/test_samples.md` file for the test report.

## 7. Screenshots
The screenshots folder contains:
- sample_run.png – Sample suspicious URL output.
- test_results1.png – First set of test results.
- test_results2.png – Remaining test results.

## 8. Limitations
- This project checks URL text only.
- It does not open or visit URLs.
- It does not use a live phishing database.
- It cannot guarantee that a URL is safe.

## 9. Conclusion
The project demonstrates how Python can identify selected phishing-related URL patterns and educate users about suspicious links.