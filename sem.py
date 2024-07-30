import streamlit as sl
import pandas as pd
import datetime
import math
import csv
def grade_point(n):
    if n=="A+":
        return 10
    elif n=="A":
        return 9
    elif n=="B":
        return 8
    elif n=="C":
        return 7
    elif n=="D":
        return 6
    elif n=="E":
        return 5
    else:
        return 0
def calculate(l):
    with open("marks.csv","r") as f:
        x=csv.reader(f)
        data=list(x)
        l1=[]
        for j in l:
            count=0
            g=[grade_point(i[4])*float(i[5]) for i in data if i[0] ==j]
            c=[float(i[5]) for i in data if i[0]==j]
            if(sum(c)==21.5):
                count+=1
                string="pass"
            else:
                string="fail"
            grade=("%.2f"%(sum(g)/21.5))
            p=(float(grade)-0.75)*10
            percentage=("%.2f"%p)
            l1.append([j,grade,percentage,string])
        s_l1=sorted(l1,key=lambda x: x[2],reverse=True)
        for i in range(len(s_l1)):
                if(roll==str(s_l1[i][0])):
                    if(s_l1[i][3]=="pass"):
                        sl.write("Congratulations you have passed in all of your exams")
                        sl.write(f"YOU HAVE SECURED {s_l1.index(s_l1[i])+1}th position")
                        sl.success(f"{s_l1[i][0]} --> CGPA={s_l1[i][1]}, percentage={s_l1[i][2]}")
                    else:
                        sl.write("sorry you have failed")
                        sl.write(f"YOU HAVE SECURED {s_l1.index(s_l1[i])+1}th position in the department")
                        sl.error(f"{s_l1[i][0]} --> CGPA={s_l1[i][1]}, percentage={s_l1[i][2]}")
        t=pd.DataFrame({"Roll Number":[s_l1[i][0] for i in range(len(s_l1))], "SGPA":[s_l1[i][1] for i in range(len(s_l1))],
                        "Percentage":[s_l1[i][2] for i in range(len(s_l1))],"status":[s_l1[i][3] for i in range(len(s_l1))]})
        t = t.set_index([pd.Index([i for i in range(1,len(s_l1)+1)])])
        return t

def calculate2(l):
    with open("marks.csv","r") as f:
        x=csv.reader(f)
        data=list(x)
        l1=[]
        for j in l:
            count=0
            g=[grade_point(i[4])*float(i[5]) for i in data if i[0]==j]
            c=[float(i[5]) for i in data if i[0]==j]
            if(sum(c)==21.5):
                count+=1
                string="pass"
            else:
                string="fail"
            grade=("%.2f"%(sum(g)/21.5))
            p=(float(grade)-0.75)*10
            percentage=("%.2f"%p)
            with open("ACCENTURE_FACEPREP_DATA(1).csv","r") as f1:
                x1=csv.reader(f1)
                a=list(x1)
                for k in a:
                    if k[9]==j:
                        name=k[0]+" "+k[1]+" "+k[2]
                        type=k[8]
                        l1.append([j,name,type,grade,percentage,string])
        s_l1=sorted(l1,key=lambda x: x[3],reverse=True)
        for i in range(len(s_l1)):
                if(roll==str(s_l1[i][0])):
                    if(s_l1[i][5]=="pass"):
                        sl.write(f"Congratulations {s_l1[i][1]} you have passed in all of your exams")
                        sl.write(f"YOU HAVE SECURED {s_l1.index(s_l1[i])+1}th position")
                        sl.success(f"{s_l1[i][0]} --> CGPA={s_l1[i][3]}, percentage={s_l1[i][4]}")
                    else:
                        sl.write(f"sorry {s_l1[i][1]} you have failed")
                        sl.write(f"YOU HAVE SECURED {s_l1.index(s_l1[i])+1}th position in the department")
                        sl.error(f"{s_l1[i][0]} --> CGPA={s_l1[i][3]}, percentage={s_l1[i][4]}")
        t=pd.DataFrame({"Roll Number":[s_l1[i][0] for i in range(len(s_l1))],"Name":[s_l1[i][1] for i in range(len(s_l1))],
                        "Type":[s_l1[i][2] for i in range(len(s_l1))],"SGPA":[s_l1[i][3] for i in range(len(s_l1))],                            
                        "Percentage":[s_l1[i][4] for i in range(len(s_l1))],"status":[s_l1[i][5] for i in range(len(s_l1))]})
        t = t.set_index([pd.Index([i for i in range(1,len(s_l1)+1)])])
        return t


