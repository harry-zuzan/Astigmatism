import numpy
import cmath

def spokes(n, rad1, rad2, vshift):
	theta = (2.0*cmath.pi)/n

	p1 = complex(rad1,vshift)
	p2 = complex(rad2,vshift)

	idx = 0
	while idx < n:
		rotn1 = p1*cmath.rect(1,idx*theta)
		rotn2 = p2*cmath.rect(1,idx*theta)

		yield (rotn1.real,rotn2.real),(rotn1.imag,rotn2.imag)

		idx += 1


spoke_gen0 = spokes(32,1.0,4.0,0.0)
spoke_gen1 = spokes(32,1.0,4.0,-0.025)
spoke_gen2 = spokes(32,1.0,4.0,0.025)
spoke_gen3 = spokes(4,0.5,0.9,0.0)
spoke_gen4 = spokes(8,0.7,0.9,0.0)
	
import matplotlib
matplotlib.use('Agg')
from pylab import plt
plt.gcf().set_size_inches(8,8)

while 1:
	try:
		x,y = next(spoke_gen0)
#		plt.plot(x,y,c='0.0',lw=1,ls='-')
	except: break

while 1:
	try:
		x,y = next(spoke_gen1)
		plt.plot(x,y,c='0.0',lw=1,ls='-')
	except: break

while 1:
	try:
		x,y = next(spoke_gen2)
		plt.plot(x,y,c='0.0',lw=1,ls='-')
	except: break

while 1:
	try:
		x,y = next(spoke_gen3)
		plt.plot(x,y,c='0.0',lw=1,ls='-')
	except: break

while 1:
	try:
		x,y = next(spoke_gen4)
		plt.plot(x,y,c='0.0',lw=1,ls='-')
	except: break

plt.xlim(-4,4)
plt.ylim(-4,4)

plt.axis('off')
plt.savefig('spokes.pdf')
