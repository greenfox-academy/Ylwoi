__author__ = 'ylwoi'

# Accidentally I messed up this quote from Richard Feynman.
# Two words are out of place
# Your task is to fix it by swapping the right words with code

# Also, print the sentence to the output with spaces in between.

words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]

words[2], words[5] = words[5], words[2]

for i in range(len(words)):
    print(words[i], end=" ")