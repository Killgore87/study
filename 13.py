import requests


def response():
    site_request = requests.get("http://jsonplaceholder.typicode.com/posts").json()
    print_resp(site_request)


def print_resp(response_list):
    hold = 0
    for i in range(len(response_list)):
        print('title \n', response_list[i].get('title'), '\n', 'text \n', response_list[i].get('body'), ' \n', i + 1, ' \n')
        hold += 1
        if hold == 3:
            input()
            hold = 0


response()