import csv
def is_chx(main):
    with open('check_remember.txt', mode='w',newline='\n') as f:
        # writer = csv.writer(f, delimiter=',')
        inputvar = main.get()
        f.write(str(inputvar))
        # writer.writerow([inputvar])
        # print(inputvar) #check value checkbox tren terminal
def is_remember():
    with open('check_remember.txt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[0] == '1' :
                return True
            elif row[0] == '0' :
                return False
def is_exist_user(list_users,user):
    if user in list_users:
        length_user = len(list_users)
        for i in range(length_user):
            if str(user) == str(list_users[i]):
                break
        return i
    else: return -1
def is_corret_password(list_users,list_password,user,password):
    # length_user = len(list_users)
    index = is_exist_user(list_users,user)
    if str(user) == str(list_users[index]) and str(password) == str(list_password[index]):
        return True
    else: return False
        