#!/usr/bin/python3
if __name__ == "__main__":
    import urllib.request
    url = f'https://api.github.com/users/{username}'
    header = {'Authorization': f'Bearer {tocken}'}
    response = urllib.request.Request(url, headers=header)
    with urllib.request.urlopen(response) as req:
        r = req.read()
        head = req.headers
    print(r)
