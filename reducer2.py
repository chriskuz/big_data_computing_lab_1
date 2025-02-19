#!/usr/bin/env python
import sys
import os
from collections import defaultdict

start_hour = int(os.environ.get('START', '00'))  # Default to 0
end_hour = int(os.environ.get('END', '17'))  # Default to 17

ip_counts = defaultdict(int)

for line in sys.stdin:
    try:
        hour, ip, count = line.strip().split("\t")
        hour = int(hour)

        if start_hour <= hour < end_hour:
            ip_counts[ip] += int(count)
    except ValueError:
        continue

top_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:3]

print "Top 3 IP addresses for the time period {} to {}:".format(start_hour, end_hour)
for ip, count in top_ips:
    print "{}\t{}".format(ip, count)
