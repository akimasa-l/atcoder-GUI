import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import requests #インスコ必須
from bs4 import BeautifulSoup
import time
import glob
import subprocess
import os
import textwrap

#やるべきこと
'''
提出しないオプションをうまくやる
テストケースを選べるようにする
ACWAとかに色を付ける
ほかデザイン全般
other をしっかり
'''
class AtCoderGUI:
    def __init__(self):
        self.stringLen=30
    def openfile(self,path):
        with open(path,mode='r') as f:
            a='\n'.join([textwrap.fill(i,self.stringLen) for i in f.read().split('\n')])
        return a
    def ACWA(self,num,path,result,time,myoutput):
        detail = tk.Tk()
        detail.geometry('700x700')
        detail.title(u'テストケースチェック')
        
        
        #makeframe
        mainframe = tk.Frame(detail)
        mainframe.pack()
        codeframe = tk.LabelFrame(mainframe,text='Source Code',width = 160, height = 600, labelanchor = tk.N)
        codeframe.pack(padx = 5, pady = 5, side = tk.LEFT)
        codeframe.propagate(False)
        inputframe = tk.LabelFrame(mainframe,text='input',width = 160, height = 600, labelanchor = tk.N)
        inputframe.pack(padx = 5, pady = 5, side = tk.LEFT)
        inputframe.propagate(False)
        outputframe = tk.LabelFrame(mainframe,text='output',width = 160, height = 600, labelanchor = tk.N)
        outputframe.pack(padx = 5, pady = 5, side = tk.LEFT)
        outputframe.propagate(False)
        myoutputframe = tk.LabelFrame(mainframe,text='myoutput',width = 160, height = 600, labelanchor = tk.N)
        myoutputframe.pack(padx = 5, pady = 5, side = tk.LEFT)
        myoutputframe.propagate(False)
        #makestringvar
        codevar = tk.StringVar()
        inputvar = tk.StringVar()
        outputvar = tk.StringVar()
        myoutputvar = tk.StringVar()
        
        #今回は特別
        myoutputvar.set(myoutput)
        
        #getsourcecode,input,output and set
        '''
        with open(path+'main.py',mode='r') as f:
            codevar.set('\n'.join([textwrap.fill(i,30) for i in f.read().split('\n')]))#改行一つずつに対して文字数制限
        with open(path+'input{}.txt'.format(num),mode='r') as f:
            inputvar.set('\n'.join([textwrap.fill(i,30) for i in f.read().split('\n')]))#改行一つずつに対して文字数制限
        with open(path+'output{}.txt'.format(num),mode='r') as f:
            outputvar.set('\n'.join([textwrap.fill(i,30) for i in f.read().split('\n')]))#改行一つずつに対して文字数制限
        '''
        codevar.set(AtCoderGUI().openfile(path=path+'main.py'))
        inputvar.set(AtCoderGUI().openfile(path=path+'input{}.txt'.format(num)))
        outputvar.set(AtCoderGUI().openfile(path=path+'output{}.txt'.format(num)))
        #makelabel
        codelabel = tk.Label(codeframe,textvariable=codevar,bg='white',justify=tk.LEFT)
        codelabel.pack()
        inputlabel = tk.Label(inputframe,textvariable=inputvar,bg='white',justify=tk.LEFT)
        inputlabel.pack()
        outputlabel = tk.Label(outputframe,textvariable=outputvar,bg='white',justify=tk.LEFT)
        outputlabel.pack()
        myoutputlabel = tk.Label(myoutputframe,textvariable=myoutputvar,bg='white',justify=tk.LEFT)
        myoutputlabel.pack()
        
        #詳細情報
        belowframe = tk.Frame(detail)
        belowframe.pack()
        #button
        buttontext = 'Next'
        button = tk.Button(belowframe,text=buttontext,command=lambda : detail.destroy(),width = 5, height = 3)
        button.pack(side=tk.RIGHT)
        #property
        propertytext = 'Task : {} Status : {} Exec time : {}ms Code Size : {}'.format('ABC012 input{}.txt'.format(num),result,time,os.path.getsize(path+'main.py'))
        propertyframe = tk.LabelFrame(belowframe,text='Property',width = 500, height = 70, labelanchor = tk.NW)
        propertyframe.pack(padx = 5, pady = 5, side = tk.LEFT)
        propertyframe.propagate(False)
        propertylabel = tk.Label(propertyframe,text=propertytext,justify=tk.CENTER)
        propertylabel.pack()
        
        detail.mainloop()
    
    def TLERE(self,num,path,result,time,myoutput):
        detail = tk.Tk()
        detail.geometry('700x700')
        detail.title(u'テストケースチェック')
        
        
        #makeframe
        mainframe = tk.Frame(detail)
        mainframe.pack()
        codeframe = tk.LabelFrame(mainframe,text='Source Code',width = 220, height = 600, labelanchor = tk.N)
        codeframe.pack(padx = 5, pady = 5, side = tk.LEFT)
        codeframe.propagate(False)
        inputframe = tk.LabelFrame(mainframe,text='input',width = 220, height = 600, labelanchor = tk.N)
        inputframe.pack(padx = 5, pady = 5, side = tk.LEFT)
        inputframe.propagate(False)
        myoutputframe = tk.LabelFrame(mainframe,text='myoutput',width = 220, height = 600, labelanchor = tk.N)
        myoutputframe.pack(padx = 5, pady = 5, side = tk.LEFT)
        myoutputframe.propagate(False)
        #makestringvar
        codevar = tk.StringVar()
        inputvar = tk.StringVar()
        myoutputvar = tk.StringVar()
        
        #今回は特別
        myoutputvar.set(myoutput)
        
        #getsourcecode,input,output and set
        with open(path+'main.py',mode='r') as f:
            codevar.set('\n'.join([textwrap.fill(i,30) for i in f.read().split('\n')]))#改行一つずつに対して文字数制限
        with open(path+'input{}.txt'.format(num),mode='r') as f:
            inputvar.set('\n'.join([textwrap.fill(i,30) for i in f.read().split('\n')]))#改行一つずつに対して文字数制限
        
        #makelabel
        codelabel = tk.Label(codeframe,textvariable=codevar,bg='white',justify=tk.LEFT)
        codelabel.pack()
        inputlabel = tk.Label(inputframe,textvariable=inputvar,bg='white',justify=tk.LEFT)
        inputlabel.pack()
        myoutputlabel = tk.Label(myoutputframe,textvariable=myoutputvar,bg='white',justify=tk.LEFT)
        myoutputlabel.pack()
        
        #詳細情報
        belowframe = tk.Frame(detail)
        belowframe.pack()
        #button
        buttontext = 'Next'
        button = tk.Button(belowframe,text=buttontext,command=lambda : detail.destroy(),width = 5, height = 3)
        button.pack(side=tk.RIGHT)
        #property
        propertytext = 'Task : {} Status : {} Exec time : {}ms Code Size : {}'.format('ABC012 input{}.txt'.format(num),result,time,os.path.getsize(path+'main.py'))
        propertyframe = tk.LabelFrame(belowframe,text='Property',width = 500, height = 70, labelanchor = tk.NW)
        propertyframe.pack(padx = 5, pady = 5, side = tk.LEFT)
        propertyframe.propagate(False)
        propertylabel = tk.Label(propertyframe,text=propertytext,justify=tk.CENTER)
        propertylabel.pack()
        
        detail.mainloop()


