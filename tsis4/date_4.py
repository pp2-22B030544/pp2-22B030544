import datetime

# Define two datetime objects
date1 = datetime.datetime(2023, 2, 17, 12, 0, 0)
date2 = datetime.datetime(2023, 2, 18, 13, 0, 0)

# Calculate the difference in seconds
difference = (date2 - date1).total_seconds()

# Print the result
print("The difference between the two dates is", difference, "seconds.")