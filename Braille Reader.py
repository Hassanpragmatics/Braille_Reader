import RPi.GPIO as GPIO #we need to run it on rasyberry pie 
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)#21
GPIO.setup(38,GPIO.OUT)#20
GPIO.setup(36,GPIO.OUT)#16
GPIO.setup(33,GPIO.OUT)#13
GPIO.setup(35,GPIO.OUT)#19
GPIO.setup(37,GPIO.OUT)#26
GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.output(40,GPIO.LOW)
GPIO.output(38,GPIO.LOW)
GPIO.output(36,GPIO.LOW)
GPIO.output(33,GPIO.LOW)
GPIO.output(35,GPIO.LOW)
GPIO.output(37,GPIO.LOW)

def start_system(channel):
    global start
    global read_counter
    global inter
    if ((start==0)&(read_counter==0)):
        start=1
    if ((read_counter==0)&(inter==1)):
        read_counter=1

def audio_stuff(channel):
    global audio_counter
    global audio
    print('in 2')
    audio_counter=audio_counter+1
    if (audio_counter==2):
        audio=1
    if (audio_counter==4):
        audio=0
        audio_counter=(audio_counter)%4
    time.sleep(0.25)

def inputchange3(channel):
    global allow
    global j
    global text
    print('in 3')
    if allow==1:
        if((j+10)<(len(text))):
           j=j+10

def inputchange4(channel):
    global allow
    global j
    global text
    print('in 4')
    if allow==1:
        if((j-10)>1):
           j=j-10
           

def inputchange5(channel):
    global allow
    global j
    global text
    print('in 5')
    j=len(text)
           

GPIO.add_event_detect(7 ,GPIO.RISING, callback=start_system, bouncetime=3)
GPIO.add_event_detect(8 ,GPIO.RISING, callback=audio_stuff, bouncetime=3)
GPIO.add_event_detect(10 ,GPIO.RISING, callback=inputchange3, bouncetime=3)
GPIO.add_event_detect(11 ,GPIO.RISING, callback=inputchange4, bouncetime=3)
GPIO.add_event_detect(15 ,GPIO.RISING, callback=inputchange5, bouncetime=3)

