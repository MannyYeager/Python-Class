recorded_speeds = [95, 110, 100, 85, 125, 90, 105, 115, 70, 130, 99, 101, 88] 

SPEED_LIMIT = 100 

speeding_violations = []

for speed in recorded_speeds:
    if speed > SPEED_LIMIT:
        print(f"WARNING : Vehicle recorded at {speed} km/h. Exceeds speed limit of {SPEED_LIMIT} km/h")
        speeding_violations.append(speed)

print("------------------Speeding Violations Summary------------------")
print(f"Total number of vehicles: {len(recorded_speeds)}")
print(f"Total number of speeding violations: {len(speeding_violations)}")
print(f"The percentage of speeding vehicles: {round((len(speeding_violations) / len(recorded_speeds) * 100), 2)}%")
print(f"Average speed of violation: {round((sum(recorded_speeds) / len(recorded_speeds)), 2)} km/h")

speed_data = recorded_speeds[2:8:]
print(f"Speeds for focused inspection segment (3rd to 8th vehicle): {speed_data}")