import math
import numpy as np
import matplotlib.pyplot as plt

#if the input source is current :
#Imax = int(input()
Imax = 1
print("hi!, welcome to simple RLC circuit ! i will show u the current on each branch on reppetetive phasor diagrams from some frequencies lower , exact and higher than resonance frequency!")
R = float(input("pls enter the value of resistance: "))
L = float(input("pls enter the value of inductance: "))
C = float(input("pls enter the value of capacitance: "))

#resonace frequecy
w0 = 1/math.sqrt(L*C)
#creating the admittace vector
for i in range(1, int(2*w0)):
	w = i
	Re = 1/R
	Im = w*C - 1/(w*L)
	Z = np.array([Re, Im])
	#creating the 90B-admittace vector
	w1 = np.array([Im, -1*Re])
	#creating the 90A-admittace vector
	w2 = np.array([-1*Im, Re])
	#fixed vectors
	length = 1/(Re**2 + Im**2)
	IR = np.array([(Re/R)*length,(-1*Im/R)*length])
	Ic = np.array([Im*w*C*length, Re*w*C*length])
	IL = np.array([-1*Im/(w*L)*length, -1*Re/(w*L)*length])
	#angel of admittance
	φ = math.degrees(math.atan2(Im, Re))

	#create the plot
	fig, ax = plt.subplots()

	#add vectors to the plot , note : change the scale for better view
	ax.quiver(0, 0, IR[0], IR[1], angles = 'xy', scale_units = 'xy',scale = 1,  color='r')
	ax.quiver(0, 0, Ic[0], Ic[1], angles = 'xy', scale_units = 'xy',scale = 1,  color='g')
	ax.quiver(0, 0, IL[0], IL[1], angles = 'xy', scale_units = 'xy',scale = 1,  color='b')

	#set the x limit and y limit of the plot
	lim_x = max(abs(Re)/R, abs(Im)*w*C, abs(Im)/(w*L))*length 
	lim_y = max(abs(Im)/R, abs(Re)*w*C, abs(Re)/(w*L))*length 
	ax.set_xlim([-lim_x-lim_y, lim_x+lim_y]) 
	ax.set_ylim([-lim_x-lim_y, lim_x+lim_y])

	#show the plot
	plt.grid()
	plt.title("RESONANCE")
	plt.xlabel("real")
	plt.ylabel("imaginary")
	plt.show()
