words = ["hello", "world", "python", "code"]
words_length = [len(i) for i in words] #составляем список длины слов
print(words_length)

long_words = [words for words in words if len(words) > 4] #составляем список слов, длина которых > 4 (если честно, так и не понял, почему оно работает именно так, но оно работает))
print(long_words)

settings = dict(hello=len('hello'), world=len('world'), python=len('python'), code=len('code')) #составляем словарь слов с их длиной
print(settings)
