code = int(input('ASCII code>>'))
if 65 <= code <= 90 or 97 <= code <= 122:
    print(code, ' is a letter ', chr(code))
else:
    print(code, ' is a  ', chr(code))
