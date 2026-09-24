'''Give U'''

n, s = map(int,input().split())
student = {}
for i in range(n):
    student[i+1]=int(input())

whogive = [s]

for i in range(1,n+1):
    if student[whogive[i-1]] and student[whogive[i-1]] not in whogive :
        whogive.append(student[whogive[i-1]])
    else:
        break
print(len(whogive))
