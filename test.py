def list_concater(first_text, second_text):
    result = []
    def gen(s):
        for i in s:
            yield i
    tasks = [gen(first_text), gen(second_text)]
    print(str(tasks))
    while tasks:
        task = tasks.pop(0)
        try:
            i = next(task)
            result.append(i)
            tasks.append(task)
        except StopIteration:
            pass
    return result


first_input = input('please input first text with delimeter space" " number>>').split()
second_input = input('please input first text with delimeter space" " number>>').split()
print(list_concater(first_input,second_input))