#!/usr/bin/env python3
"""
My first Python script on Raspberry Pi
This script demonstrates basic Python syntax
"""

def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}! Welcome to Raspberry Pi development."

def main():
    """Main function"""
    print("=" * 50)
    print("Weather Station Project - Day 1")
    print("=" * 50)

    user_name = input("Enter your name: ")
    greeting = greet(user_name)
    print(greeting)

    print("\nPython version check:")
    import sys
    print(f"Python {sys.version}")

    print("\nEnvironment check:")
    import os
    print(f"Current directory: {os.getcwd()}")
    print(f"Home directory: {os.path.expanduser('~')}")

    print("\n✓ Your Python environment is working correctly!")

if __name__ == "__main__":
    main()
