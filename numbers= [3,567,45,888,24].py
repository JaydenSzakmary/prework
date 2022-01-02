def sum_two_smallest_numbers(numbers):
    numbers= [3,567,45,888,24]
    numbers.sort()
#sorted the list and captured the first integer
    first_integer=numbers[0]
    print(first_integer)
#captured second integer
    second_integer=numbers[1]
    print(second_integer)
#add together for final answer
    sum= first_integer + second_integer
    print(sum)