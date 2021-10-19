import statistics
import matplotlib.pyplot as plt
estimates=[1000,200,240,700,529,379,282,900,500]
y=[]
estimates.sort()
tv=int(0.1*(len(estimates)))
estimates=estimates[tv:]
estimates=estimates[:len(estimates)-tv]
for i in range(len(estimates)):
    y.append(5)
plt.plot(estimates,y,'r--')
plt.plot([statistics.mean(estimates)],[5],'ro')
plt.plot([statistics.median(estimates)],[5],'bs')
plt.plot([375],[5],'g^')