#!/usr/bin/env python
import sys
import os
from collections import defaultdict

# Ensure environment variables are correctly converted to integers
try:
    start_hour = int(os.environ.get('START', 0))  # Default to 0
    end_hour = int(os.environ.get('END', 17))  # Default to 17
except ValueError:
    print("Error: Invalid START or END hour values.")
    sys.exit(1)

# Dictionary to store total request count per IP
ip_counts = defaultdict(int)

# Process Mapper Output
for line in sys.stdin:
    try:
        # Split input and ensure proper format
        parts = line.strip().split("\t")
        if len(parts) != 3:
            continue  # Skip malformed lines
        
        hour, ip, count = parts
        hour = int(hour)  # Ensure `hour` is an integer

        # Filter based on the user-specified time period
        if start_hour <= hour < end_hour:
            ip_counts[ip] += int(count)
    except ValueError:
        continue  # Ignore incorrectly formatted lines

# Sort by request count in descending order and get the top 3
top_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:3]

# Print results
print "Top 3 IP addresses for the time period {} to {}:".format(start_hour, end_hour)
for ip, count in top_ips:
    print "{}\t{}".format(ip, count)

