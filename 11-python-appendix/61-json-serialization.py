import json
friends = {"Dan": [20, "London", 3234342], "Maria": [25, "Madrid", 3423423]}

# Write the dictionary to a file
with open("friends.json", "w") as f:
    json.dump(friends, f, indent=4)

json_string = json.dumps(friends, indent=4)
print(json_string)