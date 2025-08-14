
---
# WsxThint Tool - Open Source Intelligence Tool

## Tool Description

A powerful and comprehensive OSINT tool specifically designed for cybersecurity professionals and ethical hackers. Contains 20 advanced options for gathering information from open sources.

## Main Features

### Email OSINT

* Search for email in data breach sites
* Email validation
* Social media search
* Information gathering from known breach sites

### Website OSINT

* WHOIS information gathering
* DNS information extraction
* Open port scanning
* Shodan search
* Security and vulnerability scanning
* Server geolocation

### Google Dorks

* Search for sensitive files
* Search for open directories
* Search for databases
* Search for documents and files
* Search for admin panels

### Additional Tools

* Phone number scanning
* National ID verification
* Company search
* Person search
* Comprehensive report

## Installation and Usage

### Basic Requirements

* Python 3.7+
* pip
* Windows/Linux/macOS operating system

### Installation Steps

1. **Clone the project**

```bash
git clone <repository-url>
cd Blarys
```

2. **Install requirements**

```bash
pip install -r requirements.txt
```

3. **Run the tool**

```bash
python osint_tool.py
```

## How to Use

1. Run the tool

```bash
python osint_tool.py
```

2. Choose the desired option

* Select a number from 1 to 20 according to the required service
* Follow the on-screen instructions
* Enter the required data

3. Review results

* Results will appear in colored and organized format
* Press Enter to continue
* Select 0 to exit

## Available Options

| Number | Service               | Description                   |
| ------ | --------------------- | ----------------------------- |
| 1      | Email Search          | Search in data breach sites   |
| 2      | Email Validation      | Email format validation       |
| 3      | Social Search         | Search in social media        |
| 4      | Information Gathering | Information from breach sites |
| 5      | WHOIS Info            | Domain registration data      |
| 6      | DNS Info              | Various DNS records           |
| 7      | Port Scan             | Open port scanning            |
| 8      | Shodan Search         | Information from Shodan       |
| 9      | Security Scan         | Vulnerability scanning        |
| 10     | Geolocation           | Server location               |
| 11     | Sensitive Files       | Google Dorks for files        |
| 12     | Open Directories      | Search for directories        |
| 13     | Databases             | Search in databases           |
| 14     | Documents             | Search for documents          |
| 15     | Admin Panels          | Search for control panels     |
| 16     | Phone Scan            | Phone number information      |
| 17     | ID Verification       | National ID information       |
| 18     | Company Search        | Company information           |
| 19     | Person Search         | Person information            |
| 20     | Comprehensive Report  | Comprehensive target report   |

## Important Warnings

### Ethical Use

* Use this tool for legal purposes only
* Respect others' privacy
* Do not use for criminal activities

### Protection

* Use VPN to protect your identity
* Do not share sensitive information
* Keep API keys secure

## Security Requirements

### Required API Keys

* Shodan API Key (optional)
* HaveIBeenPwned API Key (optional)
* Other sites (optional)

### Configuration File

```json
{
    "shodan_api": "your_shodan_key",
    "hibp_api": "your_hibp_key"
}
```

## Troubleshooting

### Common Issues

1. Library errors

```bash
pip install --upgrade -r requirements.txt
```

2. Color issues

* Ensure Terminal supports colors
* Use `colorama` on Windows

3. DNS issues

* Check internet connection
* Verify DNS settings

## Sources and References

* [OSINT Framework](https://osintframework.com/)
* [Shodan Documentation](https://developer.shodan.io/)
* [Google Dorks](https://www.exploit-db.com/google-hacking-database)
* [DNS Security](https://dnssec-analyzer.verisignlabs.com/)

## Contributing

We welcome contributions! Please:

1. Fork the project
2. Create a new branch
3. Add features
4. Send Pull Request

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Developer

Cybersecurity Expert

* Cybersecurity specialist
* OSINT expert
* Python developer


---

**Warning**: This tool is for educational and defensive purposes only. Use responsibly!

---

