import gdata as g
class user:
    #cid - current id, name - user name, passwd - password, access level
    def __init__(self,cid,alvl,name,email,passwd):
        self.cid=cid
        self.alvl=alvl
        self.name=name
        self.email=email
        self.passwd=passwd

    #login
    def login(self,name,email,passwd):
        #get all data
        all=g.getdata()
        #if (uname or email) match whith password login, bv - buffer variable
        for i in all:
            bv=all[i]
            if name==bv["name"] or email == bv["email"]:
                if passwd==bv["passwd"]:
                    user.__init__(self,cid=bv, alvl=bv["alvl"], name=bv["name"],email=bv["email"],passwd=bv["passwd"] )
                    return "completed successful, now you are: "+str(name)
                else:return "wrong password"
        return "no user whith this name: "+str(name)