import collections


def frequency_distribution(text):
    words = text.split()
    word_counts = collections.Counter(words)
    return word_counts


if __name__ == "__main__":
    with open("C://Users//ASHIK C SABU//Desktop//stdent.csv") as f:
        text = f.read()
    word_counts = frequency_distribution(text)
    print(word_counts)
