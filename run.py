import sys
import os

try:
    # Importing the compiled .so module
    import xx
    
    if __name__ == "__main__":
        try:
            # Execute the main function from the .so file
            xx.main_menu()
        except AttributeError:
            print("\033[1;31m[!] Error: Function 'main_menu' not found in xx.so\033[1;00m")
        except KeyboardInterrupt:
            sys.exit()
            
except ImportError:
    print("\033[1;31m[!] Error: 'xx.so' file not found. Please build it first.\033[1;00m")
except Exception as e:
    print(f"\033[1;31m[!] Unexpected Error: {e}\033[1;00m")
    
