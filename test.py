# def validate_password (password):
#     if len(password) >= 8:
#         for i in password:
#             if 'A' <= i <= 'Z':
#                 return True
#             else:
#                 return False
#     else:
#         return False
# paswd = input('validate password')
# print(validate_password(paswd))

# url = "https://youtu.be/eVIozKR9p5a0"
# url1 = "https://youtu.be12-3.v1/eVIozKR9asdp50"
# url2 = "https://youtu.be/eVIoassdzKR9asdp50"
# url3 = "https://youtu.bev1/v1/eVIoas!!zKR9asdp50"
# url4 = "https://youtu.beapi.v2/eVIoas!!zKR9asdp50"
#
# urls = [url, url4, url3, url2, url1]
# out=[]
# for i in urls:
#     out.append(i[(i.rfind('/')+1):])
# print(out)
#a = int(input('a'))
#if 4 <= a <= 6:
#    print('ok')
#lst = [int(i) for i in'q1j321kj123kj12' if '0' <= i <= '9']
#print(lst)
# def custom_min (*a):
#     if not a:
#         return 'empty'
#     min = a[0]
#     for i in a:
#         if i < min:
#             min = i
#     return min
#
# print(custom_min(10, -23, 17, 20))