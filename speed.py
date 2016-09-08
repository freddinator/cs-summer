def mps_to_mph(mps):
    return 2.23694 * mps

def mph_to_mps(mph):
    return mph / 2.23694


print("Checking equation accuracy...")
mph = mps_to_mph(100)
print("Converting 100 m/s to mph:", mph)
ms = mph_to_mps(mph)
print("Converting back to m/s:", ms)
print("Difference:", 100-ms)
print("--------------")

distance = float(input('How long is the road distance in metres? > '))
print('  \033[92m ✔ Road distance set\033[0m')

speedlimit = float(input('Enter speed limit in miles per hour > '))
print('  \033[92m ✔ Speed limit set\033[0m')
print("--------------")

# d = s*t
# s = d/t
while True:
    try:
        time = float(input('Enter time to get through the road distance in seconds > '))
    except ValueError:
        print('\033[93m ❗ Invalid time \033[0m')
    else:
        speed_in_ms = distance / time
        speed_in_mph = mps_to_mph(speed_in_ms)
        print('Speed in MPH: {0:.2f}'.format(speed_in_mph))
        if speed_in_mph < 0.05:
            print('\033[93m ⓘ  The driver\'s speed is zero when rounded to two decimal places \033[0m')
        elif speed_in_mph < speedlimit or speed_in_mph == speedlimit:
            print('\033[92m ✔ Under speed limit \033[0m')
        else:
            print('\033[91m ✗ Over speed limit \033[0m')

        print("--------------\n")


