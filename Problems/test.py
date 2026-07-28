"""SurprisingVote"""
total = float(input())
maximum = float(input())
others = total - maximum
minimum = max(0, others - maximum)
print(minimum)