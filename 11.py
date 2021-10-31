first_list = input('please input first text with delimeter space" " number>>').split()
second_list = input('please input first text with delimeter space" " number>>').split()


def dic_creator(first_list, second_list):
        return {first_list[a]: second_list[a] for a in range(len(first_list))}


print(dic_creator(first_list, second_list))