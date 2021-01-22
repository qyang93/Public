####################################################################################################
#####                   Automatically output wbs top50 realtime hot                            #####
#####                       and check if Vin is in  wbs-hotrank                                #####
#####                    If yes, send email to qunyang93@gmail.com (not yet set)          #####
#####                                date: 8 of December 2020                                  #####
#####                      Written by Qun Yang (Qun.Yang@cpfs.mpg.de) in MPI-CPFS              #####
####################################################################################################
    
import urllib.request
from bs4 import BeautifulSoup
import re
import yagmail
import traceback 
def main():
    url = "https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6"
    email = "qunyang93@gmail.com"
    keyword = "周震南"
    ReturnValue = askURL(url,keyword)
    return 0

def askURL(url,keyword):
    try:
        response = urllib.request.urlopen(url,timeout = 10)
    except urllib.error.URLError as e:
        print("time out!")
    
    html = response.read().decode("utf-8")
    bs = BeautifulSoup(html,"html.parser")
    #content = bs.findAll(text=re.compile("周震南"))
    menu = bs.findAll("a", target="_blank")
    print("%%% wbs top50 realtime hot %%%")
    vinkeyword = []
    for cnt, item in enumerate(menu[0:51]):
        print("  No.%s    %s" % (cnt, item.text))
        if keyword in item.text:
            vinkeyword.append(item.text)
    print("%%% wbs top50 realtime hot %%%")
    print("\n")
    print("%%% if you want to see more details, please go to: https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6")
    print("\n")
    if len(vinkeyword) == 0:
        print("  ###########################")
        print("  ##### %s没有上热搜！#####" % keyword)
        print("  ###########################")
        print("\n")
    else:
        print("  #############################")
        print("  ##### %s上热搜啦！！！####" % keyword)
        print("  #############################")
        print("\n")
        for i in range(len(vinkeyword)):
            print("  !!! 热搜词条是:%s" % (vinkeyword[i]))
        print("\n")

def sendEmail(content):
    try:
        yag = yagmail.SMTP(user='qunyang93@gmail.com', password='not set yet')
        yag.send(to='qunyang93@gmail.com', subject="周震南上热搜啦！！！", contents='Hurray, it worked!')
        print("Email sent successfully")
    except:
        print("Error, email was not sent")
        #print(traceback.format_exc())

if __name__ == "__main__":
    main()
