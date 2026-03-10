def top_frequent_words(file_path, k=10):
    word_count = {}

    with open(file_path, "r") as f:
        for line in f:
            word = line.strip()

            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Sort by frequency (highest first)
    top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    return top_words[:k]


if __name__ == "__main__":
    result = top_frequent_words("words.txt")

    for word, freq in result:
        print(word, freq)