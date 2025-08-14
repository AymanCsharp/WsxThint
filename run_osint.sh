#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                       WsxThint < Osint Tool >                                ║"
echo "║                      For Security Programmers and Ethical Hackers            ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

echo -e "${YELLOW}Checking requirements...${NC}"

if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo -e "${RED}Python is not installed!${NC}"
        echo -e "${YELLOW}Please install Python 3.7 or higher${NC}"
        echo -e "${BLUE}Ubuntu/Debian: sudo apt install python3 python3-pip${NC}"
        echo -e "${BLUE}CentOS/RHEL: sudo yum install python3 python3-pip${NC}"
        echo -e "${BLUE}macOS: brew install python3${NC}"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo -e "${GREEN}Python is installed${NC}"

if ! command -v pip3 &> /dev/null; then
    if ! command -v pip &> /dev/null; then
        echo -e "${RED}pip is not installed!${NC}"
        echo -e "${YELLOW}Please install pip${NC}"
        exit 1
    else
        PIP_CMD="pip"
    fi
else
    PIP_CMD="pip3"
fi

echo -e "${GREEN}pip is installed${NC}"

echo
echo -e "${YELLOW}Installing requirements...${NC}"

$PIP_CMD install -r requirements.txt

if [ $? -ne 0 ]; then
    echo -e "${YELLOW}Warning: Some requirements failed to install${NC}"
    echo -e "${CYAN}The tool might work with limited functionality${NC}"
    echo
fi

echo
echo -e "${GREEN}Starting the tool...${NC}"
echo

$PYTHON_CMD osint_tool.py

echo
echo -e "${GREEN}Thank you for using OSINT Tool!${NC}"
