import datetime

# Create a datetime object with microseconds
dt_with_microseconds = datetime.datetime(2023, 2, 17, 12, 34, 56, 789)

# Drop the microseconds
dt_without_microseconds = dt_with_microseconds.replace(microsecond=0)

# Print the original and modified datetime objects
print("Original datetime with microseconds:", dt_with_microseconds)
print("Datetime without microseconds:", dt_without_microseconds)