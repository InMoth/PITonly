import argparse 

def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)



