import rich
from rich.console import Console
from rich.progress import track
from function import *
from function import *

console = Console()

print("\n")
Loading_Bar()

console.print("""[blue] ______   __    __     ______    
/\  ___\ /\ "-./  \   /\  ___\   
\ \  __\ \ \ \-./\ \  \ \ \____  
 \ \_\    \ \_\ \ \_\  \ \_____\ 
  \/_/     \/_/  \/_/   \/_____/ 
                                 

""")
console.print("[red] THE POWER OF MACCHANGER IN A SCRIPT\n")

console.print("[red][1] Install Macchanger")
print("\n")

options = int(input("Enter a options: "))

if(options == 1):
  Install_Macchanger()
