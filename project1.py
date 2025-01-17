import mysql.connector
mydb = mysql.connector.connect(host='localhost', password='crk@44457778', user='root', database='quiz')
mycursor=mydb.cursor()

print("Welcome to  the Quiz ")
print(" The topics are: ")
l=['1.Mythology','2.Sports','3.Superhero','4.Science','5.Politics']
for i in range(0,5):
    if i<4:
        print(l[i], end='                                   ')
    else:
        print(l[i])

def input_player():
    global name
    name=input("Enter your name: ")
    app=int(input("Enter the no. of appearances made(already attempted): "))
    if app < 1:
        mycursor.execute(f"Create table {name} ( slno int primary key, topic varchar(15), score int)")
    else:
        print("Table already exists")

ch=int(input("Enter the number to choose topic: "))    

def play_quiz():
    global score
    global code
    if ch==1:
        score=0
        mycursor.execute("select * from mythology")
        Q = mycursor.fetchall()
        for i in Q:
            print(i)
            A = input("Enter your answer:")
            n = 1
            code = "myt"+str(n)
            mycursor.execute("select * from ans_key")
            An=mycursor.fetchall()
            for x in An:
                ans = x[1]
                n=n+1
                if A.upper()==ans.upper():
                    score+=1
                    
    elif ch==2:
        score=0
        mycursor.execute("select * from sports")
        Q = mycursor.fetchall()
        for i in Q:
            print(i)
            A = input("Enter your answer:")
            n = 1
            code = "sp"+str(n)
            mycursor.execute("select * from ans_key")
            An=mycursor.fetchall()
            for x in An:
                ans = x[1]
                n=n+1
                if A.upper()==ans.upper():
                    score+=1
                
    elif ch==3:
        score=0
        mycursor.execute("select * from superhero")
        Q = mycursor.fetchall()
        for i in Q:
            print(i)
            A = input("Enter your answer:")
            n = 1
            code = "sh"+str(n)
            mycursor.execute("select * from ans_key")
            An=mycursor.fetchall()
            for x in An:
                ans = x[1]
                n=n+1
                if A.upper()==ans.upper():
                    score+=1
        
    elif ch==4:
        score=0
        mycursor.execute("select * from science")
        Q = mycursor.fetchall()
        for i in Q:
            print(i)
            A = input("Enter your answer:")
            n = 1
            code = "sc"+str(n)
            mycursor.execute("select * from ans_key")
            An=mycursor.fetchall()
            for x in An:
                ans = x[1]
                n=n+1
                if A.upper()==ans.upper():
                    score+=1
    elif ch==5:
        score=0
        mycursor.execute("select * from politics")
        Q = mycursor.fetchall()
        for i in Q:
            print(i)
            A = input("Enter your answer:")
            n = 1
            code = "po"+str(n)
            mycursor.execute("select * from ans_key")
            An=mycursor.fetchall()
            for x in An:
                ans = x[1]
                n=n+1
                if A.upper()==ans.upper():
                    score+=1
    else:
        print("Wrong option! ")

    return score


def update_result():
    mycursor.execute(f'select * from {name}')
    data=mycursor.fetchall()
    r=mycursor.rowcount
    if ch == 1:
        mycursor.execute(f"insert into {name} values({r}+1, 'mythology',{score})")
    elif ch==2:
        mycursor.execute(f"insert into {name} values({r}+1, 'Sports',{score})")
    elif ch==3:
        mycursor.execute(f"insert into {name} values({r}+1, 'superhero',{score})")
    elif ch==4:
        mycursor.execute(f"insert into {name} values({r}+1, 'Science',{score})")
    elif ch==5:
        mycursor.execute(f"insert into {name} values({r}+1, 'politics',{score})")


def  display_result():
    print("Dear", name, 'your score is: ', score)

def display_answer():
    if ch == 1:
        mycursor.execute("select * from ans_key where code like 'myt%'")
        data = mycursor.fetchall()
        print(data)
    elif ch == 2:
        mycursor.execute("select * from ans_key where code like 'sp%'")
        data = mycursor.fetchall()
        print(data)
    elif ch == 3:
        mycursor.execute("select * from ans_key where code like 'sh%'")
        data = mycursor.fetchall()
        print(data)
    elif ch == 4:
        mycursor.execute("select * from ans_key where code like 'sc%'")
        data = mycursor.fetchall()
        print(data)
    elif ch == 5:
        mycursor.execute("select * from ans_key where code like 'po%'")
        data = mycursor.fetchall()
        print(data)
    else:
        print("Wrong input found")

input_player()
play_quiz()
display_result()
display_answer()
update_result()

mydb.commit()
mydb.close()

print("Thank you for joining us")
