#!/usr/bin/env python3
import re
import sys

log_pattern = re.compile(r'^(\S+) - - \[\d{2}/\w+/\d{4}:(\d{2}):\d{2}:\d{2}')

for line in sys.stdin:
    match = log_pattern.search(line)
    if match:
        ip = match.group(1)
        hour = match.group(2)

        print(f"{hour}\t{ip}\t1")