from django.shortcuts import render
import mysql.connector as p
from datetime import date
from datetime import timedelta

# Create your views here.
def home(request):
    return render(request,"home.html",{"msg":"select one option"})
def addrec(request):
    return render(request,"addrec.html")
def add (request):
    a=int(request.GET.get("bno"))
    b=request.GET.get("bname")
    c=request.GET.get("author")
    d=int(request.GET.get("qty"))
    e=float(request.GET.get("price"))
    f=request.GET.get("dop")
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("insert into book values({},'{}','{}',{},{},'{}')".format(a,b,c,d,e,f,))   
    con.commit()
    con.close()
    return render(request,"home.html",{'msg':'added'})
def modify(request):
    return render(request,"modify.html")
def modrec(request):
    return render(request,"modrec.html")
def mod(request):
    a=int(request.GET.get("bno"))
    b=request.GET.get("bname")
    c=request.GET.get("author")
    d=int(request.GET.get("qty"))
    e=float(request.GET.get("price"))
    f=request.GET.get("dop")
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("update book set bname='{}',author='{}',qty={},price={},dop='{}' where bno={}".format(b,c,d,e,f,a,))   
    con.commit()
    con.close()
    return render(request,"home.html",{'msg':'updated'})
def m1(request):
    return render(request,"m1.html")
def mod1(request):
    a=int(request.GET.get("bno"))
    b=request.GET.get("bname")
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("update book set bname='{ }' where bno={}".format(b,a,))   
    con.commit()
    con.close()
    return render(request,"home.html",{'msg':'updated'})
def m2(request):
    return render(request,"m2.html")
def mod2(request):
    a=int(request.GET.get("bno"))
    c=request.GET.get("author")
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("update book set author='{}' where bno={}".format(c,a,))   
    con.commit()
    con.close()
    return render(request,"home.html",{'msg':'updated'})
def m3(request):
    return render(request,"m3.html")
def mod3(request):
    a=int(request.GET.get("bno"))
    d=int(request.GET.get("qty"))
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("update book set  qty={}  where bno={}".format(d,a,))   
    con.commit()
    con.close()
    return render(request,"home.html",{'msg':'updated'})
def m4(request):
    return render(request,"m4.html")
def mod4 (request):
    a=int(request.GET.get("bno"))
    e=float(request.GET.get("price"))
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("update book set price={} where bno={}".format(e,a,))   
    con.commit()
    con.close()
    return render(request,"home.html",{'msg':'updated'})
def m5(request):
    return render(request,"m5.html")
def mod5(request):
    a=int(request.GET.get("bno"))
    f=request.GET.get("dop")
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("update book set  dop='{}'  where bno={}".format(f,a,))   
    con.commit()
    con.close()
    return render(request,"home.html",{'msg':'updated'})
def delrec(request):
    return render(request,"delrec.html")
def delete(request):
    a=int(request.GET.get("bno"))
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("delete from  book  where bno={}".format(a,))   
    con.commit()
    con.close()
    return render(request,"home.html",{'msg':'deleted'})
def searchrec(request):
    return render(request,"search.html")
def search1(request):
    return render(request,"s1.html")
def s1(request):
    a=int(request.GET.get("bno"))
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("select * from book  where bno={}".format(a,))
    x=cur.fetchall()
    con.commit()
    con.close()
    return  render (request,"results.html",{"list":x})
def search2(request):
    return render(request,"s2.html")
def s2(request):
    a=request.GET.get("bname")
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("select * from book  where bname='{}'".format(a,))
    x=cur.fetchall()
    con.commit()
    con.close()
    return  render (request,"results.html",{"list":x})
def search3(request):
    return render(request,"s3.html")
def s3(request):
    a=request.GET.get("aurhor")
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("select * from book  where author='{}'".format(a,))
    x=cur.fetchall()
    con.commit()
    con.close()
    return  render (request,"results.html",{"list":x})
