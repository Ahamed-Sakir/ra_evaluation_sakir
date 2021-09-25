persons = [
    {
        "name": "John",
        "age": 36,
        "country": "Norway"
    },
    {"name": "Bob",
     "age": 36,
     "country": "Norway"
     }
]
persons.sort(key=lambda x: x["name"])
print(persons)

