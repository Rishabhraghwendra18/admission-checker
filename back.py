import json
import sqlite3 as sql
def check_json():
    with open("coll_data.json") as c:
        data=json.loads(c)
        return data

def check_sql():
    # with open('coll_sql.db') as c:
    #     s=c.cursor()
    #     s.execute("SELECT 'coll_web' FROM 'collist' ")
    #     return s.fetchall()
    conn=sql.connect('coll_sql.db')
    c=conn.cursor()
    c.execute("SELECT 'coll_Web' FROM 'collist1' ")
    conn.commit()
    conn.close()
    


def write_sql(counselling):
    if counselling=='JAC-Delhi':
        website='https://jacdelhi.nic.in/WebInfo/Page/Page?PageId=1&LangId=P'
    elif counselling=='JOSSA':
        website='https://jacdelhi.nic.in/WebInfo/Page/Page?PageId=1&LangId=P'
    else:
        website='https://jacdelhi.nic.in/WebInfo/Page/Page?PageId=1&LangId=P'
    conn=sql.connect('coll_sql.db')
    c=conn.cursor()
    c.execute("INSERT INTO collist1 VALUES (:name,:web)",{'name':counselling,'web':website})
    conn.commit()
    conn.close()
           

     
    
                

