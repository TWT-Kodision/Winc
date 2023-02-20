import argparse
from functions import*

commands = {
                "ab":"add to buy list",
                "as":"add to sold list",
                "sp":"show product inventory list",
                "si":"show complete inventory",
                "cl":"clear list"
                }

parser = argparse.ArgumentParser(description='Inventory administration')
parser.add_argument('command', type=str, choices=commands, help="what is your command: ab=add to buy list, as=add to sold list, sp=show product inventory list, si=show complete inventory, cl=clear list")
parser.add_argument("product", nargs='*', help="product specifications bought list: sold list:")
parser.add_argument("--file_name", type=str, help="file name needed to define which list to clear") 
args = parser.parse_args()

def switch(command):
    command_keys = list(commands)
    if command == command_keys[0]: 
        return "you chose add to buy"
    elif command == command_keys[1]:
        return "you chose add to sell"
    elif command == command_keys[2]:
        return "you chose show product inventory"
    elif command == command_keys[3]:
        return "you chose show complete inventory"
    elif command == command_keys[4]:
        return "you chose clear inventory list"
    else:
        return("chosen option is not available")

#check input product


print(switch(args.command))
print(args.product)
