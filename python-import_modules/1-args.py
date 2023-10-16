import sys

def print_arguments():
    # Get the number of arguments
    num_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name

    # Print the number of arguments
    if num_args == 0:
        print("Number of argument(s) .")
    elif num_args == 1:
        print("Number of argument(s) followed by argument:")
    else:
        print(f"Number of argument(s) followed by arguments:")

    # Print each argument
    for i in range(num_args):
        print(f"{i + 1}: {sys.argv[i + 1]}")

if __name__ == "__main__":
    print_arguments()
