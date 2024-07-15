import sys
import requests

def send_sms(phone_number, text):
    url = "https://rapid-sms-api.p.rapidapi.com/sms"

    payload = {
        "phone_number": phone_number,
        "text": text
    }
    headers = {
        "x-rapidapi-key": "c710bc2045msh4a30948250732e4p1f4853jsn3651b645e37c",
        "x-rapidapi-host": "rapid-sms-api.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(f"Failed to send SMS to {phone_number}. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return False

def main(cnt, phone_number, text):
    try:
        print("""\033[1m
   _____ __  ________
  / ___//  |/  / ___/ | SMS Spammer
  \__ \/ /|_/ /\__ \  | SMS Spammer using Rapid API
 ___/ / /  / /___/ /  | Coded by Mrxpoint
/____/_/  /_//____/   | ex: +15684036121\033[0m
        """)

        success_count = 0
        for i in range(cnt):
            success = send_sms(phone_number, text)
            if success:
                success_count += 1
                print(f"[{success_count}] SMS sent to {phone_number} successfully.")
            else:
                print(f"[{i + 1}] Failed to send SMS to {phone_number}")

    except (KeyboardInterrupt, EOFError):
        print("\n")
        sys.exit()

if __name__ == '__main__':
    try:
        phone_number = input("No    : ").strip()
        if not phone_number.startswith('+') or not phone_number[1:].isdigit():
            print("Check your phone number format! It should start with '+' and contain only digits.")
            sys.exit()

        text = input("Text  : ").strip()
        if not text:
            print("Text should not be empty!")
            sys.exit()

        cnt = input("Count : ").strip()
        if not cnt.isdigit():
            print("Check your count! It should be a number.")
            sys.exit()

        cnt = int(cnt)
        if cnt <= 0:
            print("Count should be greater than zero!")
            sys.exit()

        print("")
        main(cnt, phone_number, text)

    except (KeyboardInterrupt, EOFError):
        print("\n")
        sys.exit()
