import re
from urllib.parse import urlparse
def inspect_url(raw_url):

    warnings = []

    # Parse the URL
    parsed = urlparse(raw_url)

    # Check 1: @ symbol
    if "@" in raw_url:
        warnings.append("URL contains @ symbol")

    # Check 2: URL length
    if len(raw_url) > 100:
        warnings.append("URL length is greater than 100 characters")

    # Check 3: IP address in hostname
    hostname = parsed.hostname or ""

    ip_pattern = r"(?:\d{1,3}\.){3}\d{1,3}"

    if re.search(ip_pattern, hostname):
        warnings.append("URL contains an IP address")

    # Check 4: Number of hostname labels
    if len(hostname.split(".")) >= 5:
        warnings.append("Hostname contains 5 or more labels")

    # Check 5: Punycode
    if "xn--" in hostname:
        warnings.append("Hostname contains punycode")

    # Check 6: HTTP protocol
    if parsed.scheme.lower() == "http":
        warnings.append("URL uses HTTP instead of HTTPS")
    return warnings
    
def main():

    print("=" * 50)
    print("       PHISHING URL AWARENESS CHECKER")
    print("=" * 50)

    checked_count = 0
    flagged_count = 0

    while True:

        raw_url = input("\nEnter a URL (or type 'q' to quit): ").strip()

        # Exit condition
        if raw_url.lower() in ["q", "quit", "exit"]:
            break

        if not raw_url:
            print("Please enter a URL.")
            continue

        try:
            parsed = urlparse(raw_url)

            if not parsed.scheme or not parsed.netloc:
                print("Invalid URL format. Include https:// or http://")
                continue

            warnings = inspect_url(raw_url)

            checked_count += 1

            print("\n----- SCAN RESULT -----")

            if warnings:
                flagged_count += 1
                print("Status: SUSPICIOUS")
                print("Warning signs detected:")

                for warning in warnings:
                    print("- " + warning)

            else:
                print("Status: NO LISTED WARNING SIGNS")
                print("No warning signs from the six checks were detected.")

            print("-----------------------")

        except ValueError:
            print("Invalid URL. Please try again.")

    print("\n========== SUMMARY ==========")
    print("Total URLs checked:", checked_count)
    print("URLs with warning signs:", flagged_count)
    print("=============================")
    print("Thank you for using the checker!")


if __name__ == "__main__":
    main()