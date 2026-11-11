
contacts = {
    "9876543210": {
        "name": "Arun Kumar",
        "email": "arun@gmail.com"
    },
    "9876543211": {
        "name": "Priya Nair",
        "email": "priya@gmail.com"
    },
    "9876543212": {
        "name": "Rahul Menon",
        "email": "rahul@gmail.com"
    }
}

contacts["9876543213"] = {
    "name": "Anjali Menon",
    "email": "anjali@gmail.com"
}

# Look up an existing phone number
print(contacts.get("9876543210", "Not found"))

# Look up a missing phone number
print(contacts.get("9999999999", "Not found"))

# Delete an existing contact
removed_contact = contacts.pop("9876543213", "Not found")
print(removed_contact)

# Try deleting a missing contact
removed_contact = contacts.pop("9999999999", "Not found")
print(removed_contact)

# Print one contact's email
print(contacts["9876543210"]["email"])

# Print all dictionary items
print(contacts.items())

# Copy the contacts dictionary using .copy()
contacts_copy = contacts.copy()

# Change a nested email in the copy
contacts_copy["9876543210"]["email"] = "arun.new@gmail.com"

# Print the original email
print(contacts["9876543210"]["email"])

# Print the copied email
print(contacts_copy["9876543210"]["email"])

# Explanation: .copy() creates a shallow copy, so the outer dictionaries
# are different objects, but their nested contact dictionaries are shared.
# As Part A taught us, changing a nested object affects both dictionaries.
