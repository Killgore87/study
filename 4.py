def list_concater(first_text, second_text):
    result = []
    for i in range(len(first_text)):
        result.append(first_text[i])
        if i < len(second_text):
            result.append(second_text[i])
            if i == (len(first_text) - 1) and i != (len(second_text) - 1):
                for a in range(i, len(second_text)):
                    result.append(second_text[a])
    return result

first_input = input('please input first text with delimeter space" " number>>').split()
second_input = input('please input first text with delimeter space" " number>>').split()
print(list_concater(first_input,second_input))
