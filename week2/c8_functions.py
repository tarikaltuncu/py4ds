import sys

def print_multiplication_table_for(x):
    """Prints the multiplication table for a given digit."""    
    assert 10 >= x >= 0, "x must be between 0 and 10"

    print(f"Multiplication table for {x}:")
    
    for i in range(1, 11):
        print(f"\t{x} x {i} = {multiply(x, i)}")

def multiply(x, y):
    """Multiplies two numbers"""
    assert type(x) == int, "x must be an integer"
    assert type(y) == int, "y must be an integer"
    return x * y

def main():
    x = int(sys.argv[1])
    print_multiplication_table_for(x)

if __name__ == "__main__":
    main()