import numpy as np
import matplotlib.pyplot as plt

#Plot Grafik
to= 0 #xawal
tn = 300 #xakhir
ndata = 1000 #sumbuY

t = np.linspace(to,tn,ndata)
h = t[2] - t[1]

N = 1000 #Masyarakat
I0 = 1 #Terinfeksi
R0 = 0 #Sembuh
S0 = N-I0-R0 #Suspek 

I = np.zeros(ndata)
S = np.zeros(ndata)
R = np.zeros(ndata)

I[0] = I0
R[0] = R0
S[0] = S0

beta = 0.2
gamma = 0.1
for i in range (0,ndata-1):
      S[i+1]= S[i] - h*beta/N*S[i]*I[i]
      I[i+1] = I[i] + h*beta/N*S[i]*I[i]-h*gamma*I[i]
      R[i+1] = R[i] + h*gamma*I[i]

plt.plot(t,S, label ='S')
plt.plot(t,I,label = 'I')
plt.plot(t,R,label = 'R')

plt.legend()
plt.show()
