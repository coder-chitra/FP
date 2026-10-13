countries = ["India", "England", "Egypt", "USA", "Ethiopia", "Japan"]

result = list(filter(lambda x: x.startswith("E"), countries))

print(result)