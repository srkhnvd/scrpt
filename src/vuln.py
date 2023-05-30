import requests

def check_security_headers(url):
    response = requests.get(url)
    headers = response.headers

    # Define the required security headers
    required_headers = [
        'Content-Security-Policy',
        'Strict-Transport-Security',
        'X-XSS-Protection',
        'X-Content-Type-Options',
        'X-Frame-Options'
    ]

    print(f"Scanning website: {url}\n")

    for header in required_headers:
        if header in headers:
            print(f"{header}: {headers[header]}")
        else:
            print(f"{header} header not found")

# Usage example
website_url = input("Enter the URL of the website to scan: ")
check_security_headers(website_url)

