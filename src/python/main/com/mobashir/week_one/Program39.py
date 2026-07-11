secs = int(input("Enter the number of seconds: "))

hours = secs // 3600

minutes = (secs % 3600) // 60

secs = secs % 60

print(f"The number of hours: {hours}, minutes: {minutes} and seconds: {secs}")