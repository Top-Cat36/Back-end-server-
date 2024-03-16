def main():
    try:
        import user as u
        import gdata as g
        import wdata
        import wdata as w
    except ImportError:
        return "fatall error can't import one or more modules"

    #current user as default guest
    u=u.user("",0,"guest","","")

    print(g.getdata())

    print(u.login("root","","1234"))

    print(wdata.deluser(int(u.alvl),0))

if __name__=="__main__":
    main()