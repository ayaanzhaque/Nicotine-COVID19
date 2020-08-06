import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#weatherData = pd.read_csv('weatherdataSOUTHKOREA.csv')
#casesData = pd.read_csv('CasesInfoSOUTHKOREA.csv')
casesData = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")

#plt.style.use('ggplot')

#ax = weatherData.plot()
#casesData.plot(ax=ax)
#plt.legend()
#plt.show()

indexNames = casesData[casesData['location'] != "South Korea"].index
casesData.drop(indexNames, inplace=True)

print(casesData)
