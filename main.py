# __Author__: mathemartins
import requests

api_key: str = "TLZVWxYv8Q60Dnyga5awI4XoE9imuSfI3iWXLBrpwWiuG1PWpDghwRJtMdE99H"
baseUrl: str = f"https://api.ng.termii.com/api/sender-id?api_key={api_key}"


def send_message(receiver: str, sender: str, message: str, api_key: str):
    url = "https://api.ng.termii.com/api/sms/send"
    payload = {
        "to": receiver,
        "from": sender,
        "sms": message,
        "type": "plain",
        "channel": "generic",
        "api_key": api_key,
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    print(response.text)
    return response.content.decode("utf-8")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    send_message()
