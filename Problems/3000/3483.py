'''Team'''
def myteam():
    '''Team'''
    n, m = map(int,input().split())
    if not 1<=n<=10 or not 1<=m<=20:
        print('Data Incorrect')
        return
    total = 0
    teams = []
    for _ in range(n):
        data = list(map(int,input().split()))
        teams.append(data)

    for i, team in enumerate(teams):
        total += sum(team)
        print(f"Team {i+1}: Average = {sum(team)/m:.2f}, Max = {max(team)}")
    print(f"Total Score of All Teams = {total}")
myteam()
