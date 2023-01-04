import time
import datetime

# Get current time
current_time = datetime.datetime.now()

# Calculate end of day by setting hour, minute, and second to 0
end_of_day = current_time.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)

# Calculate time left until end of day
time_left = end_of_day - current_time

# Print time left in hours, minutes, and seconds
print(f"Hours left: {time_left.seconds // 3600}")
print(f"Minutes left: {(time_left.seconds // 60) % 60}")
print(f"Seconds left: {time_left.seconds % 60}")

# Continuously update time left until end of day
while True:
    current_time = datetime.datetime.now()
    time_left = end_of_day - current_time
    print(f"\r{time_left.seconds // 3600} Hours : {(time_left.seconds // 60) % 60} Minutes : {time_left.seconds % 60} Seconds ", end="")
    time.sleep(1)