# Write a program that uses assert to verify a list of temperatures is valid
# Write a function called check_temps that takes a list of temperatures
# and asserts that none of them are below -273 (absolute zero in celsius — physically impossible)
# Loop through the list and assert each one.
# Test it with : temps = [100, 25, -50, -300, 37]


temps = [100, 25, -50, -300, 37]

def check_temps (temps):

    for absolute in temps:
        assert  absolute >= -273

check_temps(temps)


