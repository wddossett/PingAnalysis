
import sys
import os
import pingparsing
import re


regex = r"^(.{3}) ([0-9]{2}\/[0-9]{2}\/[0-9]{4}) ([0-9]{2}:[0-9]{2}:[0-9]{2}).+?time.([0-9]{2})+"
with open("c:\\temp\\log_usdby1-netvault.log") as f:
    for x in range(0,2):
        next(f)
    for line in f:
         print(line)
         matches = re.findall(regex, line)
         if matches: 
             print(matches[0][0] + "\n")
             print(matches[0][1] + "\n")
             print(matches[0][2] + "\n")
             print(matches[0][3] + "\n")