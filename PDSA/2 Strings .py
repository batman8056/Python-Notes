# Reverse Words in a Sentence O(n)

def reverse_words(s):
    return " ".join(s.split()[::-1])

s = "hello world python"
print(reverse_words(s))  # Output: "python world hello"
