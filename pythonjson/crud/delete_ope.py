import json

def delete_item(filename='data/user.json'):
    with open(filename) as file:
        temp=json.load(file)
    str=input("Enter the organization/city/India u want to delete")
    for x in range(len(temp)):
        if temp[x]["organization"]==str or temp[x]["city"]==str or temp[x]["country"]==str:
            temp.pop(x)
            break
    print(temp)
    print("succefully deleted")
    with open(filename,'w') as file:
        json.dump(temp,file,indent=4)