foods = ["pizza","tacos","dim sum","sushi"]
print(foods[1])
for food in foods:
    print(f"I like to eat {food}")
    print(type(food))
#break will stop the loop
    print("loop is over")
    for food in foods:
        
        if food == "dim sum":
            continue
        print(f"I like {food} because they are yummy")
for index in range(len(foods)):
    print(index)
    print(foods[index])


#loop of the index
print(list(enumerate(foods)))
for index, food in enumerate(foods):
    print(f"My No {index + 1}, food is {food.title()}")