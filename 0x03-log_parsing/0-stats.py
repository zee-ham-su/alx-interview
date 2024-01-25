#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''


import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            line_count += 1

        if line_count == 10:
            line_count = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted((k, v)
                                     for k, v in cache.items() if v != 0):
                print('{}: {}'.format(key, value))


except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted((k, v) for k, v in cache.items() if v != 0):
        print('{}: {}'.format(key, value))
