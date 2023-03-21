import argparse
from datetime import datetime, timedelta

def fone(n):
    print('functie een'+ str(n))

def ftwo(n, date):
    print('functie twee'+ str(n) + str(date))
    
def fthree(n):
    print('functie drie'+ str(n))
    

def Main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    subparser = parser.add_subparsers(dest = "command")

    parserone = subparser.add_parser("one", help = 'function one')
    parserone.add_argument('-num', help= "help me" + \
                        "i dont know 1", type = int)
    
    parsertwo = subparser.add_parser("two", help = 'function two')
    parsertwo.add_argument('-num', help= "help me" + \
                        "i dont know 2", type = int)
    parsertwo.add_argument('-date', help= "help me" + \
                        "i dont know datetime", type = datetime)
        
    parserthree = subparser.add_parser("three", help = 'function three')
    parserthree.add_argument('-num', help= "help me" + \
                        "i dont know 3", type = int)

    args = parser.parse_args()
    print(args)
    if args.command == "one":
        fone(args.num)

    if args.command == "two":
        ftwo(args.num, args.date)

if __name__ == '__main__':
    Main()
#print(args.list)