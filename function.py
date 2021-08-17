import subprocess
from rich.progress import track
from time import sleep

def Install_Macchanger():
    options = input("Install Macchanger as Root? ")
    if((options == "Yes") or (options == "Y") or (options == "yes") or (options == "y")):
        subprocess.run(["sudo", "apt", "install", "macchanger"])
    elif((options == "No") or (options == "N") or (options == "no") or (options == "n")):
        subprocess.run(["apt", "install", "macchanger"])
    else:
        print("Error in the input option...")

def Loading_Bar():
    for step in track(range(100), description="Loading..."):
        sleep(0.1)

def Change_Mac_Manually():
    interface = input("Enter a interface: ")
    new_mac_address = input("Enter a new mac address for machine [EXAMPLE 00:00:00:00:00:01]: ") 
    choice = input("Run command with Root? ")
    if((choice == "Yes") or (choice == "Y") or (choice == "yes") or (choice == "y")):
        subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "down"])
        subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "address", new_mac_address])
        subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "up"])
    elif((choice == "No") or (choice == "N") or (choice == "no") or (choice == "n")):
        subprocess.run(["ip", "link", "set", "dev", interface, "down"])
        subprocess.run(["ip", "link", "set", "dev", interface, "address", new_mac_address])
        subprocess.run(["ip", "link", "set", "dev", interface, "up"])
    else:
        print("Error in the input option...")

def Change_New_Mac_Address():
    interface = input("Enter a interface: ")
    choice = input("Run command with Root? ")
    if((choice == "Yes") or (choice == "Y") or (choice == "yes") or (choice == "y")):
        subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "down"])
        subprocess.run(["sudo", "macchanger", "-a", interface])
        subprocess.run(["sudo","ip", "link", "set", "dev", interface, "up"])
    elif((choice == "No") or (choice == "N") or (choice == "no") or (choice == "n")):
        subprocess.run(["ip", "link", "set", "dev", interface, "down"])
        subprocess.run(["macchanger", "-a", interface])
        subprocess.run(["ip", "link", "set", "dev", interface, "up"])
    else:
        print("Error in the input option...")
    
def Show_Current_Perma_Mac():
    interface = input("Enter a interface: ")
    print("\n")
    subprocess.run(["macchanger", "-s", interface])
    print("\n")
