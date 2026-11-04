# Phishing URL Awareness Checker – Test Report

## Project Information
- **Project:** Phishing URL Awareness Checker
- **Language:** Python
- **Testing:** Manual testing using sample URLs
- **Result:** All 5 test cases passed

## Test Cases

| Test | Input URL | Expected Result | Actual Result |
|---|---|---|---|
| 1 | https://www.example.com/login | No warning signs | Passed |
| 2 | http://192.0.2.10/account | IP address and HTTP warnings | Passed |
| 3 | http://example.com@sample.invalid/login | @ symbol and HTTP warnings | Passed |
| 4 | https://a.b.c.d.e.example.invalid/path | Long hostname warning | Passed |
| 5 | https://xn--example.invalid/ | Punycode warning | Passed |

## Conclusion

All five test cases were executed successfully. The program detected the selected URL warning signs and displayed explanations for suspicious patterns.

**Note:** This is an educational, text-based checker. It does not open URLs and cannot guarantee that a URL is safe.