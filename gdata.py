#gdata - get data
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
        while cs!="\n" and len(line)!=0:
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
        if cid!='':
            end.update({cid: {"alvl":alvl,"name": name, "email": email, "passwd": passwd}})

    return end

#get free id
def getfid():
    # finding id, lid - list of id
    all=getdata()
    #get all ids in one list
    lid=list(all.keys())

    #cheking for some free ids in the middle of datdbase
    d = int(lid.pop())
    c=0; a=d
    while len(lid):
        if c%2:
            a = int(lid.pop())
        if c%2==0:
            b = int(lid.pop())
        if a-b!= 1 and c%2==0:
            return b+1
        elif b-a!=1 and c%2:
            return a+1
        #if no free ids in the middle of database get free id in the end of database
        else:return int(d+1)
        c+=1
    else:return d+1

#save input if type(t) bool and return False all ok else not
def savech(t: str,text: str,bl=["~"]):
    match t:
        case "bool":
            if text=="0" or text.lower()=="false":
                return False
            else:
                return bool(text)

        case "int":
            try:
                text = int(text)
                return text
            finally:
                return False

        case "float":
                try:
                    text=float(text)
                    return text
                finally:
                    return False

        case "str":
            text = text.lower()
            for i in bl:
                i = str(i)
                if text.find(i.lower()) != -1:
                    return False
            return text
