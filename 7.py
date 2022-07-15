# Chocolate Distribution Problem

#     Difficulty Level : Easy
#     Last Updated : 07 Nov, 2021

# Given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

#     Each student gets one packet.
#     The difference between the number of chocolates in the packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.

#approach: you sort the array and then traverse in intervals of M to find the least difference.


arr = [int(x) for x in input().split()]
m = int(input())

arr.sort()
n = float('inf')
for i in range(len(arr) - m):
    x = arr[i+m-1] - arr[i]
    n = min(x, n)

print(n)