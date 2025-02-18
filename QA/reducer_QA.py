#!/usr/bin/env python3
import sys
from collections import defaultdict

hourly_ip_counts = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    hour, ip, count = line.strip().split("\t")
    hourly_ip_counts[hour][ip] += int(count)

for hour, ip_counts in sorted(hourly_ip_counts.items()):
    top_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    print(f"Hour: {hour}")
    for ip, count in top_ips:
        print(f"{ip}\t{count}")
