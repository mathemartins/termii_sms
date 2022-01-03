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
    msg = send_message(
        '2348034743223',
        'AMJU',
        'Greetings From AMJU Loans, Our Loan systems is back! '
        'Live and active! with improved server upgrades and advanced system architecture. '
        'Start applying for loans today',
        'TLZVWxYv8Q60Dnyga5awI4XoE9imuSfI3iWXLBrpwWiuG1PWpDghwRJtMdE99H'
    )
    msg2 = send_message(
        '2347032692137',
        'AMJU',
        'Greetings From AMJU Loans, Our Loan systems is back! '
        'Live and active! with improved server upgrades and advanced system architecture. '
        'Start applying for loans today',
        'TLZVWxYv8Q60Dnyga5awI4XoE9imuSfI3iWXLBrpwWiuG1PWpDghwRJtMdE99H'
    )
    msg3 = send_message(
        '2348033930074',
        'AMJU',
        'Greetings From AMJU Loans, Our Loan systems is back! '
        'Live and active! with improved server upgrades and advanced system architecture. '
        'Start applying for loans today',
        'TLZVWxYv8Q60Dnyga5awI4XoE9imuSfI3iWXLBrpwWiuG1PWpDghwRJtMdE99H'
    )
    msg4 = send_message(
        '2348032927221',
        'AMJU',
        'Greetings From AMJU Loans, Our Loan systems is back! '
        'Live and active! with improved server upgrades and advanced system architecture. '
        'Start applying for loans today',
        'TLZVWxYv8Q60Dnyga5awI4XoE9imuSfI3iWXLBrpwWiuG1PWpDghwRJtMdE99H'
    )
    print(msg, msg2, msg3, msg4)
