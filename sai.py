# GUIBasic2-Expense.py
from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime
# ttk is theme of Tk

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย by Uncle Sai')
GUI.geometry('500x600+500+50')

'''
style = ttk.Style()
style.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [50, 20] },}})

style.theme_use("MyStyle")
'''

Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)

expenseicon = PhotoImage(file='expense.png')
listicon = PhotoImage(file='list.png')



'''
# f'{"tab short": ^50s}
# f'{"tab longgggggggggg": ^50s}'

https://stackoverflow.com/questions/8450472/how-to-print-a-string-at-a-fixed-width
https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498
>>> f'{"HELLO": <{20}}'
'HELLO               '
>>> f'{"HELLO": >{20}}'
'               HELLO'
>>> f'{"HELLO": ^{20}}'
'       HELLO        '
'''

Tab.add(T1, text=f'{"Add Expense": ^50s}', image=expenseicon,compound='top')
Tab.add(T2, text=f'{"Expense List": ^50s}', image=listicon,compound='top')
#Tab.add(T2, text='Expense List', image=listicon,compound='top')

# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx=50,ipady=20) #.pack() ติดปุ่มเข้ากับ GUI หลัก

F1 = Frame(T1)
F1.place(x=100,y=50)

days = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed':'พุธ',
        'Thu':'พฤหัสบดี',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์'}

def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    quantity = v_quantity.get()
    total = int(price) * int(quantity)
    # .get() คือดึงค่ามาจาก v_expense = StringVar()
    print('รายการ: {} ราคา: {}'.format(expense,price))
    print('จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total))
    # clear ข้อมูลเก่า
    v_expense.set('')
    v_price.set('')
    v_quantity.set('')

    # บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
    today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
    print(today)
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dt = days[today] + '-' + dt
    with open('savedata.csv','a',encoding='utf-8',newline='') as f:
        # with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
        # 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
        # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
        fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
        data = [dt,expense,price,quantity,total]
        fw.writerow(data)

    # ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
    E1.focus()

# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = (None,20) # None เปลี่ยนเป็น 'Angsana New'


centerimg = PhotoImage(file='wallet.png')
logo = ttk.Label(F1,image=centerimg)
logo.pack()


#------text1--------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#-------------------

#------text2--------
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#-------------------

#------text3--------
L = ttk.Label(F1,text='จำนวน (ชิ้น)',font=FONT1).pack()
v_quantity = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#-------------------

saveicon = PhotoImage(file='save.png')

B2 = ttk.Button(F1,text='Save',command=Save,image=saveicon,compound='left')
B2.pack(ipadx=10,ipady=15,pady=15)

GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
