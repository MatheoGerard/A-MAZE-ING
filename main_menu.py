from rich.panel import Panel
from rich.console import Console


def print_title(console: Console) -> None:
    title: str = r"""
 ______                     ______  ________   ____            ______   __  __  ____      
/\  _  \            /'\_/`\/\  _  \/\_____  \ /\  _`\         /\__  _\ /\ \/\ \/\  _`\    
\ \ \L\ \          /\      \ \ \L\ \/____//'/'\ \ \L\_\       \/_/\ \/ \ \ `\\ \ \ \L\_\  
 \ \  __ \  _______\ \ \__\ \ \  __ \   //'/'  \ \  _\L   _______\ \ \  \ \ , ` \ \ \L_L  
  \ \ \/\ \/\______\\ \ \_/\ \ \ \/\ \ //'/'___ \ \ \L\ \/\______\\_\ \__\ \ \`\ \ \ \/, \
   \ \_\ \_\/______/ \ \_\\ \_\ \_\ \_\/\_______\\ \____/\/______//\_____\\ \_\ \_\ \____/
    \/_/\/_/          \/_/ \/_/\/_/\/_/\/_______/ \/___/          \/_____/ \/_/\/_/\/___/ 
                                                                                          
"""

    console.print(Panel(title, expand=False, border_style="yellow"))


if __name__ == "__main__":
    console: Console = Console()
    print_title(console)
