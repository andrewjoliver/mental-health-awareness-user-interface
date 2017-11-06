import tkinter
from tkinter import *
import simpleaudio as sa
import webbrowser

#user interface
tk = Tk()
tk.geometry('700x700')
canvas = Canvas(tk, width=0, height=0, bg = 'white')
canvas.pack()
canvas.pack(expand = YES, fill = BOTH)
canvas.create_text(635, 20, text="Mental Health Awareness Activism Project", anchor=CENTER, fill="dark blue", font=("arial",40))
#Logo
global logo
logo = PhotoImage(file='logo.gif')
canvas.create_image(1280, 0, image=logo, anchor=NE)

#Bodies
global male
male = PhotoImage(file = 'body.gif')

#Audio Playing for Each Body Part 
def audio_head(event):
    wave_obj = sa.WaveObject.from_wave_file("/Activism Project/head.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
def audio_heart(event):
    wave_obj = sa.WaveObject.from_wave_file("/Activism Project/heart.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
def audio_joint(event):
    wave_obj = sa.WaveObject.from_wave_file("/Activism Project/joint.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
def audio_stom(event):
    wave_obj = sa.WaveObject.from_wave_file("/Activism Project/stom.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
def audio_rep(event):
    wave_obj = sa.WaveObject.from_wave_file("/Activism Project/rep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

#Audio Playing for Each Pysical Joint
    

def sources1(event):
    global sources2
    canvas.create_rectangle(0, 68,1280,685, fill="white")
    sources2 = PhotoImage(file='sources.gif')
    canvas.create_image(1100,90, image=sources2, anchor=NE)
    canvas.update()
    def deletesources(event):
        canvas.delete(all)
        drawcanvas(1)
    canvas.tag_bind(sources, '<Button-1>', deletesources)

def drawcanvas(x):
    canvas.delete(all)
    canvas.create_rectangle(0, 0, 1279, 718, fill="white")
    canvas.create_text(635, 20, text="Mental Awareness Activism Project", anchor=CENTER, fill="dark blue", font=("arial",40))
    canvas.create_image(1280, 0, image=logo, anchor=NE)
    canvas.create_image(990, 110, image = male, anchor=NW)
    canvas.create_oval(850, 400, 890, 450, outline="white", fill="white")
    canvas.create_text(5, 80, text="Weekly Cost Span (each bill represents $50 USD):", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(448, 73, text="1", fill="black", font=("Times New Roman", 16), anchor=W)
    canvas.create_text(5, 200, text="Weekly Time Commitment Span (each clock represents 4 hours):", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(564, 190, text="2", fill="black", font=("Times New Roman", 16), anchor=W)
    canvas.create_text(5, 323, text="Common Treatment Options:", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(241, 310, text="3", fill="black", font=("Times New Roman", 16), anchor=W)
    canvas.create_text(5, 450, text="Diagnosis Names:", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(1180, 140, text="5", fill="black", font=("Times New Roman", 16), anchor=W)
    global sources
    sources = canvas.create_rectangle(0,0, 70, 50, fill="light grey")
    canvas.tag_bind(sources, '<Button-1>', sources1)
    canvas.create_text(4, 25, text="Sources", fill="black", font=("Times New Roman", 20), anchor=W)

#functions for male body
def showmhead():
    global mhead
    mhead1 = canvas.create_oval(1134, 130, 1159, 145, fill="blue", outline="black")
    mhead = canvas.create_oval(1104, 100, 1189, 175, fill="", outline="")
    canvas.tag_bind(mhead, '<Button-1>', expmhead)
def showmheart():
    global mheart
    mheart1 = canvas.create_oval(1132, 269, 1161, 288, fill="red", outline="black")
    mheart = canvas.create_oval(1102, 239, 1191, 318, fill="", outline="")
    canvas.tag_bind(mheart, '<Button-1>', expmheart)
def showmjoint():
    global mlelbow
    mlelbow1 = canvas.create_oval(1066, 341, 1086, 323, fill="red", outline="black")
    mlelbow = canvas.create_oval(946, 311, 1116, 353, fill="", outline="")
    mrelbow = canvas.create_oval(1200, 341, 1220, 323, fill="red", outline="black")
    mlknee = canvas.create_oval(1106, 535, 1131, 555, fill="red", outline="black")
    mrknee = canvas.create_oval(1147, 535, 1172, 555, fill="red", outline="black")
    canvas.tag_bind(mlelbow, '<Button-1>', expmjoint)
def showmstom():
    global mstom
    mstom1 = canvas.create_oval(1107, 345, 1178, 388, fill="blue", outline="black")
    mstom = canvas.create_oval(1077, 315, 1208, 418, fill="", outline="")
    canvas.tag_bind(mstom, '<Button-1>', expmstom)
def showmrepsystem():
    global mrepsystem
    mrepsystem = canvas.create_oval(1121, 406, 1165, 434, fill="blue", outline="black")
    mrepsystem = canvas.create_oval(1091, 376, 1195, 464, fill="", outline="")
    canvas.tag_bind(mrepsystem, '<Button-1>', expmrepsystem)


#explanation for male body functions
def expmhead(event):
    expmhead1=canvas.create_line(1142, 135, 1000, 123)
    expmhead2=canvas.create_rectangle(770, 95, 1000, 123)
    expmhead3=canvas.create_text(885, 103, text="This diagnosis is know to affect:")
    expmhead4=canvas.create_text(885, 115, text="the brain and/or nervous system")
    canvas.update()
    def deleteexpmhead(event):
        canvas.delete(expmhead1)
        canvas.delete(expmhead2)
        canvas.delete(expmhead3)
        canvas.delete(expmhead4)
        canvas.update()
        showmhead()
    
    canvas.tag_bind(mhead, '<Button-1>', deleteexpmhead)
def expmheart(event):
    expmheart1=canvas.create_line(1145, 280, 780, 239)
    expmheart2=canvas.create_rectangle(550, 211, 780, 239)
    expmheart3=canvas.create_text(552, 220, text="This diagnosis is know to cause:", anchor=W)
    expmheart4=canvas.create_text(552, 232, text="chest pain and/or heart problems.", anchor=W)
    canvas.update()
    def deleteexpmheart(event):
        canvas.delete(expmheart1)
        canvas.delete(expmheart2)
        canvas.delete(expmheart3)
        canvas.delete(expmheart4)
        canvas.update()
        showmheart()
    canvas.tag_bind(mheart, '<Button-1>', deleteexpmheart)
    
def expmjoint(event): 
    expmjoint1=canvas.create_line(1076, 333, 750, 340)
    expmjoint2=canvas.create_rectangle(750, 340, 512, 310)
    expmjoint3=canvas.create_text(513, 317, text="This diagnosis is know to cause:", anchor=W)
    expmjoint4=canvas.create_text(513, 331, text="(chronic) joint and/or bone pain.", anchor=W)
    canvas.update()
    def deleteexpmjoint(event):
        canvas.delete(expmjoint1)
        canvas.delete(expmjoint2)
        canvas.delete(expmjoint3)
        canvas.delete(expmjoint4)
        canvas.update()
        showmjoint()
    canvas.tag_bind(mlelbow, '<Button-1>', deleteexpmjoint)

def expmstom(event): 
    expmstom1=canvas.create_line(1145, 368, 750, 375)
    expmstom2=canvas.create_rectangle(750, 375, 510, 345)
    expmstom3=canvas.create_text(513, 352, text="This diagnosis is know to cause:", anchor=W)
    expmstom4=canvas.create_text(513, 366, text="problems with the digestive systems.", anchor=W)
    canvas.update()
    def deleteexpmstom(event):
        canvas.delete(expmstom1)
        canvas.delete(expmstom2)
        canvas.delete(expmstom3)
        canvas.delete(expmstom4)
        canvas.update()
        showmstom()
    canvas.tag_bind(mstom, '<Button-1>', deleteexpmstom)

def expmrepsystem(event):
    expmrepsystem1=canvas.create_line(1145, 422, 750, 420)
    expmrepsystem2=canvas.create_rectangle(750, 420, 490, 390)
    expmrepsystem3=canvas.create_text(493, 397, text="This diagnosis is know to cause", anchor=W)
    expmrepsystem4=canvas.create_text(493, 411, text="problems with the reproductive system", anchor=W)
    canvas.update()
    def deleteexpmrepsystem(event):
        canvas.delete(expmrepsystem1)
        canvas.delete(expmrepsystem2)
        canvas.delete(expmrepsystem3)
        canvas.delete(expmrepsystem4)
        canvas.update()
        showmrepsystem()
    canvas.tag_bind(mrepsystem, '<Button-1>', deleteexpmrepsystem)


#Money Descriptor (RANGE MUST BE FROM 0 TO 21)
global money
money = PhotoImage(file = 'hundredbill.gif')
global tpmoney
money1 = PhotoImage(file = 'tphundredbill.gif')

def cost(x):
    if x==5:
        canvas.create_image(3+70*0, 93, image = money, anchor=NW)
        canvas.create_image(3+70*1, 93, image = money, anchor=NW)
        canvas.create_image(3+70*2, 93, image = money1, anchor=NW)
        canvas.create_image(3+70*3, 93, image = money, anchor=NW)
        canvas.create_image(3+70*4, 93, image = money1, anchor=NW)
    if x==7:
        canvas.create_image(3+70*0, 93, image = money, anchor=NW)
        canvas.create_image(3+70*1, 93, image = money, anchor=NW)
        canvas.create_image(3+70*2, 93, image = money1, anchor=NW)
        canvas.create_image(3+70*3, 93, image = money1, anchor=NW)
        canvas.create_image(3+70*4, 93, image = money, anchor=NW)
        canvas.create_image(3+70*5, 93, image = money1, anchor=NW)
        canvas.create_image(3+70*6, 93, image = money1, anchor=NW)
    if x>7 and x<15:
        canvas.create_image(3+70*0, 93, image = money, anchor=NW)
        canvas.create_image(3+70*1, 93, image = money, anchor=NW)
        canvas.create_image(3+70*2, 93, image = money, anchor=NW)
        canvas.create_image(3+70*3, 93, image = money1, anchor=NW)
        canvas.create_image(3+70*4, 93, image = money1, anchor=NW)
        canvas.create_image(3+70*5, 93, image = money, anchor=NW)
        canvas.create_image(3+70*6, 93, image = money1, anchor=NW)
        canvas.create_image(3+70*0, 123, image = money1, anchor=NW)
    if 19>x>14:
        for y in range (0,7):
            canvas.create_image(3+70*y, 93, image = money, anchor=NW)
        for y in range (0,4):
            canvas.create_image(3+70*y, 123, image = money, anchor=NW)
        canvas.create_image(3+70*5, 123, image = money1, anchor=NW)
        canvas.create_image(3+70*7, 123, image = money1, anchor=NW)
        canvas.create_image(3+70*6, 123, image = money, anchor=NW)
    if x==20:
        for y in range (0,7):
            canvas.create_image(3+70*y, 93, image = money, anchor=NW)
        for y in range (0,7):
            canvas.create_image(3+70*y, 123, image = money, anchor=NW)
        for y in range (0,2):
            canvas.create_image(3+70*y, 153, image = money, anchor=NW)
        canvas.create_image(3+70*2, 153, image = money1, anchor=NW)
        canvas.create_image(3+70*3, 153, image = money1, anchor=NW)
        canvas.create_image(3+70*4, 153, image = money, anchor=NW)
        canvas.create_image(3+70*5, 153, image = money1, anchor=NW)
        canvas.create_image(3+70*6, 153, image = money1, anchor=NW)
        
#Time Descriptor
global clock
clock = PhotoImage(file = 'clock.gif')
global clock1
clock1 = PhotoImage(file = 'clock1.gif')

def time(q):
    if q==3:
        canvas.create_image(3+32*0, 215, image = clock1, anchor=NW)
        canvas.create_image(3+32*1, 215, image = clock, anchor=NW)
        canvas.create_image(3+32*2, 215, image = clock1, anchor=NW)
    if q==4:
        canvas.create_image(3+32*0, 215, image = clock, anchor=NW)
        canvas.create_image(3+32*1, 215, image = clock1, anchor=NW)
        canvas.create_image(3+32*2, 215, image = clock, anchor=NW)
        canvas.create_image(3+32*3, 215, image = clock1, anchor=NW)
    if q==5:
        canvas.create_image(3+32*0, 215, image = clock, anchor=NW)
        canvas.create_image(3+32*1, 215, image = clock, anchor=NW)
        canvas.create_image(3+32*2, 215, image = clock1, anchor=NW)
        canvas.create_image(3+32*3, 215, image = clock, anchor=NW)
        canvas.create_image(3+32*4, 215, image = clock1, anchor=NW)
    if q==7:
        canvas.create_image(3+32*0, 215, image = clock, anchor=NW)
        canvas.create_image(3+32*1, 215, image = clock, anchor=NW)
        canvas.create_image(3+32*2, 215, image = clock, anchor=NW)
        canvas.create_image(3+32*3, 215, image = clock, anchor=NW)
        canvas.create_image(3+32*4, 215, image = clock1, anchor=NW)
        canvas.create_image(3+32*5, 215, image = clock, anchor=NW)
        canvas.create_image(3+32*6, 215, image = clock1, anchor=NW)
    if q==20:
        for y in range (0, 7):
            canvas.create_image(3+32*y, 215, image = clock, anchor=NW)
        for y in range (0, 7):
            canvas.create_image(3+32*y, 250, image = clock, anchor=NW)
        canvas.create_image(3+32*0, 285, image = clock, anchor=NW)
        canvas.create_image(3+32*1, 285, image = clock, anchor=NW)
        canvas.create_image(3+32*2, 285, image = clock, anchor=NW)
        canvas.create_image(3+32*3, 285, image = clock1, anchor=NW)
        canvas.create_image(3+32*4, 285, image = clock, anchor=NW)
        canvas.create_image(3+32*5, 285, image = clock1, anchor=NW)

def wait_screen():
    canvas.delete("all")
    canvas.create_text(635, 150, text="While learning about these different diagnoses, we want to heavily emphasis that these diagnoses", anchor=CENTER, fill="black", font=("arial",20))
    canvas.create_text(635, 170, text="should not be compared. None of these diagnoses should be considered \"worse\" than any other.", anchor=CENTER, fill="black", font=("arial", 20))
    canvas.create_text(635, 190, text="These diagnoses affect each person in a wide variety of ways and to simply compare them using", anchor=CENTER, fill="black", font=("arial",20))
    canvas.create_text(635, 210, text="this limited amount of information would be inappropriate and incorrect. The next screen will", anchor=CENTER, fill="black", font=("arial",20))
    canvas.create_text(635, 230, text="be automatically generated in 5 seconds.", anchor=CENTER, fill="black", font=("arial",20))
    tk.update()
    tk.after(17000)
    canvas.delete("all")
#Main Functions
def bipolar(x):
    #wait_screen()
    x=1
    canvas.delete("all")
    drawcanvas(1)
    showmhead()
    audiohead1=canvas.create_rectangle(770, 95, 1000, 123, fill='', outline='')
    canvas.tag_bind(audiohead1, '<Button-1>', audio_head)
    cost(8)
    time(5)
    canvas.create_text(5, 350, text="Those who are diagnosed with Bipolar I have a multifaceted", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 370, text="treatment method that consists of medications like: mood", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 390, text="stabilizers and antipsycotics combined with personal therapy.", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 470, text="Bipolar Disorder, Bipolar I, Bipolar II, Cyclothymic Disorder", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 490, text="Melancholy (From Ancient Greece, now obsolete), Dual-Form Insanity", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 510, text="(From 19th Century France, now obsolete), Manic-Depressive Psychosis", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 530, text="(From 19th Century Germnay, partially obsolete) and Manic-Depressive Illness", fill="black", font=("Times New Roman", 20), anchor=W)
def schizophrenia(x):
    #wait_screen()
    x=1
    canvas.delete("all")
    drawcanvas(1)
    showmhead()
    audiohead1=canvas.create_rectangle(770, 95, 1000, 123, fill='', outline='')
    canvas.tag_bind(audiohead1, '<Button-1>', audio_head)
    cost(14)
    time(7)
    canvas.create_text(5, 350, text="Those who are diagnosed with schizophrenia have a combined", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 370, text="treatment method that consists of antipsychotic medication", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 390, text="coupled with therapy that tries to encourage those dealing", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 410, text="with this diagnosis to find appropriate coping mechanisms.", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 470, text="Schizophrenia, Psychosis Susceptibility Syndrome (Proposed)", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 490, text="Dementia Praecox (From 19th Century Germany, now obsolete)", fill="black", font=("Times New Roman", 20), anchor=W)

def ptsd(x):
    #wait_screen()
    canvas.delete("all")
    drawcanvas(1)
    showmhead()
    audiohead1=canvas.create_rectangle(770, 95, 1000, 123, fill='', outline='')
    canvas.tag_bind(audiohead1, '<Button-1>', audio_head)
    cost(8)
    time(5)
    canvas.create_text(5, 350, text="Those who are diagnosed with Post Traumatic Stress Disorder", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 370, text="(PTSD) recieve a combination of therapy, including group and", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 390, text="solo therapy, along with medical treatments, which usually", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 410, text="include SSRIs, the same medicine used to treat symptoms of OCD.", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 470, text="Post Traumatic Stress Disorder, PTSD, Soldier's Heart (From American Civil War,", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 490, text="now obsolete), Da Costa's Syndrome (From mid 19th Century America, now obsolete)", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 510, text="Shell Shock (From Early 20th Century America, now obsolete), Combat Stress Reaction/CSR", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 530, text="(From mid 20th Century America, now obsolete)", fill="black", font=("Times New Roman", 20), anchor=W)
def ocd(x):
    #wait_screen()
    canvas.delete("all")
    drawcanvas(1)
    showmhead()
    audiohead1=canvas.create_rectangle(770, 95, 1000, 123, fill='', outline='')
    canvas.tag_bind(audiohead1, '<Button-1>', audio_head)
    cost(5)
    time(3)
    canvas.create_text(5, 350, text="Those who are diagnosed with OCD typically recieve", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 370, text="sessions with a therapist and also a type of medication", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 390, text="known as SSRIs, selective serotonin reuptake inhibitators,", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 410, text="which help treat symptons associated with OCD.", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 470, text="Obsessive Compulsive Disorder, OCD, Obsessive Compulsive Personality", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 490, text="Disorder", fill="black", font=("Times New Roman", 20), anchor=W)
 
def autism(x):
    #wait_screen()
    x=1
    canvas.delete("all")
    drawcanvas(1)
    showmhead()
    audiohead1=canvas.create_rectangle(770, 95, 1000, 123, fill='', outline='')
    canvas.tag_bind(audiohead1, '<Button-1>', audio_head)
    showmstom()
    audiostom1=canvas.create_rectangle(750, 375, 510, 345, fill="", outline="")
    canvas.tag_bind(audiostom1, '<Button-1>', audio_stom)
    cost(7)
    time(4)
    canvas.create_text(5, 350, text="Those who are diagnosed with autism typically recieve", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 370, text="treatment mediciation and are provided with therapy to", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 390, text="help facilitate commication skills and interactions with", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 410, text="their environment.", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 470, text="Autism, Autism Spectrum Disorder, Austistic Spectrum Disorder", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 490, text="ASD, Classic Autism, Kanner Autism, Pervasive Development Disorder,", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 510, text="PSD, High Function Autism, HFA, Asperger Syndrom", fill="black", font=("Times New Roman", 20), anchor=W)

def anorexia(x):
    #wait_screen()
    canvas.delete("all")
    drawcanvas(1)
    showmjoint()
    audiojoint1=canvas.create_rectangle(750, 340, 512, 310, fill='', outline='')
    canvas.tag_bind(audiojoint1, '<Button-1>', audio_joint)
    showmheart()
    audioheart1=canvas.create_rectangle(550, 211, 780, 239, fill='', outline='')
    canvas.tag_bind(audioheart1, '<Button-1>', audio_heart)
    showmstom()
    audiostom1=canvas.create_oval(1107, 345, 1178, 388, fill="", outline="")
    canvas.tag_bind(audiostom1, '<Button-1>', audio_stom)
    showmrepsystem()
    audiorep1=canvas.create_rectangle(750, 420, 490, 390, fill='', outline='')
    canvas.tag_bind(audiorep1, '<Button-1>', audio_rep)
    cost(20)
    time(20)
    canvas.create_text(5, 350, text="Those who are diagnosed with anorexia typically recieve", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 370, text="residential treatment where the patient is fed all meals", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 390, text="and constantly monitored. After this, the patient will", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 410, text="meet with a therpaist for 3-4 times a week until healthy.", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 470, text="Anorexia, Anorexia Nervosa, Binge-Eating Anorexia Nervosa", fill="black", font=("Times New Roman", 20), anchor=W)
    canvas.create_text(5, 490, text="Purging Anorexia Nervosa, Restricting Anorexia Nervosa", fill="black", font=("Times New Roman", 20), anchor=W)

#Creation of Buttons
button1 = Button(tk, text='Diagnosis 1', width=21, command=lambda: bipolar(1))
button1.pack(side=LEFT)

button2 = Button(tk, text='Diagnosis 2', width=21, command=lambda: schizophrenia(1))
button2.pack(side=LEFT)

button6 = Button(tk, text='Diagnosis 3', width=21, command=lambda: anorexia(1))
button6.pack(side=LEFT)

button3 = Button(tk, text='Diagnosis 4', width=21, command=lambda: ptsd(1))
button3.pack(side=LEFT)

button4 = Button(tk, text='Diagosis 5', width=21, command=lambda: ocd(1))
button4.pack(side=LEFT)

button5 = Button(tk, text='Diagnosis 6', width=21, command=lambda: autism(1))
button5.pack(side=LEFT)

#Keyboard Usage
tk.bind('<Key-1>', lambda x: bipolar(1))
tk.bind('<Key-2>', lambda x: schizophrenia(1))
tk.bind('<Key-3>', lambda x: anorexia(1))
tk.bind('<Key-4>', lambda x: ptsd(1))
tk.bind('<Key-5>', lambda x: ocd(1))
tk.bind('<Key-6>', lambda x: autism(1))


#Keyboard access to buttons

logo1=canvas.create_image(1280, 0, image=logo, anchor=NE)
canvas.create_rectangle(0, 0, 1280, 700, fill="white")
highlight_box = canvas.create_rectangle(504, 240, 1162, 259, fill="light blue", outline='')
canvas.create_text(635, 20, text="Mental Health Awareness Activism Project", anchor=CENTER, fill="dark blue", font=("arial",40))
canvas.create_text(635, 150, text="Welcome to our mental health awareness project!", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 170, text="We created this project to help users learn more about each of these mental diagnoses below.", anchor=CENTER, fill="black", font=("arial", 20))
canvas.create_text(635, 190, text="Before you begin using the user interface, it is very important that you gain some context about", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 210, text="our project. We strongly recommend reading an article discussing our project and a video that helps", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 230, text="highlight some of the initial problems with this interface and frame our interface. Both the video", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 250, text="and the article can be seen by clicking here: https://sites.duke.edu/NeuroDiversityAndInclusion/Articles/User-Interface/ ", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 270, text="Click the boxes at the bottom to browse through some common diagnoses and learn some information about", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 290, text="each. We have included information about the financial and time committment of each diagnosis. This information", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 310, text="is on a span, as represented by the semi-transparent objects. The highlighted parts of the body can", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 330, text="be clicked for brief descriptions. These description boxes can be clicked to play an audio recording of the", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 350, text="text included. Also, these diagnoses inlcude Anorexia, Post Traumatic Stress Disorder (PTSD), Obsessive", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 370, text="Compulsive Disorder (OCD), Schizophrenia, Autism and Bipolar. The discussion of these topics may be upsetting", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 390, text="to some. We want to disclose this information to our users and allow each user to make a decision about using", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 410, text="this interface that is appropriate for each user. The sources for our information can be found in the upper", anchor=CENTER, fill="black", font=("arial",20))
canvas.create_text(635, 430, text="left hand corner of our interface.", anchor=CENTER, fill="black", font=("arial",20))
circle=canvas.create_oval(515, 450, 780, 568, fill="gray", outline="black")
canvas.create_text(522, 507, text="I understand and would like to proceed.", font=("arial", 15), anchor=W)
canvas.tag_bind(circle, '<Button-1>', drawcanvas)
highlight_box = canvas.create_rectangle(474, 240, 1132, 259, fill="", outline='')

#Hyperlink to video
def open_link(event):
    webbrowser.open("https://sites.duke.edu/NeuroDiversityAndInclusion/Articles/User-Interface/")
canvas.tag_bind(highlight_box, '<Button-1>',open_link)

mainloop()
