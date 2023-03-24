from re import findall
from constants import *
from operator import itemgetter


def delete_separator_repeats(text: str):

    stack = []
    for symbol in text:
        stack.pop() if stack and symbol in SYMBOLS and stack[-1] == symbol else stack.append(symbol)
    stack.append(".") if stack and stack[-1] not in SYMBOLS else stack.append("")

    return ''.join(stack)


def get_sentences_amount(text: str):

    dot_separators = text.count(".")
    other_separators = 0
    for separator in SYMBOLS :
        if separator != ".":
            other_separators += text.count(separator)
    dot_exceptions = 0
    for abbreviation in APPEALS:
        dot_exceptions += len(findall(abbreviation, text))

    non_declarative_amount = other_separators
    general_amount = non_declarative_amount + dot_separators - dot_exceptions

    return [general_amount, non_declarative_amount]


def get_average_sentence_length(text: str):

    words = text.split()
    result = 0
    current_sentence_symbols_amount = 0
    current_sentence_words_amount = 0

    symbols = 0
    sentences = 0

    for word in words:
        current_sentence_symbols_amount += len(word) if not word.isdigit() else 0
        symbols += len(word) if not word.isdigit() else 0
        current_sentence_words_amount += 1 if not word.isdigit() else 0

        if word[-1] in SYMBOLS:
            current_sentence_symbols_amount -= 1
            symbols -= 1

            if word not in APPEALS:
                result += current_sentence_symbols_amount
                current_sentence_symbols_amount = 0
                current_sentence_words_amount = 0
                sentences += 1

    return [round(result / sentences, 3), round(symbols / len(words), 3)] if text else [0, 0]


def get_top_k_ngrams(text, k=10, n=4):

    result = {}
    words = text.split()

    for word in words:

        if len(word) == n:
            try:
                result[word] += 1
            except KeyError:
                result[word] = 1

    result = dict(sorted(result.items(), key=itemgetter(1), reverse=True))
    result = {key: result[key] for key in list(result.keys())[:k]}

    return result