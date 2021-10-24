import tkinter.ttk as ttk
import tkinter.font
from tkinter import*

root=Tk()
root.title("Nado GUI")
root.geometry("800x700+300+50")
color='white'

root['bg']=color
# font
font=tkinter.font.Font(family="맑은 고딕", size=11)

# 콤보박스
values=["DFS","BFS","다익스트라","플로이드 워셜","크루스칼","위상정렬","이진탐색","서로소 알고리즘","서로소(무방향 탐색)"]

clicked=StringVar()
clicked.set(values[0])
drop=OptionMenu(root,clicked,values)
drop.pack()
#조건 
txt_sample=Text(root,width=95,height=4,pady=10,font=font,bg='#333333',fg='white',insertbackground='white')
txt_sample.insert(END,"조건") #

txt_sample.pack()

txt=Text(root,width=95,height=22,pady=10,font=font,bg='#333333',fg='white',insertbackground='white')
txt.insert(END,"알고리즘을 입력하세요") # END : 글자를 어디 넣을건지

txt.pack()

# 클릭시 텍스트 위젯 삭제
def click(event):
   txt.configure(state=NORMAL)
   txt.delete("1.0", END)
   txt.unbind('<Button-1>', clicked)

clicked = txt.bind('<Button-1>', click)


def btncmd(): # txt.insert에 쓰인 값을 가져오게 만드는 함수
    f=open('C:/Users/박준형/Desktop/새 폴더/2021.10.21.txt','w',encoding='utf-8')
    f.write(txt.get("1.0",END))
    txt.delete("1.0",END)


#실행 프레임
frame_run=Frame(root,background=color)
frame_run.pack(fill="x",padx=5,pady=15)

btn_close=Button(frame_run,padx=30,pady=5,text="닫기",width=12,command=root.quit,background=color)
btn_close.pack(side="right",padx=100,pady=10)

btn_start=Button(frame_run,padx=30,pady=5,text="입력",width=12,command=btncmd,background=color)
btn_start.pack(side="left",padx=100,pady=10)

root.resizable(False,False) # 창 크기 못바꾸게 설정
root.mainloop()