run_gaame=True
char_1={'name':'Chaos','health':100}
char_2={'name':'Ragnarok','health':100}
gun_1={'name':'AK-47','Mag Size':40,'Damage':75,'mobilty':30}
gun_2={'name':'M416','Mag Size':35,'Damage':60,'mobilty':40}

char_choice=int(input("Select Character.\n1.Chaos\n2.Ragnarok\n"))
gun_choice=int(input("Selcet preffered Gun.\n1. AK-47\n2.M416\n"))
if char_choice==1:
    print("You have selected " +char_1['name'])
    if gun_choice==1:
        char_1["Gun"]=gun_1
        print("Description of chosen gun:\n{}".format(gun_1))
        print(char_1['name']+" is ready with his trusted "+gun_1['name'])
    else:
        char_1["Gun"]=gun_2
        print("Description of chosen gun:\n{}".format(gun_2))
        print(char_1['name']+" is ready with his trusted "+ gun_2['name'])
elif char_choice==2:
    print("You have selected " +char_2['name'])
    if gun_choice==1:
        char_1["Gun"]=gun_1
        print("Description of chosen gun:\n{}".format(gun_1))
        print(char_2['name']+" is ready with his trusted "+gun_1['name'])
    else:
        char_1["Gun"]=gun_2
        print("Description of chosen gun:\n{}".format(gun_2))
        print(char_2['name']+" is ready with his trusted "+ gun_2['name'])
else:
    print("No Character Selected")




