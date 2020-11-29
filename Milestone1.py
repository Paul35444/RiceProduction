####### Milestone 1 Python Script
import pandas as pd
import scipy.stats as st
from snhu_MAT243 import prop_1samp_ztest
from snhu_MAT243 import means_1samp_ttest



##Step 1: Import your data set
##-----------------------------------------------------------------------------
production = pd.read_csv('Rice_Production.csv')



##Step 2: Calculate descriptive statistics 
##-----------------------------------------------------------------------------
print ('Descriptive Statistics - Step 2')
print ('')

print ('Mean')
print (production[['Company1']].mean())
print ('')

print ('Median')
print (production[['Company1']].median())
print ('')

print ('Mode')
print (production[['Company1']].mode())
print ('')

print ('Minimum')
print (production[['Company1']].min())
print ('')

print ('Maximum')
print (production[['Company1']].max())
print ('')

print ('Variance')
print (production[['Company1']].var())
print ('')

print ('Standard Deviation')
print (production[['Company1']].std())
print ('')

print ('Describe')
print (production[['Company1']].describe())
print ('')

print ('')

##Step 3: Calculate descriptive statistics
##-----------------------------------------------------------------------------
print ('Descriptive Statistics - Step 3')
print ('')

print ('Mean')
print (production[['Company2']].mean())
print ('')

print ('Median')
print (production[['Company2']].median())
print ('')

print ('Mode')
print (production[['Company2']].mode())
print ('')

print ('Minimum')
print (production[['Company2']].min())
print ('')

print ('Maximum')
print (production[['Company2']].max())
print ('')

print ('Variance')
print (production[['Company2']].var())
print ('')

print ('Standard Deviation')
print (production[['Company2']].std())
print ('')

print ('Describe')
print (production[['Company2']].describe())
print ('')


##Step 4: Construct confidence interval for population proportion
##-----------------------------------------------------------------------------
print ('Confidence Interval - Step 4')
n = production[['Company1']].count()
x = (production[['Company1']] > 307200.0).values.sum()
p = x/n*1.0
stderror = (p * (1 - p)/n)**0.5
print (st.norm.interval(0.99, p, stderror))
print ('')



##Step 5: Construct confidence interval for population mean
##-----------------------------------------------------------------------------
print ('Confidence Interval - Step 5')
n = production[['Company2']].count()
df = n - 1
mean = production[['Company2']].mean()
stdev = production[['Company2']].std()
stderror = stdev/(n**0.5)
print (st.t.interval(0.95, df, mean, stderror))
print ('')



##Step 6: Perform hypothesis test for population proportion
##-----------------------------------------------------------------------------
print ('Hypothesis Test - Step 6')
n = production[['Company1']].count()
x = (production[['Company1']] > 307200.0).values.sum()
null_value = 0.29
alternative = 'smaller'
print (prop_1samp_ztest(x, n, null_value, alternative))
print ('')



##Step 7: Perform hypothesis test for population mean
##-----------------------------------------------------------------------------
print ('Hypothesis Test - Step 7')
n = production[['Company2']].count()
df = n - 1
mean = production[['Company2']].mean()
std_dev = production[['Company2']].std()
null_value = 209500.0
alternative = 'not-equal'
print (means_1samp_ttest(mean, std_dev, n, null_value, alternative))
print ('')