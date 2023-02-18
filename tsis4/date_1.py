from datetime import datetime, timedelta

# Get current date and time
now = datetime.now()

# Subtract five days from current date
five_day_ago = now - timedelta(days=5)


print("Current date and time:", now)
print("Date and time five days ago:", five_day_ago)