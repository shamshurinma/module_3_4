def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.upper() in i.upper() or i.upper() in root_word.upper():
            same_words.append(i)
    return same_words


result_1 = single_root_words('Бок', 'богатый', 'коробок', 'Богатырь', 'Боковой', 'колобок')
result_2 = single_root_words('Тепловоз', 'тепло', 'воз', 'Зов', 'ход', 'Плов')
print(result_1)
print(result_2)
