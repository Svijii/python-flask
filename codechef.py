def is_oneful_pair(a, b):
    return a + b + (a * b) == 111

# Iterate through possible values of a and b to find Oneful Pairs
oneful_pairs = []
for a in range(1, 111):
    for b in range(1, 111):
        if is_oneful_pair(a, b):
            oneful_pairs.append((a, b))

# Print the Oneful Pairs
for pair in oneful_pairs:
    print(pair)
