def print_multiplication_table_for(x):
    """Prints the multiplication table for a given digit."""    
    
    print(f"Multiplication table for {x}:")

    for i in range(1, 10):
        print(f"\t{x} x {i} = {multiply(x, i)}")

def multiply(x, y):
    """Multiplies two numbers"""
    assert type(x) == int, "x must be an integer"
    assert type(y) == int, "y must be an integer"
    return x * y

print_multiplication_table_for(5)
print_multiplication_table_for(5.5)