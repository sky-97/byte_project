import sqlite3
import pandas as pd


def manual_list(role):
    if role == 'datascience':
        temp = pd.read_csv("DS.csv")
        temp = temp[['skills','values']].set_index('skills')
        return temp.to_dict()['values']
    elif role == 'fullstack':
        temp = pd.read_csv("FSD.csv")
        temp = temp[['skills','values']].set_index('skills')
        return temp.to_dict()['values']
    return 
    
    # temp['skills'].to_list(),temp['values'].to_list(), 

def get_manual_score(selected_skills, skill_dict):
    score = 0
    for skill in selected_skills:
        score = score + skill_dict[skill]
    return score


def init_db():
    conn = sqlite3.connect('skill.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM fullstacktable")
    except:
        c.execute("""create table fullstacktable (name TEXT,id REAL)""")
    conn.commit()
    conn.close()

def show():
    conn=sqlite3.connect('skill.db')
    c=conn.cursor()
    full_stack_results=c.execute("SELECT * FROM fullstacktable;")
    python_list=[]
    for item in full_stack_results:
        python_list.append([item[1]])
    return python_list

def datasci():
    conn=sqlite3.connect('skill.db')
    c=conn.cursor()
    data=c.execute("SELECT * from datascience datascience;")
    science = []
    for item in data:
        science.append([item[1]])
    return science

def get_score(players):
    conn = sqlite3.connect('skill.db')
    c = conn.cursor()
    l = []
    for item in players:
        value = c.execute("SELECT [value] FROM fullstacktable WHERE [name]=(:uname)",{'uname':item}).fetchall()
        # print(type(value))
        l.extend(value)
    # print(type(l))
    s = 0
    for i in l:
        s+=sum(i)
    return s

if __name__=='__main__':
    temp= manual_list(role='fullstack')
    print(temp)
    # print(val)
    # init_db()
