'''Shorten'''
num_list = []
while True:
    number = int(input())
    if number == -1:
        break
    num_list.append(number)
if not num_list:
    pass
else:
    set_list = []
    start_num = num_list[0]
    end_num = num_list[0]
    LENGTH = len(num_list)
    for i in range(1, LENGTH):
        print(num_list[i], start_num, end_num)
        if num_list[i] == end_num + 1:
            end_num = num_list[i]
        else:
            if start_num == end_num:
                set_list.append(str(start_num))
            else:
                set_list.append(f"{start_num}-{end_num}")
            start_num = num_list[i]
            end_num = num_list[i]
    if start_num == end_num:
        set_list.append(str(start_num))
    else:
        set_list.append(f"{start_num}-{end_num}")
    print(", ".join(set_list))
