capitals = {"USA":"Washington",
            "India":"New Delhi",
            "italy":"Rome",
            "Russia":"mascow"
            }
print(capitals.get("USA"))
print(capitals.update({"UK":"london"}))#
print(capitals.pop("USA"))
for key in capitals.keys():
    print(key)
for value in capitals.values():
    print(value)
print(capitals)
for key,value in capitals.items():
    print(f"{key},{value}")