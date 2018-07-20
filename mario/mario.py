from cs50 import get_int

def main():
    height = get_height("Height: ")
    print_mario(height)

def get_height(prompt):
    while True:
        n = get_int(prompt)
        if n > 0 and n <= 23:
            break
    return n


def print_mario(height):
    pound = '#'
    space = ' '
    for i in range(height):
        for blank in range(height - i - 1):
            print(space, end='')
        for left_hash in range(i + 2):
            print(pound, end='')

        print("  ", end='')

        for right in range(i + 2):
            print(pound, end='')

        print('')


if __name__ == "__main__":
    main()