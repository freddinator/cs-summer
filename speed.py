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
print("--------------\n")

distance = float(input('How long is the road distance in metres? > '))
print('  \033[92m ✔ Road distance set\033[0m')

speedlimit = float(input('Enter speed limit in miles per hour > '))
print('  \033[92m ✔ Speed limit set\033[0m')

# d = s*t
# s = d/t
while True:
	print("--------------\n")
	time = float(input('Enter time to get through the road distance in seconds > '))
	speed_in_ms = distance / time
	speed_in_mph = mps_to_mph(speed_in_ms)
	print('Speed in MPH:', speed_in_mph)
	if speed_in_mph < speedlimit or speed_in_mph == speedlimit:
		print('\033[92m ✔ Under speed limit \033[0m')
	else:
		print('\033[91m ✗ Over speed limit \033[0m')

