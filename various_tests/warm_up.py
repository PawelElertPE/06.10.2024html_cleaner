import time

# while True:
#     current_time = time.time()
#     print("Current time:", time.strftime("%H:%M:%S", time.localtime(current_time)))
#     print("Keep coding in Python!")
#     time.sleep(3)
#     time_difference = time.time() - current_time
#     print("Time difference after sleeping for 3 seconds:", time_difference, "seconds")

import time

# Continuous loop
while True:
    # Get the current time before sleeping
    start_time = time.time()

    # Print the current time
    print("Current time:", time.strftime("%Y-%m-%d %H:%M:%S"))

    # Print the message
    print("Keep coding in Python!")

    # Sleep for 3 seconds
    time.sleep(3)

    # Get the time after sleeping
    end_time = time.time()

    # Calculate the time difference
    time_diff = end_time - start_time

    # Print the time difference
    print(f"Time difference: {time_diff} seconds\n")