
#geting data to authenticate user
#ofile - open file
def ofile():
    # opening database file if it is not found - create new
    try:
        database = open("data.txt")
    except FileNotFoundError:
        database = open("data.txt", "w")
        database.close()
        database = open("data.txt")
    return database

#rewrite database
def dwrite(data):
    #delete all
    database=open("data.txt","w")
    #writing
    for i in data:
        d=data[i]
        database.write(str(i)+"~"+d["alvl"]+"~"+d["name"]+"~"+d["email"]+"~"+d["passwd"])

def getdata():
    #variable whith end data
    end={}
    #start work with file
    database=ofile()
    for line in database:
        line = list(line)

        #wariables
        #step - current step, structure of database: cid~alvl~name~email~passwd     one ~ is one step
        step=0
        # cs - current symbol
        cs=0
        # current id
        cid=""
        #access level
        alvl=""
        #name
        name=""
        #email
        email=""
        #password
        passwd=""

        #working whith symbols
        while cs!="\n":
            #geting 1 symbol from file
            cs=line.pop(0)
            cs=str(cs)
            #cheking that current symbol is not special
            if cs!="\n" and cs!="~":
                match step:
                    #cheking what step of geting data from line then add symbol to match variable
                    case 0:cid+=cs
                    case 1:alvl+=cs
                    case 2:name+=cs
                    case 3:email+=cs
                    case 4:passwd+=cs

            #if cs special(next step)
            elif cs=="~":
                step+=1
        #writing to end variable dato of one user
        end.update({cid: {"alvl":alvl,"name": name, "email": email, "passwd": passwd}})

    return end

#get free id
def getfid():
    # finding id, lid - list of id
    all=getdata()
    lid = []
    #get all ids in one list
    for i in all:
        lid.append(i)

    #cheking for some free ids in the middle of datdbase
    a = lid.pop();
    c=0;d=a
    while c<=d:
        if c%2:
            a=lid.pop()
        if c%2==0:
            b = lid.pop()
        if a-b!= 1 and c%2==0:
            return b+1
        elif b-a!=1 and c%2:
            return a+1
        #if no free ids in the middle of database get frre id in the end of database
        else:return str(d+1)
        c+=1



#create new user
def cruser(alvl:int,nalvl:int,name:str,email:str,passwd:str):
    all=getdata()
    #name cheking
    if name=="" or email=="":
        return "please enter your name and emai right"
    for i in all:
        ur = all[i]
        if name == ur["name"] or email == ur["email"]:
            return "user whit this name or email already exists"

    #access level cheking
    if alvl==2 and nalvl<=2:nalvl=str(nalvl)
    else:return"access level must be < or = your access level"
    if alvl == 0 or alvl == 1: nalvl = "1"
    if alvl == 3: nalvl=str(nalvl)

    #id
    cid=getfid()

    #password cheking
    if passwd=="":
        return "please enter normal password"

    # creating
    all.update({cid: {"alvl":nalvl,"name": name, "email": email, "passwd": passwd}})
    dwrite(all)
    #to do cheking successful creat


