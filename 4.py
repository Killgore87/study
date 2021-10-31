def list_concater(first_text, second_text):
    result = []
    for i in range(0, max([len(first_text), len(second_text)])):
        try:
            result.append(first_text[i])
        except:
            pass
        try:
            result.append(second_input[i])
        except:
            pass
    return result


first_input = input('please input first text with delimeter space" " number>>').split()
second_input = input('please input first text with delimeter space" " number>>').split()
print(list_concater(first_input,second_input))