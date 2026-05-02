import sys
import os
import time

# Function to clear screen
def clear():
    os.system("clear" if os.name == "posix" else "cls")

# Check if cc.so exists and fix naming if necessary
def prepare_module():
    if not os.path.exists("cc.so"):
        found = False
        for file in os.listdir("."):
            if file.startswith("cc.cpython") and file.endswith(".so"):
                os.rename(file, "cc.so")
                found = True
                break
        
        if not found:
            print("\033[1;31m[!] Error: 'cc.so' module not found!\033[0m")
            print("\033[1;33m[*] Please compile cc.py using Cython first.\033[0m")
            sys.exit(1)

def start_program():
    try:
        # Import the compiled .so module
        import cc
        
        # Calling the main function from cc.so
        # Note: Ensure your main function in cc.py is named main_menu()
        cc.main_menu()
        
    except ImportError as e:
        print(f"\033[1;31m[!] Failed to import cc.so: {e}\033[0m")
    except AttributeError:
        print("\033[1;31m[!] Error: function 'main_menu' not found in cc.so\033[0m")
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Program stopped by user.\033[0m")
        sys.exit()
    except Exception as e:
        print(f"\033[1;31m[!] Unexpected Error: {e}\033[0m")

if __name__ == "__main__":
    prepare_module()
    start_program()

