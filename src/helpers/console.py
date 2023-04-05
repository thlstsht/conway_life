from os import system, name

def clear_console():
    if name == 'nt':
        return system('cls')
    
    return system('clear')