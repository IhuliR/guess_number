def find_texts_with_substring(texts, substring):
    matching_texts = []
    for text in texts:
        if substring in str.lower(text):
            matching_texts.append(text)
    return matching_texts


original_texts = [
    'Маша читает газету',
    'Кот и кошка гуляют по двору',
    'Бутерброд лежит на столе маслом вниз'
]
what_to_find = 'ма'

print(
    'Подходящие строки:',
    find_texts_with_substring(original_texts, what_to_find)
)
