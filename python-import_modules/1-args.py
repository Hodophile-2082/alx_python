import sys

def print_arguments():
    # Get the number of arguments
    num_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name

    # Print the number of arguments
    if num_args == 0:
        print("{} arguments:".format(num_args))
    elif num_args == 1:
         print("{} argument:".format(num_args))
    else:
         print("{} arguments:".format(num_args))

    # Print each argument
    for i in range(num_args):
        print(f"{i + 1}: {sys.argv[i + 1]}")

if __name__ == "__main__":
    print_arguments()