'''
contget = list()
#メインウィンドウ
root=tk.Tk()
root.geometry('200x200')
root.title(u'ファイルを選ぶ')

#提出しないオプション
submitbool = tk.BooleanVar()
submitbool.set(True)
submitcheckbutton = tk.Checkbutton(root,variable=submitbool,text=u'提出する')
submitcheckbutton.place(x=100,y=30)


#setcontcombo
contcombo = ttk.Combobox(root,state='readonly',width=10,justify=tk.CENTER)#編集不可

def getcontinfo(event):#contgetに(contcomboからもらった情報をもとに探したフォルダー)を渡す
    global contget
    if contcombo.get()=='':#選ばれていないときは虚無を返す
        contget=[]
    else:
        contget=[os.path.basename(i.rstrip(os.sep)) for i in glob.glob(r'./{}/*/'.format(contcombo.get()))]

def changelevel():#levelcombo['values']にcontgetを渡す
    global contget
    levelcombo['values']=contget

'''
def ACWA(num,path,result,time,myoutput):
    detail = tk.Tk()
    detail.geometry('700x700')
    detail.title(u'テストケースチェック')
    
    
    #makeframe
    mainframe = tk.Frame(detail)
    mainframe.pack()
    codeframe = tk.LabelFrame(mainframe,text='Source Code',width = 160, height = 600, labelanchor = tk.N)
    codeframe.pack(padx = 5, pady = 5, side = tk.LEFT)
    codeframe.propagate(False)
    inputframe = tk.LabelFrame(mainframe,text='input',width = 160, height = 600, labelanchor = tk.N)
    inputframe.pack(padx = 5, pady = 5, side = tk.LEFT)
    inputframe.propagate(False)
    outputframe = tk.LabelFrame(mainframe,text='output',width = 160, height = 600, labelanchor = tk.N)
    outputframe.pack(padx = 5, pady = 5, side = tk.LEFT)
    outputframe.propagate(False)
    myoutputframe = tk.LabelFrame(mainframe,text='myoutput',width = 160, height = 600, labelanchor = tk.N)
    myoutputframe.pack(padx = 5, pady = 5, side = tk.LEFT)
    myoutputframe.propagate(False)
    #makestringvar
    codevar = tk.StringVar()
    inputvar = tk.StringVar()
    outputvar = tk.StringVar()
    myoutputvar = tk.StringVar()
    
    #今回は特別
    myoutputvar.set(myoutput)
    
    #getsourcecode,input,output and set
    with open(path+'main.py',mode='r') as f:
        codevar.set('\n'.join([textwrap.fill(i,30) for i in f.read().split('\n')]))#改行一つずつに対して文字数制限
    with open(path+'input{}.txt'.format(num),mode='r') as f:
        inputvar.set('\n'.join([textwrap.fill(i,30) for i in f.read().split('\n')]))#改行一つずつに対して文字数制限
    with open(path+'output{}.txt'.format(num),mode='r') as f:
        outputvar.set('\n'.join([textwrap.fill(i,30) for i in f.read().split('\n')]))#改行一つずつに対して文字数制限
    
    #makelabel
    codelabel = tk.Label(codeframe,textvariable=codevar,bg='white',justify=tk.LEFT)
    codelabel.pack()
    inputlabel = tk.Label(inputframe,textvariable=inputvar,bg='white',justify=tk.LEFT)
    inputlabel.pack()
    outputlabel = tk.Label(outputframe,textvariable=outputvar,bg='white',justify=tk.LEFT)
    outputlabel.pack()
    myoutputlabel = tk.Label(myoutputframe,textvariable=myoutputvar,bg='white',justify=tk.LEFT)
    myoutputlabel.pack()
    
    #詳細情報
    belowframe = tk.Frame(detail)
    belowframe.pack()
    #button
    buttontext = 'Next'
    button = tk.Button(belowframe,text=buttontext,command=lambda : detail.destroy(),width = 5, height = 3)
    button.pack(side=tk.RIGHT)
    #property
    propertytext = 'Task : {} Status : {} Exec time : {}ms Code Size : {}'.format('ABC012 input{}.txt'.format(num),result,time,os.path.getsize(path+'main.py'))
    propertyframe = tk.LabelFrame(belowframe,text='Property',width = 500, height = 70, labelanchor = tk.NW)
    propertyframe.pack(padx = 5, pady = 5, side = tk.LEFT)
    propertyframe.propagate(False)
    propertylabel = tk.Label(propertyframe,text=propertytext,justify=tk.CENTER)
    propertylabel.pack()
    
    detail.mainloop()

