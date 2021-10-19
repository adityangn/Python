from scipy import stats
estimates = [100,100,120,150,150,150,172,175,178,180,190,192,199,230,250,250,275,375,400,500,580,780,920,1000,1200]
estimates.sort()
m=stats.trim_mean(estimates,0.1)
print(m)