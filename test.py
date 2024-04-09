from collections import Counter

def majority_value(strings):
    """Calculate the majority value in an array of strings."""
    counts = Counter(strings)
    majority = counts.most_common(1)[0][0]
    return majority

# Example usage:
strings = ["apple", "banana", "apple", "orange", "apple", "banana"]
majority_string = majority_value(strings)
print(majority_string)