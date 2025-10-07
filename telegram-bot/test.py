#!/usr/bin/env python3
import yaml

def get_bills():
    bills =[]
    while True:
        name = str(input("Enter your name: ")).lower()
        if name == "q":
            print (f"{bills}  those bills are added.")
            break
        billamount= float(input("Enter the amount: "))
        comment = str(input("Enter a comment: "))
        bill = {"name": name,
                    "billamount": billamount,
                    "comment": comment
                    }
        bills.append(bill)
        continue
    return bills

def write_bills_to_file(bills):
    with open("bill_test_file.yaml", "a") as bill_test_file:
        yaml.dump(bills ,bill_test_file, sort_keys=True)
    print(yaml.dump(bills, sort_keys=True))

def main():
    bills = get_bills()
    write_bills_to_file(bills)

__init__ = "__main__"
if __init__ == "__main__":
    main()
