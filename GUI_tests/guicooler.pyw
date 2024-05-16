# from tkinter import *
# from PIL import ImageTk, Image
# import random
# import keyboard
# import time
# import win32api
# import os
# from pynput import keyboard
# import screen_brightness_control as sbc
# from time import sleep
# import threading
# current_brightness=sbc.get_brightness()
#
# root=Tk()
# root.title("Cooler")
# root.configure(bg="#1C1C1C")
# main_frame= LabelFrame(root,bd=0,bg="#1C1C1C",text="Cool PC",fg="#009999",font=("Orbitron",14))
# #root.iconbitmap("icons\\snow.ico")
# #label1=Label(main_frame,text="Cooler",bd=0).pack()
#
# """col1=Label(main_frame, text="").grid(row=1,column=1,rowspan=4)
# col2=Label(main_frame, text="").grid(row=2,column=2,rowspan=4)
# col3=Label(main_frame, text="").grid(row=3,column=3,rowspan=4)"""
#
# stop_threads=False
#
# def auto_on():
# 	global current_brightness
# 	global stop_threads
# 	savedpos=win32api.GetCursorPos()
# 	while True:
# 			curpos=win32api.GetCursorPos()
# 			if savedpos!=curpos:
# 				savedpos=curpos
# 				current_brightness=sbc.get_brightness
# 				current_brightness=sbc.get_brightness()
# 				os.system('cmd /C "powercfg /S 637d3e2d-0c49-46e5-be77-1a408d584551"')#highperf
# 				sbc.set_brightness(current_brightness,display=0)
# 				#time.sleep(1)
# 			else:
# 				os.system('cmd /C "powercfg /S 8ab6f04d-cba8-4fcf-8dbb-751546bb7f2e')#coolmode
# 				sbc.set_brightness(current_brightness,display=0)
# 				#time.sleep(1)
# 			#time.sleep(3)
# 			if stop_threads:
# 				break
#
#
# def auto_off():
# 	global stop_threads, r
# 	stop_threads = True
# 	os.system('cmd /C "powercfg /S 637d3e2d-0c49-46e5-be77-1a408d584551"')
#
#
#
#
# def clicked(choice):
# 	if(choice==1):
# 		current_brightness=sbc.get_brightness()
# 		os.system('cmd /C "powercfg /S 8ab6f04d-cba8-4fcf-8dbb-751546bb7f2e"')
# 		sbc.set_brightness(current_brightness, display=0)
# 		auto_off()
#
# 	elif(choice==2):
# 		current_brightness=sbc.get_brightness()
# 		os.system('cmd /C "powercfg /S 125a7300-96d9-4d55-901e-d0d12f0e4f6d"')
# 		sbc.set_brightness(current_brightness, display=0)
# 		auto_off()
# 	elif(choice==3):
# 		current_brightness=sbc.get_brightness()
# 		os.system('cmd /C "powercfg /S 637d3e2d-0c49-46e5-be77-1a408d584551"')         #high perf.
# 		sbc.set_brightness(current_brightness, display=0)
# 		auto_off()
# 	elif(choice==4):
# 		current_brightness=sbc.get_brightness()
# 		os.system('cmd /C "powercfg /S 381b4222-f694-41f0-9685-ff5bb260df2e"')
# 		sbc.set_brightness(current_brightness, display=0)
# 		auto_off()
# 	else:
# 		pass
#
#
#
#
#
#
#
#
#
#
#
# r= IntVar()
# r.set(3)
#
# Radiobutton(main_frame, text="Cool PC at once",bg="#1C1C1C",activebackground="#009999",fg="#009999",font=("Orbitron",14),  variable=r, value=1,command= lambda: clicked(r.get())).grid(row=0,column=0,ipadx=20,sticky=W)
# Radiobutton(main_frame, text="Cool with sudo powers",bg="#1C1C1C",activebackground="#009999",fg="#009999",font=("Orbitron",14),  variable=r, value=2,command= lambda: clicked(r.get())).grid(row=1,column=0,ipadx=20,sticky=W)
# Radiobutton(main_frame, text="Gain Performance",bg="#1C1C1C",activebackground="#009999",fg="#009999",font=("Orbitron",14),  variable=r, value=3,command= lambda: clicked(r.get())).grid(row=2,column=0,ipadx=20,sticky=W)
# Radiobutton(main_frame, text="Balanced Performance",bg="#1C1C1C",activebackground="#009999",fg="#009999",font=("Orbitron",14), variable=r, value=4,command= lambda: clicked(r.get())).grid(row=3,column=0,ipadx=20,sticky=W)
# Radiobutton(main_frame, text="Auto Cooling On",bg="#1C1C1C",activebackground="#009999",fg="#009999",font=("Orbitron",14), variable=r, value=5,  command= lambda: threading.Thread(target=auto_on).start()).grid(row=4,column=0,ipadx=20,sticky=W)
# Button2 =Button(main_frame, text="Auto Cooling Off",bg="#1C1C1C",activebackground="#009999",fg="#009999",font=("Orbitron",14),  command= lambda: auto_off()).grid(row=4,column=1,ipadx=20,sticky=W)
#
#
#
#
#
# main_frame.pack()
#
#
#
#
# root.mainloop()
#
#
#
#
# '''
# def rest():
#     current_brightness=sbc.get_brightness
#     os.system('cmd /C "powercfg /S 8ab6f04d-cba8-4fcf-8dbb-751546bb7f2e"') #coolmode
#
#     sbc.set_brightness(current_brightness, display=0)
#     sleep(2.5)
# '''
