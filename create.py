import csv
import tkinter as tk
from tkinter import IntVar, ttk
import random
import check
from playsound import playsound
from time import strftime,sleep
from datetime import date, datetime
def read_user():
    list_users = list()
    list_password = list()
    with open('user.txt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            list_users.append(row[0])
            list_password.append(row[1])
    return list_users
def create_user():
    list_users = read_user()
    input_register_user = ent_register_user.get()
    input_register_password = ent_register_password.get()    
    input_repassword = ent_repassword.get()
    if len(input_register_user) > 0 and len(input_register_password) > 0 and len(input_repassword) > 0 : 
        if check.is_exist_user(list_users,input_register_user) != -1:
            lbl_notice.config(text = 'User is Exist')
        else:
            if input_register_password == input_repassword:
                with open('user.txt', mode='a',newline='') as f:
                    writer = csv.writer(f, delimiter=',')
                    writer.writerow([input_register_user,input_register_password])
                #tao ham` viet vao file neu dang ky thanh cong
                lbl_notice.config(text = 'Create Account Success')
            else :
                lbl_notice.config(text = 'incorrect Re-password')
    else:
        lbl_notice.config(text='You must enter full')
def Register_Screen():
    register_screen = tk.Tk()
    register_screen.title('Register Window')
    register_screen.resizable(width=False,height=False)
    lbl_register = tk.Label(register_screen,text = 'Create Account')

    global lbl_notice,ent_register_user,ent_register_password,ent_repassword # de chinh sua text sau khi an button create
    lbl_notice = tk.Label(register_screen,text = 'Please Enter your information!')
    lbl_register_user = tk.Label(register_screen,text = 'Username')
    lbl_register_password = tk.Label(register_screen,text = 'Password')
    lbl_repassword = tk.Label(register_screen,text = 'Re-Password')

    ent_register_user = tk.Entry(register_screen)
    ent_register_password = tk.Entry(register_screen,show = '*')
    ent_repassword = tk.Entry(register_screen,show = '*')

    btn_create_account = tk.Button(register_screen,text = 'Create Account',command=create_user,relief=tk.RAISED)
    
    lbl_register.grid(row=0,column=2,sticky='W')
    lbl_notice.grid(row=1,column=2,sticky='W')
    lbl_register_user.grid(row=2,column=1,sticky='W')
    lbl_register_password.grid(row=3,column=1,sticky='W')
    lbl_repassword.grid(row=4,column=1,sticky='W')

    ent_register_user.grid(row=2,column=2,sticky='W')
    ent_register_password.grid(row=3,column=2,sticky='W')
    ent_repassword.grid(row=4,column=2,sticky='W')

    btn_create_account.grid(row=5,column=2,sticky='W')

    register_screen.mainloop()

def Widget_Screen():
    global widget_screen
    widget_screen =tk.Tk()
    widget_screen.title('Widget Menu')     
    widget_screen.resizable(width=False,height=False)

    btn_alarm = tk.Button(master=widget_screen,text = 'Alarm',command = main_clock,relief=tk.RAISED,border=1,width=10,height=5,bg ="#"+ "%06x"%random.randint(0,0xFFFFFF))
    btn_digital_clock = tk.Button(master=widget_screen,text = 'Digital Clock',command=Digital_Clock,relief=tk.RAISED,border=1,width=10,height=5,bg ="#"+ "%06x"%random.randint(0,0xFFFFFF))
    btn_logout = tk.Button(master=widget_screen,text = 'Exit & Log Out',command = logout,relief=tk.RAISED,border=1,width=10,height=5,bg ="#"+ "%06x"%random.randint(0,0xFFFFFF))

    btn_alarm.grid(row=1, column=1,padx = 20, pady = 20)
    btn_digital_clock.grid(row=1, column=2,padx = 20, pady = 20)
    btn_logout.grid(row=1, column=3,padx = 20, pady = 20)

    widget_screen.mainloop()
#========================#Digital clock
def Digital_Clock():
    clock = tk.Tk()
    clock.title('Digital Clock')
    global lbl_clock
    lbl_clock = tk.Label(clock, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
    lbl_clock.pack(anchor = 'center')
    time()
    clock.mainloop()
def time():
    string = strftime('%H:%M:%S %p')
    lbl_clock.config(text = string)
    lbl_clock.after(1000, time)
def logout():
    with open('check_remember.txt', mode='w',newline='\n') as f:
        f.write('0')
    widget_screen.destroy()

#======================# Alarm
def WeekDay():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    today = datetime.today()
    wd = days[date.weekday(today)]
    string = str(wd)+strftime(',%B-%d-%Y')
    lbl_today.config(text = string)
    lbl_today.after(1000, WeekDay)

def main_clock():
    global Alarm_Screen
    global bot
    Alarm_Screen = tk.Tk()
    Alarm_Screen.title('Alarm Clock')
    Alarm_Screen.geometry('380x200')

    top = ttk.Frame(Alarm_Screen)
    top.pack(fill=tk.X)

    bottom = ttk.Frame(Alarm_Screen)
    bottom.pack(side=tk.BOTTOM)

    lbl_mainclock = ttk.Label(top,text = ' Alarm CLock',font=('calibri',25, 'bold'))
    lbl_mainclock.pack(anchor=tk.CENTER)

    global lbl_today
    lbl_today = tk.Label(top, font = ('Time New Roman', 12, 'bold'))
    lbl_today.pack(anchor=tk.CENTER)
    WeekDay()

    bot = ttk.Frame(Alarm_Screen)
    bot.pack(fill=tk.X)

    global ent_hour,ent_min
    ent_hour = ttk.Entry(bot)
    ent_min = ttk.Entry(bot)
    chx_on =tk.Checkbutton(bot,text = 'ON',command = isAlarm)
    ent_hour.grid(row=1, column=1,sticky='W')
    ent_min.grid(row=1, column=2,sticky='W')
    chx_on.grid(row=1, column=3,sticky='W')
    # global sb_hour,sb_minute
    # sb_hour = ttk.Spinbox(bot,from_=0, to=23)
    # sb_minute = ttk.Spinbox(bot,from_=0,to=59)

    # sb_hour.grid(row=1, column=1,sticky='W')
    # sb_minute.grid(row=1,column=2,sticky='W')

    # global on,off
    # on = tk.PhotoImage(file = "on.png")
    # off = tk.PhotoImage(file = "off.png")
    # global btn_stat
    # btn_stat = tk.Button(bot, image = off,command = switch) #nut bat tat bao thuc
    # btn_stat.grid(row=1,column=3,sticky='W')
    Alarm_Screen.mainloop()

# is_on = False               
# def switch():           #doi trang thai sau khi an nut bat tat
#     global is_on
#     if is_on:
#         btn_stat.config(image = off,fg = "red")
#         is_on = False
#     else:     
#         btn_stat.config(image = on,fg = "green")
#         is_on = True
#         global alarm_hour,alarm_min
#         alarm_hour = sb_hour.get()
#         alarm_min = sb_minute.get()
#         isAlarm(alarm_hour,alarm_min)
def isAlarm():
    AlarmHour = ent_hour.get()
    AlarmMin = ent_min.get()
    Alarm_Screen.withdraw()
    widget_screen.withdraw()
    print(AlarmHour,AlarmMin)
    while True:
        now = datetime.now()
        print(now.hour,now.minute,now.second)
        if now.hour==int(AlarmHour) :
            if now.minute==int(AlarmMin):
                print('Wakeup')
                playsound('AlarmSound.mp3')
                break
        sleep(1)
