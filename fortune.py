import random
def get_random_fortune(filename="fortune.txt"):
    with open(filename, "r") as file:
        quotes = file.read().split('%')
        quotes = [quote.strip() for quote in quotes if quote.strip()]
        print(random.choice(quotes))
get_random_fortune()
