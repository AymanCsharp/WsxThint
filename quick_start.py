#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

def check_python():
    try:
        version = sys.version_info
        if version.major >= 3 and version.minor >= 7:
            print("Python 3.7+ is installed")
            return True
        else:
            print(f"Python {version.major}.{version.minor} is installed")
            print("Python 3.7+ or higher is required")
            return False
    except:
        print("Python is not installed")
        return False

def install_requirements():
    print("Installing requirements...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True)
        print("Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install requirements: {e}")
        return False

def run_tool():
    print("Running OSINT Tool...")
    try:
        subprocess.run([sys.executable, "osint_tool.py"])
    except KeyboardInterrupt:
        print("\nTool stopped by user")
    except Exception as e:
        print(f"Error running the tool: {e}")

def main():
    print("OSINT Tool - Quick Start")
    print("=" * 40)
    
    if not check_python():
        return
    
    if not install_requirements():
        print("The tool may run with limited functionality")
    
    run_tool()

if __name__ == "__main__":
    main()

