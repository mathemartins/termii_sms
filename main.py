# __Author__: mathemartins
import requests
api_key: str = "TLZVWxYv8Q60Dnyga5awI4XoE9imuSfI3iWXLBrpwWiuG1PWpDghwRJtMdE99H"
baseUrl: str = f"https://api.ng.termii.com/api/sender-id?api_key={api_key}"


def send_message():

    url = "https://api.ng.termii.com/api/sms/send"
    payload = {
        "to": "2347880234567",
        "from": "talert",
        "sms": "Hi there, testing Termii ",
        "type": "plain",
        "channel": "generic",
        "api_key": "Your API Key",
        "media": {
            "url": "https://media.example.com/file",
            "caption": "your media file"
        }
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    print(response.text)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
