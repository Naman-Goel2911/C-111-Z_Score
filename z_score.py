import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics as stats
import random

df = pd.read_csv('medium_data.csv')
data = df['claps'].tolist()

population_mean = stats.mean(data)
population_stdev = stats.stdev(data)
print(f'The mean of the population is {population_mean}')
print(f'The Standard Deviation of the population is {population_stdev}')

def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        randomData = random.randint(0, len(data)-1)
        value = data[randomData]
        dataset.append(value)
    mean = stats.mean(dataset)
    return mean

mean_list = []

for i in range(0, 1000):
    setOfMeans = randomSetOfMean(100)
    mean_list.append(setOfMeans)

finalMean = stats.mean(mean_list)
finalStDev = stats.stdev(mean_list)

stdev1Start, stdev1End = finalMean-finalStDev, finalMean + finalStDev
stdev2Start, stdev2End = finalMean-(2*finalStDev), finalMean + (2*finalStDev)
stdev3Start, stdev3End = finalMean-(3*finalStDev), finalMean + (3*finalStDev)

print(f'The mean for sampling data is {finalMean}')
print(f'The standard deviation for sampling data is {finalStDev}')

df1 = pd.read_csv('medium_data.csv')
data1 = df1['reading_time'].tolist()

sampleMean1 = stats.mean(data1)

fig = ff.create_distplot([mean_list], ['Maths Score'], show_hist=False)
fig.add_trace(go.Scatter(x=[sampleMean1, sampleMean1], y=[0, 0.35], mode = 'lines', name = 'SampleMean1'))
fig.add_trace(go.Scatter(x=[finalMean, finalMean], y=[0, 0.2], mode='lines', name='Mean'))
fig.add_trace(go.Scatter(x=[stdev1Start, stdev1Start], y=[0, 0.2], mode='lines', name='First'))
fig.add_trace(go.Scatter(x=[stdev2Start, stdev2Start], y=[0, 0.2], mode='lines', name='Second'))
fig.add_trace(go.Scatter(x=[stdev3Start, stdev3Start], y=[0, 0.2], mode='lines', name='Third'))
fig.add_trace(go.Scatter(x=[stdev1End, stdev1End], y=[0, 0.2], mode='lines', name='EndFirst'))
fig.add_trace(go.Scatter(x=[stdev2End, stdev2End], y=[0, 0.2], mode='lines', name='EndSecond'))
fig.add_trace(go.Scatter(x=[stdev3End, stdev3End], y=[0, 0.2], mode='lines', name='EndThird'))
fig.show()

zScore = (sampleMean1-finalMean)/finalStDev

print(f'Sample 1 mean is {sampleMean1} and z-score is {zScore}')