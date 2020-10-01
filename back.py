import json
import sqlite3 as sql
from win10toast import ToastNotifier
def check_json():
    with open("coll_data.json") as c:
        data=json.load(c)
        return data
def write_json(json_file):
    with open('coll_data.json','w') as c:
        json.dump(json_file,c,indent=2)
def check_sql():
    # with open('coll_sql.db') as c:
    #     s=c.cursor()
    #     s.execute("SELECT 'coll_web' FROM 'collist' ")
    #     return s.fetchall()
    conn=sql.connect('coll_sql.db')
    c=conn.cursor()
    c.execute("SELECT * FROM 'collist1' ")
    sql_data=c.fetchall()
    conn.commit()
    conn.close()
    return sql_data
    
def write_sql(counselling):
    if counselling=='JAC-Delhi':
        website='https://jacdelhi.nic.in/WebInfo/Page/Page?PageId=1&LangId=P'
    elif counselling=='JOSSA':
        website='https://jacdelhi.nic.in/WebInfo/Page/Page?PageId=1&LangId=P'
    else:
        website='https://ipu.admissions.nic.in/IpuAdmiss/page/Page?PageId=1&LangId=P'
    conn=sql.connect('coll_sql.db')
    c=conn.cursor()
    c.execute("INSERT INTO collist1 VALUES (:name,:web)",{'name':counselling,'web':website})
    # c.execute("DELETE FROM collist1")
    conn.commit()
    conn.close()           
        
def matching(site_name,text):
    json_data=check_json()
    if text not in json_data[site_name]:
        notifier=ToastNotifier()
        json_data[site_name].append(text)
        write_json(json_data)
        notifier.show_toast(title=site_name+' Update',msg=text +'registration on '+ site_name,duration=7)
        


     
    
                

