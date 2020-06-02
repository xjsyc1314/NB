#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from  tkinter import *
#import tkMessageBox
import requests
 
# 定义button事件
def translation():
    content=entry.get()
    if  content == '':
        tkinter.messagebox.showinfo("提示", "请输入需要翻译的内容")
    else:
        print (content)
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 构造请求头
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.121Safari / 537.36',
        'Host': 'fanyi.youdao.com'
    }
    # 构造请求参数
    parameter = {
        'i': content,
        'from': 'zh-CHS',
        'to': 'zh-CHS',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15519651381700',
        'sign': '6e08c6764da13606b9fce21863bfc064',
        'ts': '1551965138170',
        'bv': '33a62fdcf6913d2da91495dad54778d1',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'
    }
    result = requests.get(url, params=parameter, headers=headers)
    if result.status_code == 200:
        data = result.json()
        translation = data['translateResult'][0][0]['tgt']
        print(translation)
        res.set(translation)
    else:
        print("网页请求失败")
 
root = Tk()
#1、窗口标题
 
res = StringVar()
 
root.title('翻译成中文or中译英')
#2、窗口大小，显示位置
root.geometry('290x100+573+286')
#3、标签控件
lable = Label(root,text='输入要翻译的内容',font=('微软雅黑',10), fg='black')
lable.grid()
 
lable = Label(root,text='翻译结果',font=('微软雅黑',10), fg='black')
lable.grid()
 
#4、输入控件
entry=Entry(root, font='微软雅黑')
entry.grid(row=0,column=1)
#显示翻译之后的内容
entry2=Entry(root, font='微软雅黑', textvariable=res)
#输入标签位置
entry2.grid(row=1,column=1)
 
#5、按钮控件
button = Button(root, text ="翻译",width=10,font=('微软雅黑',10),command=translation)
button.grid(row=2,column=0,sticky=W)
 
button = Button(root, text ="退出",width=10,font=('微软雅黑',10), command=root.quit)
button.grid(row=2,column=1,sticky=E)
 
#-----------------至此，界面已经画出来了---------------------------
 
root.mainloop()