sl.title("CGPA of KIET AI-ML in the III-I sem")
roll=sl.text_input("enter your roll number in caps",max_chars=10)
select=sl.selectbox("Choose your option",options=("All students","Students who qualified for accenture"))
l=['21B21A4201', '21B21A4202', '21B21A4203', '21B21A4204', '21B21A4205', '21B21A4206', '21B21A4207', '21B21A4208',
            '21B21A4209', '21B21A4210', '21B21A4211', '21B21A4212', '21B21A4213', '21B21A4214', '21B21A4215', '21B21A4216', 
            '21B21A4217', '21B21A4218', '21B21A4219', '21B21A4220', '21B21A4221', '21B21A4222', '21B21A4223', '21B21A4224', 
            '21B21A4225', '21B21A4226', '21B21A4227', '21B21A4228', '21B21A4229', '21B21A4230', '21B21A4231', '21B21A4232', 
            '21B21A4233', '21B21A4234', '21B21A4235', '21B21A4236', '21B21A4237', '21B21A4238', '21B21A4239', '21B21A4240', 
            '21B21A4241', '21B21A4242', '21B21A4243', '21B21A4244', '21B21A4245', '21B21A4246', '21B21A4247', '21B21A4248', 
            '21B21A4249', '21B21A4250', '21B21A4251', '21B21A4252', '21B21A4253', '21B21A4254', '21B21A4255', '21B21A4256', 
            '21B21A4257', '21B21A4258', '21B21A4259', '21B21A4260', '21B21A4261', '21B21A4262', '21B21A4263', '21B21A4264', 
            '21B21A4265', '21B21A4266', '21B21A4267', '21B21A4268', '21B21A4269', '21B21A4270', '21B21A4271', '21B21A4272', 
            '21B21A4273', '21B21A4274', '21B21A4275', '21B21A4276', '21B21A4277', '21B21A4278', '21B21A4280', '21B21A4281', 
            '21B21A4282', '21B21A4283', '21B21A4284', '21B21A4285', '21B21A4286', '21B21A4287', '21B21A4288', '21B21A4289', 
            '21B21A4290', '21B21A4291', '21B21A4292', '21B21A4293', '21B21A4294', '21B21A4295', '21B21A4296', '21B21A4297', 
            '21B21A4298', '21B21A4299', '21B21A42A0', '21B21A42A1', '21B21A42A2', '21B21A42A3', '21B21A42A4', '21B21A42A5', 
            '21B21A42A6', '21B21A42A7', '21B21A42A8', '21B21A42A9', '21B21A42B0', '21B21A42B1', '21B21A42B2', '21B21A42B3', 
            '21B21A42B4', '21B21A42B5', '21B21A42B6', '21B21A42B7', '21B21A42B8', '21B21A42B9', '21B21A42C0', '21B21A42C1', 
            '21B21A42C2', '21B21A42C3', '21B21A42C4', '21B21A42C5', '21B21A42C6', '21B21A42C7', '21B21A42C8', '21B21A42C9', 
            '21B21A42D0', '21B21A42D1', '21B21A42D2', '21B21A42D3', '21B21A42D4', '21B21A42D5', '21B21A42D6', '21B21A42D7', 
            '21B21A42D8', '21B21A42D9', '21B21A42E0', '21B21A42E1', '21B21A42E2', '21B21A42E3', '21B21A42E4', '21B21A42E5']
        
if(select=="All students"):
    t=calculate(l)
    sl.table(t)
if(select=="Students who qualified for accenture"):
    t=calculate2(l)
    sl.table(t)