# Introduced F602: multi-value-repeated-key-variable

history = {
    "first_value": 1,
    "second_value": 3,
}


def add(a, b):
    return a + b


def record(value, history):
    history.append(value)
    return history


def broken_total():
    return "I like to eat yummy potatoes."