def TLERE(num,path,result,time,myoutput):
    detail = tk.Tk()
    detail.geometry('700x700')
    detail.title(u'テストケースチェック')
    
    
    #makeframe
    mainframe = tk.Frame(detail)
    mainframe.pack()
    codeframe = tk.LabelFrame(mainframe,text='Source Code',width = 220, height = 600, labelanchor = tk.N)
    codeframe.pack(padx = 5, pady = 5, side = tk.LEFT)
    codeframe.propagate(False)
    inputframe = tk.LabelFrame(mainframe,text='input',width = 220, height = 600, labelanchor = tk.N)
    inputframe.pack(padx = 5, pady = 5, side = tk.LEFT)
    inputframe.propagate(False)
    myoutputframe = tk.LabelFrame(mainframe,text='myoutput',width = 220, height = 600, labelanchor = tk.N)
    myoutputframe.pack(padx = 5, pady = 5, side = tk.LEFT)
    myoutputframe.propagate(False)
    #makestringvar
    codevar = tk.StringVar()
    inputvar = tk.StringVar()
    myoutputvar = tk.StringVar()
    
    #今回は特別
    myoutputvar.set(myoutput)
    
    #getsourcecode,input,output and set
    with open(path+'main.py',mode='r') as f:
        codevar.set('\n'.join([textwrap.fill(i,30) for i in f.read().split('\n')]))#改行一つずつに対して文字数制限
    with open(path+'input{}.txt'.format(num),mode='r') as f:
        inputvar.set('\n'.join([textwrap.fill(i,30) for i in f.read().split('\n')]))#改行一つずつに対して文字数制限
    
    #makelabel
    codelabel = tk.Label(codeframe,textvariable=codevar,bg='white',justify=tk.LEFT)
    codelabel.pack()
    inputlabel = tk.Label(inputframe,textvariable=inputvar,bg='white',justify=tk.LEFT)
    inputlabel.pack()
    myoutputlabel = tk.Label(myoutputframe,textvariable=myoutputvar,bg='white',justify=tk.LEFT)
    myoutputlabel.pack()
    
    #詳細情報
    belowframe = tk.Frame(detail)
    belowframe.pack()
    #button
    buttontext = 'Next'
    button = tk.Button(belowframe,text=buttontext,command=lambda : detail.destroy(),width = 5, height = 3)
    button.pack(side=tk.RIGHT)
    #property
    propertytext = 'Task : {} Status : {} Exec time : {}ms Code Size : {}'.format('ABC012 input{}.txt'.format(num),result,time,os.path.getsize(path+'main.py'))
    propertyframe = tk.LabelFrame(belowframe,text='Property',width = 500, height = 70, labelanchor = tk.NW)
    propertyframe.pack(padx = 5, pady = 5, side = tk.LEFT)
    propertyframe.propagate(False)
    propertylabel = tk.Label(propertyframe,text=propertytext,justify=tk.CENTER)
    propertylabel.pack()
    
    detail.mainloop()
