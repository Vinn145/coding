import time

for i in range(100):
    print("I love you")
    time.sleep(1)

import time

message = "I love you\n" * 100

for line in message.splitlines():
    print(line)
    time.sleep(1) 