def caddrec(request):
    return render(request,"caddrec.html")
def cadd (request):
    a=int(request.GET.get("cno"))
    b=request.GET.get("cname")
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("insert into clients values({},'{}')".format(a,b,))   
    con.commit()
    con.close()
    return render(request,"home.html",{'msg':'added'})
def cmodrec(request):
    return render(request,"cmodrec.html")
def cmod(request):
    a=int(request.GET.get("cno"))
    b=request.GET.get("cname")
    con=p.connect(host="localhost",user="root",passwd="india",database="manav")   
    cur=con.cursor()
    cur.execute("update clients set cname='{}'where cno={}".format(b,a))   
    con.commit()
    con.close()
    return render(request,"home.html",{'msg':'updated'})
def issue(request):
    return render(request,"issue.html")
def iss (request):
    try:
        a=int(request.GET.get("cno"))
        b=request.GET.get("cname")
        c=request.GET.get("bname")
        con=p.connect(host="localhost",user="root",passwd="india",database="manav")
        cur=con.cursor()
        d=date.today()
        cur.execute("select qty from book where bname='{}'".format(c))
        e=cur.fetchall()
        k=cur.rowcount
        if k==0:
            return render(request,"error.html",{'msg':'book not available'})
        f=e[0][0]-1
        if f==-1:
            return render(request,"home.html",{'msg':'book not available'})
        cur.execute("update book set qty={} where bname='{}'".format(f,c))
        cur.execute("insert into issue values({},'{}','{}','{}')".format(a,b,c,d))
        con.commit(),
        con.close()
        return render(request,"home.html",{'msg':'issued'})
    except:
        return render(request, "error.html", {'msg': 'book not available'})
def returnb(request):
    return render(request,"returnb.html")
def ret(request):
    try:
        a=int(request.GET.get("cno"))
        b=request.GET.get("cname")
        c=request.GET.get("bname")
        con=p.connect(host="localhost",user="root",passwd="india",database="manav")
        cur=con.cursor()
        d=date.today()
        cur.execute("select doi from issue where cname='{}'".format(b))
        x=cur.fetchall()
        k = cur.rowcount
        if k == 0:
            return render(request, "error.html", {'msg': 'book not available'})
        d2=x[0][0]+timedelta(days=7)
        cur.execute("select cname from issue where bname='{}'".format(c))
        e=cur.fetchall()
        k=cur.rowcount
        if k==0:
            return render(request,"error.html",{'msg':'book not available'})
        f=e[0][0]
        if f!=b:
            return render(request,"home.html",{'msg':'book not issued'})
        cur.execute("select qty from book where bname='{}'".format(c))
        g= cur.fetchall()
        g=g[0][0]+1
        cur.execute("update book set qty={} where bname='{}'".format(g,c))
        cur.execute("insert into return1 values({},'{}','{}','{}')".format(a,b,c,d))
        cur.execute("delete from issue where cname='{}' and bname='{}'".format(b,c))
        con.commit(),
        con.close()
        if d2<d:
            return render(request, "home.html", {'msg': 'returned,you are fined Rs.500'})
        return render(request,"home.html",{'msg':'returned'})
    except:
        return render(request, "error.html", {'msg': 'book not available'})
def defaulter(request):
    con = p.connect(host="localhost", user="root", passwd="india", database="manav")
    cur = con.cursor()
    d = date.today()
    cur.execute("select doi from issue")
    x = cur.fetchall()
    k = cur.rowcount
    if k == 0:
        return render(request, "error.html", {'msg': 'book not available'})
    l=[]
    for i in range(0,k):
        d2 = x[i][0] + timedelta(days=7)
        if d2<d:
            cur.execute("select * from issue where doi='{}'".format(x[i][0]))
            a=cur.fetchall()
            for j in a:
                if j not in l:
                    l.append(j)
    return render(request, "defaulter.html", {'list': l})




 
 

