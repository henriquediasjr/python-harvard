# Define a list of dictionaries, where each dictionary represents a person
# Each person has two attributes: "name" and "house"
people = [
    {"name": "Henrique", "house": "Gryffindor"},  # Henrique belongs to Gryffindor house
    {"name": "Niara", "house": "Ravenclaw"},      # Niara belongs to Ravenclaw house
    {"name": "Nei", "house": "Slytherin"},        # Nei belongs to Slytherin house
]


# Bad Method
# def f(person):
#     return person["house"]

# people.sort(key=f)

# Use the sort method to sort the list of dictionaries
# The 'key' parameter specifies how to sort the dictionaries
# We use a lambda function to extract the "name" key from each dictionary for sorting
people.sort(key=lambda person: person["name"])

# Print the sorted list of dictionaries
# The list will now be sorted alphabetically by the "name" field
print(people)
