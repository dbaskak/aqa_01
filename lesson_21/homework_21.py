from datetime import datetime


def analyze_heartbeat(log_file, key="Key TSTFEED0300|7E3E|0400"):
    # Create an empty list to store filtered lines containing the specified key
    filtered_log = []

    # Read the original log file and filter lines with the specified key
    with open(log_file, 'r') as file:
        for line in file:
            if key in line:
                filtered_log.append(line.strip())

    # Open the output log file for recording the heartbeat analysis
    with open("hb_test.log", "w") as log_file:
        for i in range(len(filtered_log) - 1):
            # Extract the time from the current line
            current_line = filtered_log[i]
            next_line = filtered_log[i + 1]

            # Find the Timestamp and get the next 8 characters representing time
            current_time_str = current_line[current_line.find("Timestamp ") + 10:current_line.find("Timestamp ") + 18]
            next_time_str = next_line[next_line.find("Timestamp ") + 10:next_line.find("Timestamp ") + 18]

            # Convert time strings to datetime objects for calculation
            current_time = datetime.strptime(current_time_str, "%H:%M:%S")
            next_time = datetime.strptime(next_time_str, "%H:%M:%S")

            # Calculate the time difference between the current and next timestamp
            time_difference = (next_time - current_time).total_seconds()
            if time_difference < 0:
                time_difference += 86400  # If crossing midnight, add 24 hours (86400 seconds)

            # Log based on time difference criteria
            if 31 < time_difference < 33:
                log_file.write(f"WARNING: Heartbeat delay at {next_time_str}, delay = {time_difference} seconds\n")
            elif time_difference >= 33:
                log_file.write(f"ERROR: Heartbeat delay at {next_time_str}, delay = {time_difference} seconds\n")


# Run the function with the provided log file
analyze_heartbeat("hblog.txt")