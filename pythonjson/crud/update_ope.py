import json

def update_detail(filename='data/user.json'):
    data=[]
    with open(filename) as file:
        temp=json.load(file)
    totalindex=len(temp)-1
    print()
    idx=int(input("enter the index you want to edit"))
    i=0
    for entry in temp:
        if i==idx:
            print(i)
            entry["organization"]=input("enter the organization u want to change to")
            entry["city"]=input("enter the city u want to change to")
            entry["country"]=input("enter the country u want to change to")
            data.append({"name":entry["organization"],"city":entry["city"],"country":entry["country"]})
            i=i+1
            print("succefully updated")
            
        else:
            data.append(entry)
            
            i=i+1
        
    with open(filename,'w') as file:
        json.dump(temp,file,indent=4)

    # upd=input("enter the organization/city/country which u want to change detail")

    # for x in range(len(temp)):
    #     if temp[x]["organization"]==upd:
    #         st="enter the name of organization"
    #         temp.insert({"organization":st})
    #     elif temp[x]["city"]==upd:
    #         st="enter the name of city"
    #         temp.insert(temp[x],{"city":st})    
    #     else:
    #         st="enter the name of country"
    #         temp.insert(temp[x],{"country":st})
    

    