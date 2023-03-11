def print_multiplication_table_for(x):
    """
    Prints the multiplication table for a given digit.
    Input: 
        x - a digit
    Output:
        output - a string containing the multiplication table for x
    """    
    output = ""
    for i in range(1, 10):
        # output = output + f"{x} x {i} = {x*i}"
        output += f"{x} x {i} = {x*i}\n"
    return output

besler = print_multiplication_table_for(5)
print(besler, end="\n -- THE END -- \n")