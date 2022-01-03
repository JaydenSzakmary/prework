def first_odds():
    odd_numbers = list(range(1, 100)) 
 
    odd = []

 
    for x in odd_numbers:     
        if x % 2 != 0:                 
            odd.append(x) 

    print(odd)
first_odds()