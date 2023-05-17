

print('Задание 2.2')
def add_brackets(word):
    length = len(word)
    mid = length // 2

    result = []
    if length % 2 == 0:
        mid = length // 2
        for i in range(length):
            if i == mid or i == mid-1:
                result.append(word[i])

            else:
                if i < mid and i != mid-1:
                    result.append(word[i]+'(')
                elif i > mid:
                    result.append(')' + word[i])


    else:
        mid = length // 2
        for i in range(length):
            if i == mid:
                result.append(word[i])
            else:
                if i < mid:
                    result.append(word[i] + '(')
                elif i > mid:
                    result.append(')' + word[i])

    return ''.join(result)


input_word = input("Введите слово: ")
output_word = add_brackets(input_word)
print(output_word)


