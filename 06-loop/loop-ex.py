#!/usr/bin/env python3
# -*- encoding : utf-8 -*-

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        pass
        print('pass')
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
