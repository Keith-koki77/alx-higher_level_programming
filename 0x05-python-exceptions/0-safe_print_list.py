#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0  # Variable to keep track of the number of elements printed
        for element in my_list:
            if count < x:
                print(element, end="")
                count += 1
        print()  # Prints a new line after all elements are printed
        return (count)
    except:
        return (count)
