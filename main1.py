from textparser import *

with open('text.txt') as f:
    text = delete_separator_repeats(f.read())
    sentences = get_sentences_amount(text.replace(" ", ""))
    lengths = get_average_sentence_length(text)
    ngrams = get_top_k_ngrams(text)

    print(f"Amount of sentences in the text: {sentences[0]}"
          f"\nAmount of non-declarative sentences in the text: {sentences[1]}"
          f"\nAverage length of the sentence in characters: {lengths[0]}"
          f"\nAverage length of the word in the text in characters: {lengths[1]}"
          f"\nTop-10 repeated 4-grams in the text:")

    i = 1
    for key in ngrams.keys():
        print(f"{i}) {key}: {ngrams[key]} times")
        i += 1