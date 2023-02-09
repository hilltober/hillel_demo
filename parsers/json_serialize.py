# The json module in Python provides a way to serialize and deserialize data
# in the JavaScript Object Notation (JSON) format. JSON is a popular
# data exchange format that is lightweight and easy to read and write.
#
# Here's an example of how to use the json module in Python to serialize data:

import json

data = {
    "name": "John Doe",
    "age": 35,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA"
    },
    "phone_numbers": [
        "555-555-1234",
        "555-555-5678"
    ]
}

# Serialize the data to a JSON string
json_data = json.dumps(data)

# Write the JSON string to a file
with open("data.json", "w") as f:
    f.write(json_data)

# In this example, a dictionary data is created to represent some information
# about a person. The json.dumps function is used to serialize the data
# to a JSON string, and the string is then written to a file using the
# write method of a file object.
#
# Here's example of how to use the json module in Python to deserialize data:
import json

# Read the JSON string from a file
with open("data.json", "r") as f:
    json_data = f.read()

# Deserialize the JSON string to a Python object
data = json.loads(json_data)

# Access the values in the deserialized data
print("Name:", data["name"])
print("Age:", data["age"])
print("Address:", data["address"])
print("Phone numbers:", data["phone_numbers"])

# In this example, the JSON string is read from a file using the read method
# of a file object, and the json.loads function is used to deserialize
# the JSON string to a Python object. The values in the deserialized data
# can then be accessed using dictionary-style indexing.
