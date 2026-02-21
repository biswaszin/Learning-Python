#dictionary = a collection of keys and values pair

capitals = {"USA": "Washing DC",
            "India" : "New Delhi",
             "China" : "Beijing" }

print(capitals.get("USA"))

# to add / update the capitals dictionary

capitals.update({"Germany" : "Berlin"})
print(capitals)

all_keys = capitals.keys()

for keys in all_keys:
    print(keys)
