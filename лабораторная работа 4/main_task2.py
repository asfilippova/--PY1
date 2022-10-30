
def get_count_char(str_):
    dict_ = {}
    str_ = ''.join(str_.split())
    str_ = str_.lower() #приводим все символы к одному виду
    for symbol in str_:
        if symbol.isalpha(): #добавляем в словарь только символы, явл. буквами
            if symbol not in dict_:
                dict_[symbol] = 1 #добавляем значение в словарь
            else:
                dict_[symbol] += 1 #изменяем значение если символ уже добавлен
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

# Функция изменяющая значение на процентное соотношение
#def new(dict_):
    #a = sum(dict_.values())
    #for keys in dict_:
        #dict_[keys] /= a
        #dict_[keys] *= 100
    #return dict_


#dict_1 = {'д': 13, 'а': 18, 'н': 13}
#print(new(dict_1))

