def reverse_words(sentence):

    words = sentence.split()

    return " ".join(reversed(words))

def apply_function(func, value):
    return func(value)

text = "Functional Programming is Powerful"

print(apply_function(reverse_words, text))