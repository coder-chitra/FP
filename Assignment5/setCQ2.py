def filter_names(names, substring):

    for name in names:
        if substring.lower() in name.lower():
            yield name

names = [
    "Chitra",
    "Aakanksha",
    "Rahim",
    "Neeraja",
    "Ankush"
]

result = filter_names(names, "hi")

for name in result:
    print(name)