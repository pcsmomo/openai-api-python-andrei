import json

# Read the dictionary from a file
with open("friends.json", "r") as f:
    friends = json.load(f)
    print(type(friends))
    print(friends)

json_string = """
{
    "Dan": [
        20,
        "London",
        3234342
    ],
    "Maria": [
        25,
        "Madrid",
        3423423
    ]
}
"""

obj = json.loads(json_string)
print(type(obj))
print(obj)