while(1):
    from os import walk
    import os
    from subprocess import check_output
    from gpiozero import LED
    import time

    def braill(alphabet):
        code=[0,0,0,0,0,0]
        print ('inside function : ' + alphabet)
        if((ord(alphabet)>64) &(ord(alphabet)<91)):
            GPIO.output(37,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(37,GPIO.LOW)
           
        if((ord(alphabet)>47)&(ord(alphabet)<58)):
            GPIO.output(37,GPIO.HIGH)
            GPIO.output(36,GPIO.HIGH)
            GPIO.output(33,GPIO.HIGH)
            GPIO.output(35,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(37,GPIO.LOW)
            GPIO.output(36,GPIO.LOW)
            GPIO.output(35,GPIO.LOW)
            GPIO.output(33,GPIO.LOW)

        if ((alphabet=='a') | (alphabet=='A') | (alphabet=='1')):
            code=[0, 0, 0, 0, 0, 0]
        if ((alphabet=='b') | (alphabet=='B') | (alphabet=='2')):
            code=[1, 1, 0, 0, 0, 0]
        if ((alphabet=='c') | (alphabet=='C') | (alphabet=='3')):
            code=[1, 0, 0, 1, 0, 0]
        if ((alphabet=='d') | (alphabet=='D') | (alphabet=='4')):
            code=[1, 0, 0, 1, 1, 0]
        if ((alphabet=='e') | (alphabet=='E') | (alphabet=='5')):
            code=[1, 0, 0, 0, 1, 0]
        if ((alphabet=='f') | (alphabet=='F') | (alphabet=='6')):
            code=[1, 1, 0, 1, 0, 0]
        if ((alphabet=='g') | (alphabet=='G') | (alphabet=='7')):
            code=[1, 1, 0, 1, 1, 0]
        if ((alphabet=='h') | (alphabet=='H') | (alphabet=='8')):
            code=[1, 1, 0, 0, 1, 0]
        if ((alphabet=='i') | (alphabet=='I') | (alphabet=='9')):
            code=[0, 1, 0, 1, 0, 0]
        if ((alphabet=='j') | (alphabet=='J') | (alphabet=='0')):
            code=[0, 1, 0, 1, 1, 0]
        if ((alphabet=='k') | (alphabet=='K')):
            code=[1, 0, 1, 0, 0, 0]
        if ((alphabet=='l') | (alphabet=='L')):
            code=[1, 1, 1, 0, 0, 0]
        if ((alphabet=='m') | (alphabet=='M')):
            code=[1, 0, 1, 1, 0, 0]
        if ((alphabet=='n') | (alphabet=='N')):
            code=[1, 0, 1, 1, 1, 0]
        if ((alphabet=='o') | (alphabet=='O')):
            code=[1, 0, 1, 0, 1, 0]
        if ((alphabet=='p') | (alphabet=='P')):
            code=[1, 1, 1, 1, 0, 0]
        if ((alphabet=='q') | (alphabet=='Q')):
            code=[1, 1, 1, 1, 1, 0]
        if ((alphabet=='r') | (alphabet=='R')):
            code=[1, 1, 1, 0, 1, 0]
        if ((alphabet=='s') | (alphabet=='S')):
            code=[0, 1, 1, 1, 0, 0]
        if ((alphabet=='t') | (alphabet=='T')):
            code=[0, 1, 1, 1, 1, 0]
        if ((alphabet=='u') | (alphabet=='U')):
            code=[1, 0, 1, 0, 0, 1]
        if ((alphabet=='v') | (alphabet=='V')):
            code=[1, 1, 1, 0, 0, 1]
        if ((alphabet=='w') | (alphabet=='W')):
            code=[0, 1, 0, 1, 1, 1]
        if ((alphabet=='x') | (alphabet=='X')):
            code=[1, 0, 1, 1, 0, 1]
        if ((alphabet=='y') | (alphabet=='Y')):
            code=[1, 0, 1, 1, 1, 1]
        if ((alphabet=='z') | (alphabet=='Z')):
            code=[1, 0, 1, 0, 1, 1]
       
        if (alphabet=='.'):
            code=[0, 1, 0, 0, 1, 1]
        if (alphabet==','):
            code=[0, 1, 0, 0, 0, 0]
        if (alphabet==':'):
            code=[0, 1, 0, 0, 1, 0]
        if (alphabet==';'):
            code=[0, 1, 1, 0, 0, 0]
        if (alphabet=='?'):
            code=[0, 1, 1, 0, 0, 1]
        if (alphabet=='!'):
            code=[0, 1, 1, 0, 1, 0]
        if ((alphabet=='(') | (alphabet==')')):
            code=[0, 1, 1, 0, 1, 1]
        if (alphabet=='"'):
            code=[0, 1, 1, 0, 0, 1]
        if (alphabet=='+'):
            code=[0, 1, 1, 0, 1, 0]
        if (alphabet=='-'):
            code=[0, 1, 0, 0, 1, 0]
        if (alphabet=='*'):
            code=[0, 0, 1, 0, 1, 0]
        if (alphabet=='@'):
            code=[0, 0, 1, 1, 1, 0]
        if (alphabet=='<'):
            code=[1, 1, 0, 0, 0, 1]
        if (alphabet=='>'):
            code=[0, 0, 1, 1, 1, 0]
        if (alphabet=='/'):
            code=[0, 0, 1, 1, 0, 0]
        if (alphabet=='='):
            code=[0, 1, 1, 1, 1, 0]
        if (alphabet=='#'):
            code=[0, 0, 1, 1, 1, 1]
        if (alphabet=='_'):
            code=[0, 0, 1, 0, 1, 1]
     
        if(code[0]==1):
            GPIO.output(40,GPIO.HIGH)
        if(code[1]==1):
            GPIO.output(38,GPIO.HIGH)
        if(code[2]==1):
            GPIO.output(36,GPIO.HIGH)
        if(code[3]==1):
            GPIO.output(33,GPIO.HIGH)
        if(code[4]==1):
            GPIO.output(35,GPIO.HIGH)
        if(code[5]==1):
            GPIO.output(37,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(40,GPIO.LOW)
        GPIO.output(38,GPIO.LOW)
        GPIO.output(36,GPIO.LOW)
        GPIO.output(33,GPIO.LOW)
        GPIO.output(35,GPIO.LOW)
        GPIO.output(37,GPIO.LOW)

    for dirpath, dirnames, filenames in walk('/home/pi/Documents'):
        print(filenames)

    d=os.getcwd()
    print(d)
    d1=os.path.join(d,"Documents")
    print(d1)

    start=0
    allow=0
    read_counter=0
    inter=0
    audio_counter=0
    audio=0

    while (1):
        print("start_up stage, start = 0")
        if(start >0):
            break

    counter=-1
    #speak = check_output(['espeak','following readable files are available in the folder'])
    inter=1
    for x in filenames:
        counter=counter+1
        #speak = check_output(['espeak',x])
        #speak = check_output(['espeak','if you want to read this press the button'])
        time.sleep(1)
        if(read_counter==1):
            break
       
    i=0;

    fname=os.path.join(d1,filenames[i])
    f=open(fname,"r")
    text= f.read()
    text =text.split(' ')
    print (len(text))
    j=0
    while j<len(text):
        print(text[j])
        allow=1
        if audio==1:
            speak = check_output(['espeak',text[j]])
        if audio==0:
            for my_character in text[j]:
                co=braill(my_character)
        j=j+1

    speak = check_output(['espeak','the file ends '])

GPIO.output(40,GPIO.LOW)
GPIO.output(38,GPIO.LOW)
GPIO.output(36,GPIO.LOW)
GPIO.output(33,GPIO.LOW)
GPIO.output(35,GPIO.LOW)
GPIO.output(37,GPIO.LOW)

f.close
GPIO.cleanup()
