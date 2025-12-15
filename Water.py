consumption = float(input("Total water consumption for the month (in cubic meters): " ))

service_charge= 15.00
total_bill = 0.00

if consumption <= 15 and consumption >= 0:
    consumption_cost = consumption * 0.90
elif consumption <= 30 and consumption > 16:
    consumption_cost = consumption * 1.20
else:
    consumption_cost = consumption * 1.80

total_bill = service_charge + consumption_cost

print("------------------Monthly Water Bill Summary------------------")
print(f"Consumption: {consumption}𝑚3  ")
print(f"Service Chage : GHS {service_charge}")
print(f"Consumption Cost : GHS {round(consumption_cost, 2)}")
print(f"Total Bill : GHS {round(total_bill, 2)}")