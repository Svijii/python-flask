def is_subsequence(subsequence, sequence):
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)
    i = 0  # Index for subsequence
    j = 0  # Index for sequence
    while i < subsequence_length and j < sequence_length:
        if subsequence[i] == sequence[j]:
            i += 1
        j += 1
    return i == subsequence_length
# Example usage:
sequence = "abcde"
subsequence = "ace"
result = is_subsequence(subsequence, sequence)
if result:
    print(f'"{subsequence}" is a subsequence of "{sequence}".')
else:
    print(f'"{subsequence}" is not a subsequence of "{sequence}".')
