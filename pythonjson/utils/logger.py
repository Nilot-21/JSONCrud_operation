import sys
sys.path.append('C:/Users/Appu/Desktop/pythonjson/crud')
import select_ope
import datetime 
import insert_ope
import update_ope
import delete_ope
# select_ope.select_data()

def read_log():
    filename1=datetime.datetime.now()
    res=select_ope.select_data()
    if(res==True):
        with open('C:/Users/Appu/Desktop/pythonjson/logs/'+filename1.strftime("%d%m%Y")+".txt","a") as file:
            file.write("particular json is selected")

def write_log():
    filename2=datetime.datetime.now()
    # detail={"organization": "Infosys",
    #     "city": "Bangalore",
    #     "country": "India"}
    res=insert_ope.insert_data()
    # print("working.....")
    if(res==True):
        with open('C:/Users/Appu/Desktop/pythonjson/logs/'+filename2.strftime("%d%m%Y")+".txt","w") as file:
            file.write("particular json is inserted")

       
def update_log():
    filename3=datetime.datetime.now()
    res=update_ope.update_detail()
    if(res==True):
        with open('C:/Users/Appu/Desktop/pythonjson/logs/'+filename3.strftime("%d%m%Y")+".txt","a") as file:
            file.write("particular json is upated")

def delete_log():
    filename4=datetime.datetime.now()
    delete_ope.delete_item()
    with open('C:/Users/Appu/Desktop/pythonjson/logs/'+filename4.strftime("%d%m%Y")+".txt","a") as file:
            file.write("particular json is deleted")

write_log()