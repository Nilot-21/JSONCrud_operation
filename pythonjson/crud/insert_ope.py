import json

# detail={"organization": "ABCD",
#         "city": "Pune",
#         "country": "India"}

def insert_data(filename='data/user.json'):
    res={}
    with open(filename,'r') as file:
        temp=json.load(file)
    print(type(temp))
    res["organization"]=input("enter the name of organization")
    res["city"]=input("enter the name of city")
    res["country"]=input("enter the name of country")
    temp.append(res)
    with open(filename,'w') as file:
        json.dump(temp,file,indent=4)
    return True

    # with open(filename,'a') as file:
        # json.dump(detail,file,indent=4)


        # li=[]
        # data=json.load(file)
        # for key,value in data.items():
        #     if(key=='organization'):
        #         li.append(value)
        #     elif(key=='city'):
        #         li.append(value)
        #     else:
        #         li.append(value)
                
        # # temp=data["emp_detail"]
        # print(li)
        # json.dump(detail,file,indent=4)
        
       

