# part seperated by the lines is 1 step

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

symptomsOnlyArrhythmia = symptoms.loc[(symptoms["Condition"] == "Cardiac arrhythmia")]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

groupedByState = symptoms.groupby('State') # without Arrhythmia states and deaths
setOfStates = set(symptoms["State"])
lst = list(setOfStates)
lst2 = []
for state in setOfStates:
    conditionGroup = groupedByState.get_group(state)
    lst2.append(conditionGroup["Number of COVID-19 Deaths"].sum())

groupedByStateArrhythmia = symptomsOnlyArrhythmia.groupby('State') # with Arrhythmia states and deaths
setOfStatesArrhythmia = set(symptomsOnlyArrhythmia["State"])
lstArrhythmia = list(setOfStatesArrhythmia)
lst2Arrhythmia = []
for stateArrhythmia in setOfStatesArrhythmia:
    conditionGroupArrhythmia = groupedByStateArrhythmia.get_group(stateArrhythmia)
    lst2Arrhythmia.append(conditionGroupArrhythmia["Number of COVID-19 Deaths"].sum())

dfOfStatesAndTotalDeaths = pd.DataFrame(list(zip(lst, lst2)), columns=['state', 'total_COVID-19_deaths']) # without Arrhythmia states and deaths df
print(dfOfStatesAndTotalDeaths)
print(dfOfStatesAndTotalDeaths.shape)

dfOfStatesAndTotalDeathsArrhythmia = pd.DataFrame(list(zip(lstArrhythmia, lst2Arrhythmia)), columns=['state', 'total_COVID-19_deaths']) # with Arrhythmia states and deaths df
print(dfOfStatesAndTotalDeathsArrhythmia)
print(dfOfStatesAndTotalDeathsArrhythmia.shape)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

sns.catplot(x="state", y="total_COVID-19_deaths", kind="bar", data=dfOfStatesAndTotalDeaths) # total
plt.xticks(rotation=-90)
sns.set(font_scale=0.7)
plt.title("Total COVID-19 Deaths by State")
plt.show()

sns.catplot(x="state", y="total_COVID-19_deaths", kind="bar", data=dfOfStatesAndTotalDeathsArrhythmia) # just Arrhythmia
plt.xticks(rotation=-90)
sns.set(font_scale=0.7)
plt.title("COVID-19 Deaths by State for Total Age Groups With Arrhythmia")
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

