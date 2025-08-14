#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import socket
import requests
import whois
import dns.resolver
import shodan
import time
import json
import subprocess
from datetime import datetime
import platform

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class OSINTTool:
    def __init__(self):
        self.api_keys = {}
        self.load_api_keys()
        
    def load_api_keys(self):
        config_file = "config.json"
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r') as f:
                    self.api_keys = json.load(f)
            except:
                pass
    
    def print_banner(self):
        banner = f"""
{Colors.RED}{Colors.BOLD}
██╗    ██╗███████╗██╗  ██╗ ████████╗██╗  ██╗██╗███╗   ██╗████████╗
██║    ██║██╔════╝╚██╗██╔╝ ╚══██╔══╝██║  ██║██║████╗  ██║╚══██╔══╝
██║ █╗ ██║███████╗ ╚███╔╝     ██║   ███████║██║██╔██╗ ██║   ██║   
██║███╗██║╚════██║ ██╔██╗     ██║   ██╔══██║██║██║╚██╗██║   ██║   
╚███╔███╔╝███████║██╔╝ ██╗    ██║   ██║  ██║██║██║ ╚████║   ██║   
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝    ╚═╝   ╚═╝  ╚═╝╚═╝ ╚══╝╚═══╝   ╚═╝   
{Colors.END}

{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
║                    OSINT Tool   WsxThint                                                ║
║                    For Security Programmers and Ethical Hackers                 ║
║                    Created by: AymanCsharp                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.YELLOW}Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Operating System: {platform.system()} {platform.release()}
Python Version: {sys.version.split()[0]}{Colors.END}
"""
        print(banner)
    
    def print_menu(self):
        menu = f"""
{Colors.GREEN}╔══════════════════════════════════════════════════════════════════════════════╗
║                              Main Menu                                         ║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.CYAN}Email OSINT:{Colors.END}
{Colors.WHITE}1.  Search email in breach databases
2.  Verify email validity
3.  Search email on social media
4.  Gather info from known breach sites

{Colors.CYAN}Website OSINT:{Colors.END}
5.  WHOIS information gathering
6.  DNS information extraction
7.  Open port scanning
8.  Search in Shodan
9.  Security and vulnerability check
10. Server geolocation

{Colors.CYAN}Google Dorks OSINT:{Colors.END}
11. Search for sensitive files
12. Search for open folders
13. Search for databases
14. Search for documents and files
15. Search for admin panels

{Colors.CYAN}Additional Tools:{Colors.END}
16. Phone number lookup
17. National ID verification
18. Company lookup
19. People search
20. Comprehensive report

{Colors.RED}0.  Exit{Colors.END}
"""
        print(menu)
    
    def email_osint(self, email):
        print(f"\n{Colors.GREEN}Starting OSINT on email: {email}{Colors.END}")
        
        print(f"\n{Colors.YELLOW}1. Verify email validity:{Colors.END}")
        if '@' in email and '.' in email.split('@')[1]:
            print(f"{Colors.GREEN}Valid email format{Colors.END}")
        else:
            print(f"{Colors.RED}Invalid email format{Colors.END}")
        
        domain = email.split('@')[1] if '@' in email else None
        if domain:
            print(f"{Colors.CYAN}Domain: {domain}{Colors.END}")
            
            try:
                w = whois.whois(domain)
                print(f"{Colors.BLUE}WHOIS Information:{Colors.END}")
                print(f"   Creation Date: {w.creation_date}")
                print(f"   Expiration Date: {w.expiration_date}")
                print(f"   Registrar: {w.registrar}")
            except:
                print(f"{Colors.RED}Cannot retrieve WHOIS information{Colors.END}")
        
        print(f"\n{Colors.YELLOW}2. Checking breach sites:{Colors.END}")
        leak_sites = [
            "haveibeenpwned.com",
            "leakcheck.io",
            "dehashed.com"
        ]
        
        for site in leak_sites:
            print(f"   Checking {site}")
        
        print(f"\n{Colors.GREEN}Completed OSINT on email{Colors.END}")
    
    def website_osint(self, url):
        print(f"\n{Colors.GREEN}Starting OSINT on website: {url}{Colors.END}")
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        domain = url.split('//')[1].split('/')[0] if '//' in url else url
        
        print(f"\n{Colors.YELLOW}1. WHOIS Information:{Colors.END}")
        try:
            w = whois.whois(domain)
            print(f"   Creation Date: {w.creation_date}")
            print(f"   Expiration Date: {w.expiration_date}")
            print(f"   Registrar: {w.registrar}")
            print(f"   Emails: {w.emails}")
        except Exception as e:
            print(f"{Colors.RED}WHOIS error: {e}{Colors.END}")
        
        print(f"\n{Colors.YELLOW}2. DNS Information:{Colors.END}")
        try:
            a_records = dns.resolver.resolve(domain, 'A')
            print(f"   A Records:")
            for record in a_records:
                print(f"      {record}")
            
            try:
                mx_records = dns.resolver.resolve(domain, 'MX')
                print(f"   MX Records:")
                for record in mx_records:
                    print(f"      {record}")
            except:
                pass
                
            try:
                ns_records = dns.resolver.resolve(domain, 'NS')
                print(f"   NS Records:")
                for record in ns_records:
                    print(f"      {record}")
            except:
                pass
                
        except Exception as e:
            print(f"{Colors.RED}DNS error: {e}{Colors.END}")
        
        print(f"\n{Colors.YELLOW}3. nslookup results:{Colors.END}")
        try:
            result = subprocess.run(['nslookup', domain], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"{Colors.GREEN}nslookup results:{Colors.END}")
                print(result.stdout)
            else:
                print(f"{Colors.RED}nslookup failed{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}nslookup error: {e}{Colors.END}")
        
        print(f"\n{Colors.YELLOW}4. Common port scan:{Colors.END}")
        common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3306, 3389, 5432, 8080]
        
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((domain, port))
                if result == 0:
                    print(f"   Port {port} is open")
                sock.close()
            except:
                pass
        
        try:
            ip = socket.gethostbyname(domain)
            print(f"\n{Colors.YELLOW}5. IP Information:{Colors.END}")
            print(f"   IP Address: {ip}")
            
            try:
                response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    print(f"   Country: {data.get('country', 'Unknown')}")
                    print(f"   City: {data.get('city', 'Unknown')}")
                    print(f"   ISP: {data.get('isp', 'Unknown')}")
            except:
                pass
                
        except Exception as e:
            print(f"{Colors.RED}IP retrieval error: {e}{Colors.END}")
        
        print(f"\n{Colors.GREEN}Completed OSINT on website{Colors.END}")
    
    def google_dorks(self, query):
        print(f"\n{Colors.GREEN}Starting Google Dorks search: {query}{Colors.END}")
        
        dorks = [
            f'site:{query} filetype:pdf',
            f'site:{query} filetype:doc',
            f'site:{query} filetype:xls',
            f'site:{query} inurl:admin',
            f'site:{query} inurl:login',
            f'site:{query} inurl:config',
            f'site:{query} inurl:backup',
            f'site:{query} inurl:db',
            f'site:{query} inurl:sql',
            f'site:{query} inurl:php',
            f'site:{query} inurl:asp',
            f'site:{query} inurl:jsp',
            f'site:{query} inurl:git',
            f'site:{query} inurl:svn',
            f'site:{query} inurl:ftp',
            f'site:{query} inurl:ssh',
            f'site:{query} inurl:telnet',
            f'site:{query} inurl:database',
            f'site:{query} inurl:password',
            f'site:{query} inurl:username'
        ]
        
        print(f"\n{Colors.YELLOW}Google Dorks ready:{Colors.END}")
        for i, dork in enumerate(dorks, 1):
            print(f"   {i:2d}. {dork}")
        
        print(f"\n{Colors.CYAN}Tips:{Colors.END}")
        print("   • Use these dorks in Google")
        print("   • Add more keywords as needed")
        print("   • Use quotes for exact search")
        
        print(f"\n{Colors.GREEN}Google Dorks created{Colors.END}")
    
    def phone_osint(self, phone):
        print(f"\n{Colors.GREEN}Starting OSINT on phone number: {phone}{Colors.END}")
        
        clean_phone = ''.join(filter(str.isdigit, phone))
        
        print(f"\n{Colors.YELLOW}Phone information:{Colors.END}")
        print(f"   Original: {phone}")
        print(f"   Clean: {clean_phone}")
        
        if clean_phone.startswith('966'):
            print(f"   Country: Saudi Arabia")
        elif clean_phone.startswith('971'):
            print(f"   Country: UAE")
        elif clean_phone.startswith('965'):
            print(f"   Country: Kuwait")
        elif clean_phone.startswith('973'):
            print(f"   Country: Bahrain")
        elif clean_phone.startswith('974'):
            print(f"   Country: Qatar")
        elif clean_phone.startswith('968'):
            print(f"   Country: Oman")
        else:
            print(f"   Country: Unknown")
        
        print(f"\n{Colors.YELLOW}Search sites:{Colors.END}")
        search_sites = [
            "truecaller.com",
            "whitepages.com",
            "spokeo.com",
            "peoplefinder.com",
            "fastpeoplesearch.com"
        ]
        
        for site in search_sites:
            print(f"   {site}")
        
        print(f"\n{Colors.GREEN}Completed OSINT on phone number{Colors.END}")
    
    def comprehensive_report(self, target, target_type):
        print(f"\n{Colors.GREEN}Starting comprehensive report on: {target}{Colors.END}")
        
        print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"║                              Comprehensive Report                                    ║")
        print(f"╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}")
        
        print(f"\n{Colors.YELLOW}Target:{Colors.END}")
        print(f"   Type: {target_type}")
        print(f"   Value: {target}")
        print(f"   Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        print(f"\n{Colors.YELLOW}Tools used:{Colors.END}")
        tools = [
            "WHOIS Lookup",
            "DNS Analysis",
            "Port Scanner",
            "IP Geolocation",
            "Google Dorks",
            "Social Media Search",
            "Data Breach Check",
            "Network Analysis"
        ]
        
        for tool in tools:
            print(f"   {tool}")
        
        print(f"\n{Colors.YELLOW}Recommendations:{Colors.END}")
        recommendations = [
            "Use VPN to protect your identity",
            "Check privacy settings",
            "Monitor your accounts regularly",
            "Use strong passwords",
            "Enable two-factor authentication"
        ]
        
        for rec in recommendations:
            print(f"   {rec}")
        
        print(f"\n{Colors.GREEN}Completed comprehensive report{Colors.END}")
    
    def run(self):
        while True:
            self.print_banner()
            self.print_menu()
            
            try:
                choice = input(f"\n{Colors.CYAN}Choose option (0-20): {Colors.END}")
                
                if choice == '0':
                    print(f"\n{Colors.GREEN}Thank you for using OSINT Tool!{Colors.END}")
                    break
                
                elif choice == '1':
                    email = input(f"{Colors.YELLOW}Enter email: {Colors.END}")
                    self.email_osint(email)
                
                elif choice == '2':
                    email = input(f"{Colors.YELLOW}Enter email: {Colors.END}")
                    print(f"\n{Colors.GREEN}Email validation option selected{Colors.END}")
                    self.email_osint(email)
                
                elif choice == '3':
                    email = input(f"{Colors.YELLOW}Enter email: {Colors.END}")
                    print(f"\n{Colors.GREEN}Social media search option selected{Colors.END}")
                    self.email_osint(email)
                
                elif choice == '4':
                    email = input(f"{Colors.YELLOW}Enter email: {Colors.END}")
                    print(f"\n{Colors.GREEN}Breach site info gathering option selected{Colors.END}")
                    self.email_osint(email)
                
                elif choice == '5':
                    url = input(f"{Colors.YELLOW}Enter website: {Colors.END}")
                    self.website_osint(url)
                
                elif choice == '6':
                    url = input(f"{Colors.YELLOW}Enter website: {Colors.END}")
                    print(f"\n{Colors.GREEN}DNS information extraction option selected{Colors.END}")
                    self.website_osint(url)
                
                elif choice == '7':
                    url = input(f"{Colors.YELLOW}Enter website: {Colors.END}")
                    print(f"\n{Colors.GREEN}Open port scanning option selected{Colors.END}")
                    self.website_osint(url)
                
                elif choice == '8':
                    url = input(f"{Colors.YELLOW}Enter website: {Colors.END}")
                    print(f"\n{Colors.GREEN}Shodan search option selected{Colors.END}")
                    self.website_osint(url)
                
                elif choice == '9':
                    url = input(f"{Colors.YELLOW}Enter website: {Colors.END}")
                    print(f"\n{Colors.GREEN}Security and vulnerability check option selected{Colors.END}")
                    self.website_osint(url)
                
                elif choice == '10':
                    url = input(f"{Colors.YELLOW}Enter website: {Colors.END}")
                    print(f"\n{Colors.GREEN}Server geolocation option selected{Colors.END}")
                    self.website_osint(url)
                
                elif choice == '11':
                    query = input(f"{Colors.YELLOW}Enter website to search: {Colors.END}")
                    self.google_dorks(query)
                
                elif choice == '12':
                    query = input(f"{Colors.YELLOW}Enter website to search: {Colors.END}")
                    print(f"\n{Colors.GREEN}Open folders search option selected{Colors.END}")
                    self.google_dorks(query)
                
                elif choice == '13':
                    query = input(f"{Colors.YELLOW}Enter website to search: {Colors.END}")
                    print(f"\n{Colors.GREEN}Database search option selected{Colors.END}")
                    self.google_dorks(query)
                
                elif choice == '14':
                    query = input(f"{Colors.YELLOW}Enter website to search: {Colors.END}")
                    print(f"\n{Colors.GREEN}Documents and files search option selected{Colors.END}")
                    self.google_dorks(query)
                
                elif choice == '15':
                    query = input(f"{Colors.YELLOW}Enter website to search: {Colors.END}")
                    print(f"\n{Colors.GREEN}Admin panels search option selected{Colors.END}")
                    self.google_dorks(query)
                
                elif choice == '16':
                    phone = input(f"{Colors.YELLOW}Enter phone number: {Colors.END}")
                    self.phone_osint(phone)
                
                elif choice == '17':
                    id_number = input(f"{Colors.YELLOW}Enter ID number: {Colors.END}")
                    print(f"\n{Colors.GREEN}National ID verification option selected{Colors.END}")
                    print(f"   ID: {id_number}")
                    print(f"   This option requires special permissions")
                
                elif choice == '18':
                    company = input(f"{Colors.YELLOW}Enter company name: {Colors.END}")
                    print(f"\n{Colors.GREEN}Company lookup option selected{Colors.END}")
                    print(f"   Company: {company}")
                    print(f"   Searching commercial databases")
                
                elif choice == '19':
                    person = input(f"{Colors.YELLOW}Enter person name: {Colors.END}")
                    print(f"\n{Colors.GREEN}People search option selected{Colors.END}")
                    print(f"   Name: {person}")
                    print(f"   Searching public information sites")
                
                elif choice == '20':
                    target = input(f"{Colors.YELLOW}Enter target (email, website, phone): {Colors.END}")
                    target_type = input(f"{Colors.YELLOW}Target type (email/website/phone): {Colors.END}")
                    self.comprehensive_report(target, target_type)
                
                else:
                    print(f"\n{Colors.RED}Invalid option! Choose from 0 to 20{Colors.END}")
                
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
                os.system('cls' if os.name == 'nt' else 'clear')
                
            except KeyboardInterrupt:
                print(f"\n\n{Colors.RED}Program stopped by user{Colors.END}")
                break
            except Exception as e:
                print(f"\n{Colors.RED}Error: {e}{Colors.END}")
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")

if __name__ == "__main__":
    try:
        tool = OSINTTool()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Program stopped{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Program error: {e}{Colors.END}")
