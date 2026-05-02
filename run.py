import os
import sys

# လက်ရှိ folder ထဲက .so ဖိုင်ကို ရှာပြီး import လုပ်မယ်
try:
    import main
    if __name__ == "__main__":
        main.main_menu() # သင့် script ရဲ့ main function ကို လှမ်းခေါ်တာ
except Exception as e:
    print(f"Error: {e}")

