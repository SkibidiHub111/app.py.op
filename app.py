import requests

def handler(request):
    url = "https://raw.githubusercontent.com/SkibidiHub111/Ghoul/refs/heads/main/Ghoul"
    response = requests.get(url)
    if response.status_code == 200:
        lua_code = response.text
    else:
        lua_code = "Error: Không thể tải file Lua từ URL"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": lua_code
    }
