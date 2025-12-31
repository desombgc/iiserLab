"NEWTON'S RING EXPT. on 08/08/2025"
import numpy as np
import matplotlib.pyplot as plt
D=[0.84,1.33,1.76,2.09,2.41,2.66,2.88,3.11,3.28,3.49]
D_square=[i**2 for i in D ]
#print(D_square)
D2=[1.42,2.51,3.89,5.10,6.38,7.82,9.09,10.41,11.48] #successive D^2 difference b/w rings in mm^2
ring_no=np.linspace(1,9,9)
slope=np.polyfit(ring_no,D2,deg=1)
polynomial=np.poly1d(slope)
print(slope)
y=polynomial(ring_no)
plt.scatter(ring_no,D2,marker='o',color='red',label='Data Points')
plt.plot(ring_no,y,color="blue",label="Fit: y=1.285x+0.034")
plt.xlabel('number of Rings $m1-m2$')
plt.ylabel('$D^2_{n+m_1}$-$D^2_{n+m_2}$ in mm^2')
plt.title("Newton's Rings")
plt.legend(loc = 'best', prop = {'size':10})
plt.grid()
plt.show()