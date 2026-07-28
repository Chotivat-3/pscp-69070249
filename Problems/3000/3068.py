"""Artid"""
y = int(input())
if not y%4 and y%100 or not y%400 or y <= 1582 and not y%4:
    print("yes")
else:
    print("no")
