# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

import sys
# Your code here
def main():
    
    # TODO: read text from stdin
    text= sys.stdin.read()
    # TODO: Filter character given as an argument from the text
    user_filter = sys.argv[1]
    filtered_text = text.replace(user_filter, '')
    count = text.count(user_filter)

    # TODO: Print the result to stdout
    sys.stdout.write(filtered_text)
    # TODO: Print the total number of removed characters to stderr
    sys.stderr.write(str(count))


if __name__ == "__main__":
    main()
