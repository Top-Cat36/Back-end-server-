import data as d
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
        all=d.getdata()
        #if (uname or email) match whith password login, ur - user
        for i in all:
            ur=all[i]
            if name==ur["name"] or email == ur["email"]:
                if passwd==ur["passwd"]:
                    user.__init__(self,cid=ur, alvl=ur["alvl"], name=ur["name"],email=ur["email"],passwd=ur["passwd"] )
                    return "completed successful, now you are:"+str(name)
                else:return "wrong password"
        return "no user whith this name"+str(name)
