people = [
    {'name': 'Anitha', 'age': 25},
    {'name': 'Mallika', 'age': 30},
    {'name': 'Arun', 'age': 20}
]
sorted_people = sorted(people, key=lambda x: x['age'])
print(sorted_people)



