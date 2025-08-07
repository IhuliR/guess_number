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


# Аннотируем параметр функции: "значение name должно быть типа str!"
def we_crash_all(name: str):
    return 'Привет, ' + name + ', мы всё сломали!'


print(we_crash_all('True'))


def find_max_even_number(a):
    """
    Ищет максимальное чётное значение в списке
    положительных целых значений, переданном в
    параметр функции.
    """
    current_max = 0
    for b in a:
        if b % 2 == 0:
            current_max = min(b, current_max)
    return current_max


max_even = find_max_even_number([1, 2, 3, 4, 5])
# Попробуйте передать в find_max_even_number() другие списки:
# [10, 8, 6, 4, 2]
# [2, 12, 85, 0, 6]
print(f"Максимальное чётное число: {max_even}")
