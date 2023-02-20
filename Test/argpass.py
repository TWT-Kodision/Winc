import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-l','--list', type=str,  nargs='+', help='<Required> Set flag', required=True)

args = parser.parse_args()
#print(args.list)