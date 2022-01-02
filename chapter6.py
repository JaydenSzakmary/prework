steve = {
    "name":"steve",
    "weight":155.5,
    "foods":["chicken","collards"],
    "ice_cream":{
        "vanilla":False,
        "chocolate":True,
        "coffee":False
    },
    10: "this has an integer key"
}

print(type(steve))
# name of dict[KEY]
print(steve["foods"][1])
print(type(steve["foods"]))

print(steve[10])

print(steve.get("candies"))

steve.update({"candies":["snickers","mars","m&ms"]})
print(steve)
del steve["candies"]
print(steve)

for k in steve:
    print(k)
    print(type(k))
    print(steve[k])
print(steve.values())
print(steve.items())
for key, value in steve.items():
    if isinstance(value,list):
        print(f"the list is at {key}")

print(len(steve["foods"]))

print(steve["foods"][1])