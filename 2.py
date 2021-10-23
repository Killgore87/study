def get_ext(filename):
    a = filename.split('.')
    if a[-1] != '' and len(a) != 1:
        return a[-1]
    return "value error"


file_to_procces = input('please input filename')
print(get_ext(file_to_procces))