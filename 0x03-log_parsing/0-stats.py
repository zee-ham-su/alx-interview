#!/usr/bin/python3
"""  a script that reads stdin
line by line and computes metrics
"""
import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()

        total_size += int(data[-1])

        status_code = int(data[-2])
        status_codes[status_code] += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for key in sorted(status_codes.keys()):
                if status_codes[key] > 0:
                    print("{}: {}".format(key, status_codes[key]))

except Exception as e:
    print(f"Error: {e}")
