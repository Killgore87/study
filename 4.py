def list_concater(first_text, second_text):
    result = []
    if len(first_text) == len(second_text):
        for i in range(len(first_text)):
            result.append(first_text[i])
            result.append(second_text[i])
        return result
    else:
        if len(first_text) > len(second_text):
            for a in range(len(second_text)):
                result.append(first_text[a])
                result.append(second_text[a])
            for b in range(len(first_text) - len(second_text)):
                result.append(first_text[b])
            return result
        else:
            for a in range(len(first_text)):
                result.append(first_text[a])
                result.append(second_text[a])
            for b in range(len(second_text) - len(first_text)):
                result.append(second_text[b])
            return result


first_input = input('please input first text with delimeter space" " number>>').split()
second_input = input('please input first text with delimeter space" " number>>').split()
print(list_concater(first_input,second_input))