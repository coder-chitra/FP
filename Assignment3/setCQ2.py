def temperature_match(temp):

    match temp:

        case t if t > 30:
            return "Hot"

        case t if 20 <= t <= 30:
            return "Moderate"

        case _:
            return "Cold"

print(temperature_match(35))
print(temperature_match(25))
print(temperature_match(15))