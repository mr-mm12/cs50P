import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Split the input by dots
    ip_part = ip.split(".")

    # IPv4 must have exactly 4 parts
    if len(ip_part) != 4:
        return False

    for i in ip_part:
        # Each part must be a number without leading zeros
        if not i.isdigit() or (len(i) > 1 and i[0] == "0"):
            return False

        num = int(i)
        # Each number must be between 0 and 255
        if num < 0 or num > 255:
            return False


    return True


if __name__ == "__main__":
    main()

# Mohammad_Reza_Mokhtari_Kia
