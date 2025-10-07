from scipy.stats import mannwhitneyu
import tkinter as tk


def user_inputs():
    online_gps = []
    offline_gps = []
    while True:
        user_input = str(input("For what Group do you want to add a Value? [A/B] [stop to calculate] "))
        while True:
            if user_input == "A":
                try:
                    values = input("Enter Value(s) for Group A (space-separated): ").split()
                    for val in values:
                        value = float(val)
                        online_gps.append(value)
                    #online_gps.append(value)
                    print (online_gps)
                except ValueError:
                    print("exiting Group A Value input..")
                    break
            elif user_input == "B":
                try:
                    values = input("Enter Value for Group B (space-seperated): ").split()
                    for val in values:
                        value = float(val)
                        offline_gps.append(value)
                    print (offline_gps)
                except ValueError:
                    print("exiting Group B Value input..")
                    break
            else:
                break
                
        if user_input == "stop":
            break
        else:
            print("Do you want to add a Value? [stop] to stop and calculate..")
    
    return online_gps, offline_gps

def mannwhitneyu_calc(online_gps, offline_gps):
    U1, p = mannwhitneyu(online_gps, offline_gps, method="asymptotic")

    nx,ny = len(online_gps), len(offline_gps)
    U2 = nx*ny - U1

    print (f"the U1 Value is: {U1}")
    print (f"the U2 Value is: {U2}")
    print (f"the p Value is: {p}")

def main():
    online_gps, offline_gps = user_inputs()
    mannwhitneyu_calc(online_gps, offline_gps)

if __name__ == "__main__":
    main()