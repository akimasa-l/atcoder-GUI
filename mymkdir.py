import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import os
import shutil
import subprocess
import requests #インスコ必須
from bs4 import BeautifulSoup #インスコ必須 #lxmlももしかしたら必要かも

'''
やっておくべきこと
もしかしたらコンテスト中はうごかないかも

'''

def checkExistContest(continfo):
    if continfo[0]=='Other':
        contestname=continfo[1]
    else:
        contestname=''.join(continfo[:2])
    contesturl='https://atcoder.jp/contests/'+contestname
    while True:
        mystatuscode=requests.get(contesturl).status_code
        if mystatuscode==200:
            x=True
            break
        else:
            res = messagebox.askretrycancel("ごめんね", "{}は存在しなさそう".format(contestname))
            if res:
                continue
            else:
                x=False
                break
    return x
    


#SetFrame
start=tk.Tk()
start.geometry('250x250')
start.title(u'コンテストを選択')
#setLabel
label1=tk.Label(start,text='Contest'+' '*15+'Number'+' '*15+'Level')
label1.place(anchor='center',x=125,y=100)
#SetBox
contestcombo = ttk.Combobox(start,state='readonly',width=10,justify=tk.CENTER)#編集不可
contestnum = tk.Entry(width=10,justify=tk.CENTER)
levelcombo = ttk.Combobox(start,width=10,justify=tk.CENTER)#編集可
#SetValues
contestcombo["values"] = ("ABC","ARC","AGC",'Other')
levelcombo['values'] = [chr(i) for i in range(65,71)]#ABCDEF
#Grid
contestcombo.pack(side=tk.LEFT,padx=5,pady=5)
contestnum.pack(side=tk.LEFT,padx=5,pady=5)
levelcombo.pack(side=tk.LEFT,padx=5,pady=5)

continfo=['','','']#example:['ABC','001','A']

#注意書き
errorvar=tk.StringVar()
errorvar.set('')
errorlabel=tk.Label(start, textvariable=errorvar)
errorlabel.place(anchor='center',x=80,y=175)

def mymkdir(continfo,contget):
    with open('config.txt',mode='r') as f:#read config.txt
        userstatus = f.read().split()
    #セッション
    session=requests.session()

    #start to login
    loginurl='https://beta.atcoder.jp/login'

    # csrf_token取得
    r = session.get(loginurl)
    r = session.get(r.url)
    s = BeautifulSoup(r.text, 'html.parser')
    csrf_token = s.find(attrs={'name': 'csrf_token'}).get('value')

    # パラメータセット
    login_info = {"csrf_token": csrf_token,"username":userstatus[0],"password":userstatus[1]}#隠しとけ
    #login
    result = session.post(loginurl, data=login_info)
    result.raise_for_status()

    #ファイルコピー
    programpath = r'./{}/{}/main.py'.format(contget,''.join(continfo))
    shutil.copyfile(r"./sample.py", programpath)
    
    #scrape
    shitajunbi = (continfo[0]+continfo[1]).lower()
    contesturl='https://beta.atcoder.jp/contests/{}/tasks/{}_{}'.format(shitajunbi,shitajunbi,continfo[2].lower())
    res = session.get(contesturl)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    elems = soup.select('pre')
    testcase=[i.getText() for i in elems[1:len(elems)//2]]

    #テストケースを書き込む
    #input
    inputcase=testcase[::2]
    for i in range(len(inputcase)):
        path = r'./{}/{}/{}.txt'.format(contget,''.join(continfo),'input'+str(i))
        with open(path, mode='w') as f:
            f.write(inputcase[i].replace('\r\n','\n'))
    #output
    outputcase=testcase[1::2]
    for i in range(len(outputcase)):
        path = r'./{}/{}/{}.txt'.format(contget,''.join(continfo),'output'+str(i))
        with open(path, mode='w') as f:
            f.write(outputcase[i].replace('\r\n','\n'))
    
    #vscodeでファイルを開く
    vscodepath=userstatus[2]
    subprocess.Popen([vscodepath,programpath])

def getcontinfo():
    global continfo
    global errorvar
    contget=contestcombo.get()
    numget=contestnum.get()
    levelget=levelcombo.get()
    if contget=='' or numget=='' or levelget=='':#入力漏れ
        errorvar.set(u'入力してください')
    else:
        continfo[0]=contget
        continfo[1]=numget.zfill(3)#0埋め
        continfo[2]=levelget
        if checkExistContest(continfo):
            if continfo[0]=='Other':
                #print(u'カス')
                continfo[0]=''
            cancelbox=messagebox.askokcancel(u'確認',u'作成するのは以下のフォルダーです\n{}'.format(' '.join(continfo)))
            if cancelbox:
                start.destroy()
                os.makedirs(r'./{}'.format(contget),exist_ok=True)
                os.makedirs(r'./{}/{}'.format(contget,''.join(continfo)),exist_ok=True)
                mymkdir(continfo,contget)


#送信ボタン
getbutton=tk.Button(start,text=u'送信',command=getcontinfo,width=10)
getbutton.place(anchor='center',x=200,y=175)

start.mainloop()