'''

def selectcase(path):#ケースを選べるようにしたい...
    pass

def submission(path):#AXC用
    continfo = [path[6:12],path[12]]
    with open(path+'main.py',mode='r') as f:
        mycode = f.read()+'\n'
    
    with open('config.txt',mode='r') as f:#read config.txt
        userstatus = f.read().split()
    
    #セッション
    session=requests.session()

    #start to login
    loginurl='https://atcoder.jp:443/login'

    # csrf_token取得
    r = session.get(loginurl)
    s = BeautifulSoup(r.text, 'html.parser')
    csrf_token = s.find(attrs={'name': 'csrf_token'}).get('value')

    # パラメータセット
    login_info = {"csrf_token": csrf_token,"username":userstatus[0],"password":userstatus[1]}
    #login
    result = session.post(loginurl, data=login_info)
    result.raise_for_status()

    # lets submit
    submiturl = "https://atcoder.jp/contests/{}/submit".format(continfo[0])
    submit_info = {"data.TaskScreenName": '_'.join(continfo),"csrf_token": csrf_token,"data.LanguageId": 4006,"sourceCode": mycode}
    # post
    result = session.post(submiturl, data=submit_info)
    result.raise_for_status()
    if result.status_code == 200:
        print("Submitted!")
        print(path,submit_info)
    else:
        print("Error in submitting...")


    

def runcases(path):
    resultlist=list()
    for i in range(len(glob.glob(path+'input*.txt'))):
        try:#走らせる
            mycode = 'cat input{}.txt | python main.py'.format(i)
            starttime=time.time()
            a=subprocess.run(mycode,timeout=5,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,cwd=path)
        except subprocess.TimeoutExpired:#TLEなら
            TLERE(i,path,'TLE',int((time.time()-starttime)*1000),a.stdout.decode().replace('\r\n','\n'))
            resultlist.append('TLE')
        else:
            endtime=int((time.time()-starttime)*1000)
            if a.returncode!=0:#エラーが発生してるなら
                TLERE(i,path,'RE',endtime,a.stdout.decode().replace('\r\n','\n'))
                resultlist.append('RE')
            else:
                with open(path+'output{}.txt'.format(i),mode='r') as f:
                    ans = f.read()
                if ans == a.stdout.decode().replace('\r\n','\n'):
                    ACWA(i,path,'AC',endtime,a.stdout.decode().replace('\r\n','\n'))
                    resultlist.append('AC')
                else:
                    ACWA(i,path,'WA',endtime,a.stdout.decode().replace('\r\n','\n'))
                    resultlist.append('WA')
    if set(resultlist)==set(['AC']):
        root = tk.Tk()
        root.withdraw()
        ACmessagebox = messagebox.askyesno(u'おめでとう',u'すべてACしています\n提出しますか？')
        if ACmessagebox:
            root.destroy()
            submission(path)
        else:
            root.destroy()
    else:
        root = tk.Tk()
        root.withdraw()
        mymessage = u'{}問中{}問あっています。\nもう少し頑張ってみましょう'.format(len(resultlist),resultlist.count('AC'))
        ACmessagebox = messagebox.showinfo(u'ざんねん',mymessage)
        root.destroy()


def getlevelinfo():
    global errorvar
    continfo=contcombo.get()
    levelinfo=levelcombo.get()
    if continfo=='' or levelinfo=='':
        errorvar.set(u'入力してください')
    elif os.path.exists(r'./{}/{}/'.format(continfo,levelinfo))==False:
        errorvar.set(u'もう一度見て')
    else:
        path=r'./{}/{}/'.format(continfo,levelinfo)
        root.destroy()
        runcases(path)
    
        

#setcontcombo続き
contcombo.bind("<<ComboboxSelected>>", getcontinfo)
contcombo['values'] = [os.path.basename(i.rstrip(os.sep)) for i in glob.glob(r'./???/')]
if os.path.exists(r'./Other/'):
    contcombo['values'] += tuple(['Other'])
#setlevelcombo
levelcombo = ttk.Combobox(root,state='readonly',width=10,justify=tk.CENTER,postcommand=changelevel)#編集不可

#pack
contcombo.pack(side=tk.LEFT,padx=5,pady=5)
levelcombo.pack(side=tk.LEFT,padx=5,pady=5)
#エラーメッセージ用
errorvar=tk.StringVar()
errorvar.set('')
errorlabel=tk.Label(root, textvariable=errorvar)
errorlabel.place(anchor='center',x=50,y=150)

#送信ボタン
getbutton=tk.Button(root,text=u'送信',command=getlevelinfo,width=10)
getbutton.place(anchor='center',x=150,y=150)

root.mainloop()
'''