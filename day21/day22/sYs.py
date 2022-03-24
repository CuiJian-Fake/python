import sys
import time
# a=0
# if a==1:
#     exit(1)
# print(sys.platform)
# print(sys.argv)
for i in range(10):
    sys.stdout.write('#')
    time.sleep(0.1)
    sys.stdout.flush()