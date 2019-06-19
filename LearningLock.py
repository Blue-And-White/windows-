# coding=utf-8
import tkinter
import threading
import time
import random
import datetime
from ctypes import *
from os.path import exists
from PIL import Image, ImageTk

def background():
        win=tkinter.Tk()
        width=win.winfo_screenwidth()
        height=win.winfo_screenheight()
        image = Image.open('C:/Users/Administrator/Desktop/1.jpg')
        photo = ImageTk.PhotoImage(image.resize((width,height)))
        label =tkinter.Label(win)
        a='both'
        label.pack(expand='YES',fill=a)
        label.configure(image = photo )
        win.geometry("+0+0")
        win.wm_attributes('-topmost',1)
        win.wm_attributes('-alpha',0.4)
        win.mainloop()
        return win

def lockscern(c):
        user32 = windll.LoadLibrary('user32.dll')
        user32.BlockInput(True)
        time.sleep(int(c)*60)
        user32.BlockInput(False)

    

def countertime(names,times):
    flag=True
    start=time.ctime()
    runtime=time.time()
    d1 = datetime.datetime.strptime('2019-12-21 00:00:00', '%Y-%m-%d %H:%M:%S')
    d2=datetime.datetime.now()
    disdate=d1-d2
    workhard=['行百里者半九十','真正的才智是刚毅的志向。',"故天将降大任于斯人也，必先苦其心志，劳其筋骨，饿其体肤，行拂乱其所为，增益其所不能。","古之成大事者，不惟有超世之才，亦必有坚忍不拔之志","书山有路勤为径，学海无涯苦作舟。","不登高山，不知天之高也；不临深谷，不知地之厚也；不闻先王之遗言，不知学问之大也。","浅薄的学识是一件危险的事情。","当你尽了自己的最大努力时，失败也是伟大的。","当一个人先从自己的内心开始奋斗，他就是个有价值的人。","嘲讽是一种力量，消极的力量。赞扬也是一种力量，但却是积极的力量。","环境不会改变，解决之道在于改变自己。","没有比脚更长的路，没有比人更高的山。","若不给自己设限，则人生中就没有限制你发挥的藩篱。","每一发奋努力的背后，必有加倍的赏赐。","与其临渊羡鱼，不如退而结网。","有事者，事竟成;破釜沉舟，百二秦关终归楚;苦心人，天不负;卧薪尝胆，三千越甲可吞吴。","人生重要的不是所站的位置，而是所朝的方向。","没有一种不通过蔑视、忍受和奋斗就可以征服的命运。","构成我们学习最大障碍的是已知的东西，而不是未知的东西。","信心来自于实力，实力来自于勤奋。","不要等待机会，而要创造机会。","永远不要以粗心为借口原谅自我。","成功的法则极为简单，但简单并不代表容易。","如果要挖井，就要挖到水出为止。","所有的胜利，与征服自我的胜利比起来，都是微不足道。","宝剑锋从磨砺出，梅花香自苦寒来","如果缺少破土面出并与风雪拚搏的勇气，种子的前途并不比落叶美妙一分。","瀑布跨过险峻陡壁时，才显得格外雄伟壮观。","学习本无底，前进莫徬徨。"]
    
    while 1:
        run1time=time.time()
        distime=run1time-runtime
        thistime=round((distime/60),2)
        time.sleep(3)
        page=random.randint(0,len(workhard)-1)
        print("********************************************************************************")
        print("\n")
        print("该任务名称为: ",names,"                            今天是",d2.year,"年",d2.month,"月",d2.day,"日")  
        print("\n")      
        print("该任务开始时间为:  ",start,"           距离考研还有:   ",disdate.days,"天")
        print("\n")
        print("当前时间为:        ",time.ctime())
        print("\n")
        print("当前任务进行的时间为:  ",thistime,"分钟")
        print("\n")
        print("距离任务结束时间还有:  ",round(times-thistime,2),"分钟")
        print("\n")
        print("你要知道的:",workhard[page],"\n")
        print("********************************************************************************")            
        if int(distime/60)==times:
            print("任务完成！\n")            
            inputflies(names,times,start)
            print("已经将任务结果写入文件log\n")
            print("已成功完成任务，请点击关闭右上角透明浮窗，退出程序！")            
            break       
            #next()
                        
                      
            


def inputflies(names,times,stime):

        if not exists('tasklog.txt') :
                with open("tasklog.txt",'a+') as f:
                        title='任务名称       任务时长(分钟)       任务开始时间'
                        text=str(names)+'               '+str(times)+'               '+str(stime)
                        f.write(title+'\n')
                        f.write(text+'\n')

        if exists('tasklog.txt') :
                with open("tasklog.txt",'a+') as f:                        
                        text=str(names)+'               '+str(times)+'               '+str(stime)                        
                        f.write(text+'\n')
       
        

def start():
    flag=True
    while flag :
        print("本程序一旦启动会将日志写入当前文件夹下，您可以在任务结束之后进行文件查看，任务结束后会退出程序")
        print("欢迎使用考研自律程序，现在请您输入任务信息!\n")
        print("作者:青花@Blue_And_White")               
        taskname=str(input("请输入任务名称:\n"))
        tasktime=int(input("请输入任务时间(分钟):\n"))
        print("警告，一旦程序启动程序电脑鼠标键盘将被锁死，并且无法退出，请您再三考虑！如果现在退出请输入exit!\n")

        ok=input("是否确认输入？\n确认    y   不确认 n   退出exit\n")

        if str(ok) == 'exit':
                exit()
        if str(ok) == 'y':
                break
    return taskname,tasktime


def popthread(t):
    for i in t:
        
        if i==0:
                i.start()
        if i!=1:
                i.setDaemon(False)
                i.start()        
             


def main():

        thr=[]
        taskname,tasktime=start()
        t1=threading.Thread(target=countertime,args=(taskname,tasktime,))
        thr.append(t1)
        t2=threading.Thread(target=lockscern,args=(tasktime,))
        thr.append(t2)
        t3=threading.Thread(target=background,args=())
        thr.append(t3)
        popthread(thr)  
         

r'''def next():
        
        print("当前一次任务结束是否选择进入下一次任务？\n")
        f=input("输入   next 下一次任务，输入  exit 退出！\n")

        print("请点击右上角关闭透明浮窗，程序向下进行.\n")
        if str(f)== 'exit':                
                exit()
        if str(f)== 'next':
                main()
        if str(f) not in ['next','exit']:
                print("输入错误,程序退出!\n")'''


if __name__ == "__main__":

        
        main()
         
                 
       
        
    