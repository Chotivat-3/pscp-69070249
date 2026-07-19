"""Saitama"""
f_pull = int(input())
f_up = int(input())
f_sit = int(input())
f_run = int(input())
n_pull = int(input())
n_up = int(input())
n_run = int(input())
n_sit = int(input())
def work_out():
    """work_out!!"""
    pull = 0
    up = 0
    run = 0
    sit = 0
    day = 0
    while True :
        pull += n_pull
        up += n_up
        run += n_run
        sit += n_sit
        day += 1
        if pull>=f_pull and up>=f_up and run>=f_run and sit>=f_sit:
            break
    print(day)
work_out()
