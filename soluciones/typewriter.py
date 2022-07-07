"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor
# pip install prototools
from prototools.keyboard import typewrite, press

TXT = "* Ayuda en Python *"
BAR = "* "*(len(TXT)//2 + 1)


def start_app(app_name: str) -> None:
    subprocess.Popen(app_name)


def write_to_app(txt: str) -> None:
    time.sleep(1)
    typewrite(BAR, 0.09)
    press("enter") 
    typewrite(txt, 0.2)
    press("enter")
    typewrite(BAR, 0.09)
    press("enter")
    press("\t")
    press("\t")
    typewrite("Version ")
    press("num1")


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(start_app, ["notepad.exe"])
        executor.map(write_to_app, [TXT])
    print("Done")
