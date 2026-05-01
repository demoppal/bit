import xx
import asyncio
import sys

async def start():
    try:
        # xx.so ထဲက main_menu ကို async စနစ်နဲ့ ခေါ်တာပါ
        await xx.main_menu()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        # Async function ကို run ပေးတဲ့ command ပါ
        asyncio.run(start())
    except KeyboardInterrupt:
        pass

