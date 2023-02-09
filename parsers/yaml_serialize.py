# YAML is a data serialization format that is similar to JSON,
# but is often considered to be more human-friendly. The pyyaml library
# provides support for working with YAML in Python.
#
# Here's an example of how to use the pyyaml library to serialize data:
import yaml # pip install pyyaml (PyYAML==6.0)

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

# Serialize the data to a YAML string
yaml_data = yaml.dump(data)

# Write the YAML string to a file
with open("data.yaml", "w") as f:
    f.write(yaml_data)

# In this example, a dictionary data is created to represent some information
# about a person. The yaml.dump function is used to serialize the data
# to a YAML string, and the string is then written to a file using the
# write method of a file object.
#
# Here's an example of how to use the pyyaml library to deserialize data:
import yaml

# Read the YAML string from a file
with open("data.yaml", "r") as f:
    yaml_data = f.read()

# Deserialize the YAML string to a Python object
data = yaml.load(yaml_data)

# Access the values in the deserialized data
print("Name:", data["name"])
print("Age:", data["age"])
print("Address:", data["address"])
print("Phone numbers:", data["phone_numbers"])

# In this example, the YAML string is read from a file using the read method
# of a file object, and the yaml.load function is used to deserialize
# the YAML string to a Python object. The values in the deserialized data
# can then be accessed using dictionary-style indexing.
