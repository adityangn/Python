import matplotlib.pyplot as plt
estimates=[1000,200,240,700,529,379,282,900,500]
y=[]
for i in range(len(estimates)):
    y.append(5)
estimates.sort()
tv=int(0.1*(len(estimates)))
estimates=estimates[tv:]
estimates=estimates[:len(estimates)-tv]
plt.plot(estimates,y,'r--')