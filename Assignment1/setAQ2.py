counter = 0

def update_counter():
    global counter
    counter += 1
    return counter

print(update_counter())
print(update_counter())
print(update_counter())