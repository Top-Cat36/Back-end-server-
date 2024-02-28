import gdata as g
#wdata - work with data
#sort data for optimization
def datasort(data:dict):
    #sl - sorted list of keys, ndata - new data
    bv=data.keys()
    sl=list()
    #convert sl to int then sort
    for i in bv:
        sl.append(int(i))
    sl.sort()
    ndata={}
    #using sorted key to get value then recrete dict
    for i in sl:
        a=data.pop(str(i))
        ndata.update({str(i):a})
    return ndata

#rewrite database
def dwrite(data):
    data=datasort(data)
    #delete all
    database=open("data.txt","w")
    #writing
    for i in data:
        d=data[i]
        w=str(i)+"~"+d["alvl"]+"~"+d["name"]+"~"+d["email"]+"~"+d["passwd"]+"\n"
        database.write(w)

#create new user
def cruser(alvl:int,nalvl:int,name:str,email:str,passwd:str):
    all=g.getdata()
    #name cheking
    if name=="" and email=="":
        return "please enter your name and emai right"
    for i in all:
        ur = all[i]
        if name == ur["name"] or email == ur["email"]:
            return "user whit this name or email already exists"

    #access level cheking
    match alvl:
        case 0:nalvl=str(1)
        case 1:nalvl=str(1)
        case 2:
            if nalvl<=1 and nalvl>=0:
                nalvl=str(nalvl)
        case 3:
            if nalvl <= 2 and nalvl >= 0:
                nalvl = str(nalvl)

    #id
    cid=g.getfid()

    #password cheking
    if passwd=="":
        return "please enter normal password"

    # creating
    all.update({cid: {"alvl":nalvl,"name": name, "email": email, "passwd": passwd}})
    print(all)
    dwrite(all)
    #cheking successful creat
    data=g.getdata()
    for i in data:
        if i==cid:
            return "successfully"
    return "error"

#delete user, bv - buffer variable
def deluser(alvl:int,udata):
    #access denied for not admins
    if alvl>1:
        #start matching variables with data
        data=g.getdata()
        for i in data:
            bv=data[i]
            #trying to match as int(id)
            try:
                nudata=int(udata)
                #if it matched
                if nudata==int(i):
                    #cheking access
                    if alvl>int(bv["alvl"]):
                        #deliting and rewriting
                        data.pop(i)
                        dwrite(data)
                        #cheking is it in database if it is - error
                        data=g.getdata()
                        for i2 in data:
                            if i==i2:
                                return "error"
                        return "successfully deleted"
                    else:return "access denied"
            #trying to match as str(name, email)
            finally:
                if udata==bv["name"] or udata==bv["email"]:
                    # cheking access
                    if alvl > bv["alvl"]:
                        # deliting and rewriting
                        data.pop(i)
                        dwrite(data)
                        # cheking is it in database if it is - error
                        data=g.getdata()
                        for i2 in data:
                            bv=data[i2]
                            if udata==bv["name"] or udata==bv["email"]:
                                return "error"
                        return  "successfully deleted"
                    else:
                        return "access denied"
        return "wrong user id/name/email"
    else:return "access denied"