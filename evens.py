def even_numbers_of_evens(numbers):
    """A function that takes an list of numbers as an argument and returns true if
the number of even numbers are even.
    hould raise a TypeError if a list is not passed as argument
    if the list(numbers) is empty return False
    if the number of even is odd return False
    if the number of even is 0 return False
    if the number of even is even return true """
    if isinstance(numbers, list):
        even_counter = sum([1 for n in numbers if n % 2 == 0]) 
        # for number in numbers:
        #     if (number % 2) == 0:
        #         even_counter += 1
        return True if even_counter and even_counter % 2 == 0 else False
        # if even_counter != 0 and (even_counter % 2) == 0:
        #     return True
        # else:
        #     return False
    else:
        raise TypeError("A list was not passed into the function")

    

    

if __name__ == '__main__':
    print(even_numbers_of_evens(4))
