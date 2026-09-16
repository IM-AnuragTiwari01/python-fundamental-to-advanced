device_status = input("> device status: ")

if device_status == "active":
    temperature = int(input("> enter the temperature: "))
    if temperature > 35:
        print("WARNING: High Temperature Alert!")
    else:
        print("Temperature is normal")
else:
    print("device is offline")
    