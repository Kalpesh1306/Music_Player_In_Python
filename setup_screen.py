#setup screen 

import time
from tkinter import *
from PIL import Image,ImageTk
import os
import tkinter.messagebox
from tkinter import filedialog
from mutagen.mp3 import MP3  #for song length
from pygame import mixer  #used for music add
mixer.init()
class musicplayer:
    def __init__(self,Tk):
        self.root=Tk
        self.root.title('Music_Player')
        self.root.geometry('500x500')
        self.root.configure(background='white')
        
        #opnefile
        def Openfile():
            global filename
            filename=filedialog.askopenfilename()
        
        # Menu bar
        
        self.menubar=Menu(self.root)
        self.root.configure(menu=self.menubar)
        
        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File',menu=self.submenu)
        self.submenu.add_command(label='Open',command=Openfile)
        self.submenu.add_command(label='exit',command=self.root.destroy)
        
        def About():
            tkinter.messagebox.showinfo('About Us','Music Player Created  by Kalpesh Patil')
        
        self.submenu2=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Help',menu=self.submenu2)
        self.submenu2.add_command(label='About',command=About)
        
        #Adding Label
        self.filelabel=Label(text='Select and play',bg='black',fg='white',font=22).place(x=80,y=50)
        
        
        
        def songinf():
            self.filelabel=Label['text']='Current Music :-' + os.path.basename(filename)
             
                   
        #Adding leftside image
        # L =left
        self.L_photo=ImageTk.PhotoImage(file='music_waves.jpg')
        L_photo=Label(self.root,image=self.L_photo,bg='white').place(x=800,y=200)
        
        
        #Adding image.........
        self.photo=ImageTk.PhotoImage(file='music_bag.jpg')
        photo=Label(self.root,image=self.photo,bg='white').place(x=100,y=100)
        
        #leble
        self.label1=Label(self.root,text='Lets Play It.',bg='black',fg='white',font=20)
        self.label1.pack(side=BOTTOM,fill=X)
        
        
        #functions start music
        def playmusic():
            try:
                paused
            except NameError:    
                try:
                     mixer.music.load(filename)
                     mixer.music.play()
                     self.label1['text']='Music Playing.....'
                     songinf()
                     
                except:
                   pass #  tkinter.messagebox.showerror('Error','File could not found')
            
            else:
                mixer.music.unpause()
                self.label1['text']='Music Unpaused...'
                
        # for song length
        def length_bar():
            #select mp3 songs--
            song_mut=MP3(filename)
            #get length of song---
            song_mut_length=song_mut.info.length
       
            #convert into min and seconds
            convert_song_mut_length=time.strtime('%M:%S',time.gmtime(song_mut_length))
        
           #blit on screen
            self.lengthbar.configure(text=f'Total_Length:-00:{convert_song_mut_length}')
            
        # lengthbar pf songs
        
        self.lengthbar=Label(self.root,text='Total_Length:-00:00').place(x=300,y=50)  
         
                
        #creating Button
        #play_button
        self.photo_b1=ImageTk.PhotoImage(file='playbtn.jpg')
        photo_b1=Button(self.root,image=self.photo_b1,bg='white',bd=0,command=playmusic).place(x=100,y=610)
        
 
       #functions pause music
        def pausemusic():
            global paused
            paused = TRUE
            mixer.music.pause()
            self.label1['text']='Music Pause.....'
            
        #creating Button
        #pasue_button
        self.photo_b2=ImageTk.PhotoImage(file='pausebtn.jpg')
        photo_b2=Button(self.root,image=self.photo_b2,bg='white',bd=0,command=pausemusic).place(x=230,y=610)
        
        
       #functions start music
        def stopmusic():
            mixer.music.stop()
          
            self.label1['text']='Music Stop.....'
            
        
        #creating Button
        #stop_button
        self.photo_b3=ImageTk.PhotoImage(file='stopbtn.jpg')
        photo_b3=Button(self.root,image=self.photo_b3,bg='white',bd=0,command=stopmusic).place(x=360,y=610)
        
        #mute
        def mute():
           self.scale.set(0)
           self.mute=ImageTk.PhotoImage(file='mute.jpg')
           mute=Button(self.root,image=self.mute,bd=0,bg='white',command=unmute).place(x=500,y=610)
           self.label1['text']='Music Mute'
        # unmute  
        def unmute():
           self.scale.set(25) 
           self.volimg=ImageTk.PhotoImage(file='volume.png')
           volimg=Button(self.root,image=self.volimg,bg='white',bd=0,command=mute).place(x=500,y=610)
           self.label1['text']='Music UnMute'
          
        #volume - barimg
        self.volimg=ImageTk.PhotoImage(file='volume.png')
        volimg=Button(self.root,image=self.volimg,bg='white',bd=0,command=mute).place(x=500,y=610)
        
        #function for volume bar
        def volume(vol):
            volume=int(vol)/100
            mixer.music.set_volume(volume)
        
       
       # volume bar
        self.scale=Scale(self.root,from_=0,to=100,orient=HORIZONTAL,bg='cyan',length=200,command=volume)
        self.scale.set(25)
        self.scale.place(x=800,y=600)
      
       
               
root = Tk()
obj = musicplayer(root)
root.mainloop()        
    
