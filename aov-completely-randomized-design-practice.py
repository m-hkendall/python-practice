sample1 = [5.0, 17.0, 12.0, 10.0, 4.0]
sample2 = [19.0, 10.0, 9.0, 7.0, 5.0]
sample3 = [25.0, 15.0, 12.0, 9.0, 8.0]

n1 = input("Enter sample size 1: ")
n1 = int(n1)
n2 = input("Enter sample size 2: ")
n2 = int(n2)
n3 = input("Enter sample size 3: ")
n3 = int(n3)
totalSampleSize = n1 + n2 + n3
print("Total sample size: ", totalSampleSize)

sampleMean1 = (sum(sample1)/n1)
print("Sample Mean 1: ", sampleMean1)
sampleMean2 = (sum(sample2)/n2)
print("Sample Mean 2: ", sampleMean2)
sampleMean3 = (sum(sample3)/n3)
print("Sample Mean 3: ", sampleMean3)

totalMean = (((sampleMean1*n1)+(sampleMean2*n2)+(sampleMean3*n3))/totalSampleSize)
totalMean= round(totalMean, ndigits=1)
print("Total mean: ", totalMean)

sampleVariance1 = (((sample1[0]-sampleMean1)**2)+((sample1[1]-sampleMean1)**2)+((sample1[2]-sampleMean1)**2)+((sample1[3]-sampleMean1)**2)+((sample1[4]-sampleMean1)**2))/(n1-1)
print("Sample 1 variance: ", sampleVariance1)
sampleVariance2 = (((sample2[0]-sampleMean2)**2)+((sample2[1]-sampleMean2)**2)+((sample2[2]-sampleMean2)**2)+((sample2[3]-sampleMean2)**2)+((sample2[4]-sampleMean2)**2))/(n2-1)
print("Sample 2 variance: ", sampleVariance2)
sampleVariance3 = (((sample3[0]-sampleMean3)**2)+((sample3[1]-sampleMean3)**2)+((sample3[2]-sampleMean3)**2)+((sample3[3]-sampleMean3)**2)+((sample3[4]-sampleMean3)**2))/(n3-1)
sampleVariance3 = round(sampleVariance3,ndigits=1)
print("Sample 3 variance: ", sampleVariance3)

df1 = n1-3
print("df1: ", df1)
df2 = totalSampleSize-3
print("df2: ", df2)
dft = totalSampleSize-1
print("dft: ", dft)

SSB = (n1*((sampleMean1-totalMean)**2))+(n2*((sampleMean2-totalMean)**2))+(n3*((sampleMean3-totalMean)**2))
print("SSB: ", SSB)