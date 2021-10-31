first_list = input('please input first text with delimeter space" ">>').split()


def str_count(first_list):
    return {a: first_list.count(a) for a in list(set(first_list))}


print(str_count(first_list))