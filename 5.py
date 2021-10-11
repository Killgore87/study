code = int(input('ASCII code>>'))
if ord('a') <= code <= ord('z') or ord('A') <= code <= ord('Z'):
    print(code, ' is a letter ', chr(code))
else:
    print(code, ' is a  ', chr(code))
