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
        print(response.json())  # Cetak respons dari API
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == '__main__':
    try:
        print("""\033[1m
   _____ __  ________
  / ___//  |/  / ___/ | SMS Sender
  \__ \/ /|_/ /\__ \  | SMS Sender using Rapid API
 ___/ / /  / /___/ /  | Coded by Mrxpoint
/____/_/  /_//____/   | ex: +15684036121\033[0m
        """)

        phone_number = input("No    : ").strip()
        if not phone_number.startswith('+') or not phone_number[1:].isdigit():
            print("Check your phone number format! It should start with '+' and contain only digits.")
            sys.exit()

        text = input("Text  : ").strip()
        if not text:
            print("Text should not be empty!")
            sys.exit()

        print("")
        send_sms(phone_number, text)

    except (KeyboardInterrupt, EOFError):
        print("\n")
        sys.exit()
