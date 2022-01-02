

def sum_two_smallest_numbers(numbers):
    numbers.sort()
#sorted the list and captured the first integer
    first_integer=numbers[0]
#captured second integer
    second_integer=numbers[1]
#add together for final answer
    s= first_integer + second_integer
    print(s)