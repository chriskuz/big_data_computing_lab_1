#!/usr/bin/env python
import sys
from collections import defaultdict

hourly_ip_counts = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    try:
        # Split line into 3 parts: hour, IP, count
        hour, ip, count = line.strip().split("\t")
        hourly_ip_counts[hour][ip] += int(count)
    except ValueError:
        # Skip lines that don't have exactly 3 tab-separated fields
        continue

# Process each hour separately
for hour, ip_counts in sorted(hourly_ip_counts.items()):
    # Sort IPs by count in descending order and get top 3
    top_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    print "Hour: {}".format(hour)
    for ip, count in top_ips:
        print "{}\t{}".format(ip, count)
