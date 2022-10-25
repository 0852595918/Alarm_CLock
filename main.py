#Tkinter
import csv
import tkinter as tk
import create
import check
from Alarm import * 

def read_user(): #doc file csv chua user password va dua vao list user password, return 2 list de so sanh dang nhap
    list_users = list()
    list_password = list()
    with open('user.txt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            list_users.append(row[0])
            list_password.append(row[1])
    return list_users,list_password
# list_users,list_password = read_user() #in thu list de kiem tra
# print(list_users,list_password)
def check_login(): #kiem tra thong tin dang nhap
    list_users,list_password = read_user() 
    input_user = ent_username.get()
    input_password = ent_password.get()
    if check.is_exist_user(list_users,input_user) != -1 : #kiem tra user da dang ki truoc do chua
        if check.is_corret_password(list_users,list_password,input_user,input_password): #kiem tra mat khau neu user co ton tai
            first_screen.destroy() #xoa login_screen
            create.Widget_Screen() # tao screen widget sau khi dang nhap thanh cong
        else:
            lbl_login.config(text ='Wrong User or Password!!')
    else:
        lbl_login.config(text ='Wrong User or Password!!')     

def black(event):
    btn_register.configure(fg = 'Black')
def blue(event):
    btn_register.configure(fg = 'Blue')

if check.is_remember(): #kiem tra co danh dau vao ghi nho dang nhap o lan dang nhap truoc chua
    create.Widget_Screen() #neu da ghi nho dang nhap thi nhay thang vao screen widget
else:
    first_screen = tk.Tk()
    first_screen.resizable(width = False , height = False)
    first_screen.title('Tam Nguyen Clock')
    lbl_login = tk.Label(first_screen,text = 'Please log in first!!')

    lbl_user = tk.Label(first_screen,text = 'User :')
    lbl_password = tk.Label(first_screen, text = 'Password:')

    ent_username = tk.Entry(first_screen,width=25)
    ent_password = tk.Entry(first_screen,show = '*',width=25)

    btn_login = tk.Button(master = first_screen, text = 'Log in',command = check_login,relief=tk.RAISED,width=5) 
    btn_register = tk.Button(master = first_screen, text = '\u0332'.join('Register'),command=create.Register_Screen,fg = 'Black',relief=tk.FLAT)

    var = tk.IntVar()
    chx_remember = tk.Checkbutton(master = first_screen, text = 'Remember Login',variable = var,command = lambda: check.is_chx(var))
    lbl_login.grid(row = 1 , column = 2,sticky='W')
    lbl_user.grid(row = 2, column = 1,sticky='W')
    lbl_password.grid(row = 3, column = 1,sticky='W')
    ent_username.grid(row = 2, column = 2,sticky='W')
    ent_password.grid(row = 3, column = 2,sticky='W')
    btn_login.grid(row=3,column=4,sticky='W')
    btn_register.grid(row = 5, column = 2,sticky = 'W')
    chx_remember.grid(row = 4,column = 2,sticky = 'W' )

    lbl_space = tk.Label(first_screen,text = '',width= 1).grid(row=3,column=3,sticky='W') #tao khoang cach giua entry password va button login cho dep

    btn_register.bind('<Enter>',blue)
    btn_register.bind('<Leave>',black)
    first_screen.mainloop()