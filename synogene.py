# -*- coding: utf-8 -*-

import tkinter

import random


list_when=["とある時代","時は未来","時は現代"]

list_who=["ベレー帽の少女が","社長が","かわいい猫耳少女が","マスターである男性が","トラブルを起こしたニート主人公が","機械の大群に殺された主人公が","引っ込み思案の少女が","幽霊としてよみがえった天才小説家が"]

list_where=["冒険者の格差が問題となった異世界で","ゲーム内仮想世界で","リアル世界で","地球で","過去世界で","都会のある町で"]

list_action=["ギルドの問題を解決する","商人となってお店を開く","異世界の牢獄に閉じ込められる","何らかのトラブルによって過去に飛ばされる","ラスボスを倒す","霊体となる","機械を乗っ取る","人類を勝利に導く","作家デビューを目指して頑張る"]

n_pre_when=-1

n_pre_who=-1

n_pre_where=-1

n_pre_action=-1


#ウインドウ設定

tk=tkinter.Tk()

tk.title(u"なろう系あらすじジェネレータ")

tk.minsize(640,480)

#ウインドウ表示

win=tkinter.Canvas(bg="black",width=640,height=480)

win.place(x=0,y=0)

btn_quit = tkinter.Button(tk, text='終了')

btn_quit.place(x=130, y=80)

btn_create = tkinter.Button(tk, text='自動作成')

btn_create.place(x=50, y=80)

txt_synopsis=tkinter.Label(text=u"ここにランダムで作成したあらすじが表示されます。")

txt_synopsis.place(x=0,y=0)


def display_synopsis():

    global n_pre_when,n_pre_who,n_pre_where,n_pre_action


    if n_pre_when==-1:

        n_when=random.randint(0,len(list_when)-1)

    else:

        n_when=random.randint(0,len(list_when)-2)

        if n_when>=n_pre_when:

            n_when=n_when+1


    if n_pre_who==-1:

        n_who=random.randint(0,len(list_who)-1)

    else:

        n_who=random.randint(0,len(list_who)-2)

        if n_who>=n_pre_who:

            n_who=n_who+1


    if n_pre_where==-1:

        n_where=random.randint(0,len(list_where)-1)

    else:

        n_where=random.randint(0,len(list_where)-2)

        if n_where>=n_pre_where:

            n_where=n_where+1


    if n_pre_action==-1:

        n_action=random.randint(0,len(list_action)-1)

    else:

        n_action=random.randint(0,len(list_action)-2)

        if n_action>=n_pre_action:

            n_action=n_action+1


    t=list_when[n_when] + "、" + list_who[n_who] + "、" + list_where[n_where] + "、" + list_action[n_action]

    print(t,n_when,n_who,n_where,n_action)

    txt_synopsis["text"] = t

    n_pre_when=n_when

    n_pre_who=n_who

    n_pre_where=n_where

    n_pre_action=n_action

    

btn_create["command"]=display_synopsis


def destroy_tk():

    tk.destroy()

btn_quit["command"]=destroy_tk



tk.mainloop()