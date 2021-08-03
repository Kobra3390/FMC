import subprocess
from rich.progress import track
from time import sleep

def Install_Macchanger():
    options = input("Install Macchanger as Root? ")
    if((options == "Yes") or (options == "Y") or (options == "yes") or (options == "y")):
        subprocess.run(["sudo", "apt", "install", "macchanger"])
    if((options == "No") or (options == "N") or (options == "no") or (options == "n")):
        subprocess.run(["apt", "install", "macchanger"])
    if((options != "Yes") or (options != "No") or (options != "Y") or (options != "N") or (options != "yes") or (options != "no") or (options != "y") or (options != "n")):
        print("Error in the input option...")

def Loading_Bar():
    for step in track(range(100), description="Loading..."):
        sleep(0.1)
