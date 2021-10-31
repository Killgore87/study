def validate_password (password):
    if len(password) >= 8:
        num_of_cap = 0
        num_of_num = 0
        for i in password:
            if 'A' <= i <= 'Z':
                num_of_cap += 1
            elif '0' <= i <= '9':
                num_of_num += 1
            else:
                raise Exception('Password not valid')
        if num_of_num >= 2 and num_of_cap >= 2:
            return True
    else:
        raise Exception('Password not valid')
paswd = input('validate password')
print(validate_password(paswd))