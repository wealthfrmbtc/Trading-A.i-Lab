"""
Tah Trading AI Lab
Status: Online
Purpose: Build trading tools, AI systems, and mastery
"""

def main():
    print("🧠 Tah Trading AI Lab is LIVE.")
    print("Select a tool:")
    print("1. Percent Return")
    print("2. PnL Calculator")
    print("3. Leverage Simulator")
    print("4. Trade Summary")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        print("Running Percent Return...")
    elif choice == "2":
        print("Running PnL Calculator...")
    elif choice == "3":
        print("Running Leverage Simulator...")
    elif choice == "4":
        print("Running Trade Summary...")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

