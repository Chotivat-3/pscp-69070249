"""Fare"""
age = int(input())
char = input().lower()
fare = 50
if age < 18 or char == "s":
    fare -= 30
print(fare)
