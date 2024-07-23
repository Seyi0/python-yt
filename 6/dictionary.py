# Dictionaries
band = {
# vocal = key , plants = value
    "vocals": "Plants",
    "guitar": "Page"
}

band2 = dict(vocal = "Plants", guitar = "Page")

print(band)
print(band2)

print(type(band))
print(len(band))

# access items in dictionary
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# list all value
print(band.values())