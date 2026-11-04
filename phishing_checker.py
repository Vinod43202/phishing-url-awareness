
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check URL text for selected phishing warning signs."""

    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["Invalid URL format. Please check your input."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append(
            ("URL contains @ symbol",
             "The @ symbol can hide the actual destination.")
        )

    if len(url) > 100:
        findings.append(
            ("URL is unusually long",
             "Long URLs may hide suspicious information.")
        )

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            ("URL contains an IP address",
             "The hostname uses a numeric IP instead of a domain name.")
        )

    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append(
            ("Hostname contains 5 or more labels",
             "Multiple hostname sections can make a link confusing.")
        )

    if "xn--" in host:
        findings.append(
            ("Hostname contains punycode",
             "Punycode can represent look-alike characters.")
        )

    if parsed.scheme.lower() == "http":
        findings.append(
            ("URL uses HTTP instead of HTTPS",
             "HTTP does not encrypt the connection.")
        )

    return findings


def main():

    print("=" * 45)
    print("       PHISHING URL AWARENESS CHECKER")
    print("=" * 45)
    print("Text-based checking only. URLs are not opened.")

    while True:

        url = input("\nEnter URL (or q to quit): ")

        if url.strip().lower() in ("q", "quit", "exit"):
            print("\nThank you for using the checker!")
            break

        findings = inspect_url(url)

        print("\n--- SCAN RESULT ---")

        if findings and isinstance(findings[0], tuple):

            print("Status: SUSPICIOUS")
            print("Warning signs detected:", len(findings))

            for number, (warning, explanation) in enumerate(findings, 1):
                print(f"\n{number}. {warning}")
                print("   Explanation:", explanation)

        else:
            print("Status: REVIEW INPUT")
            for item in findings:
                print("-", item)

        if not findings:
            print("No listed warning signs found.")
            print("This does NOT prove the URL is safe.")

        print("\nAlways verify website addresses before sharing information.")


if __name__ == "__main__":
    main()
