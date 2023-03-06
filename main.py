# Main program

# We want to start by loading the data from the fastf1 api 

# Virtual environment test_env to install libraries
from matplotlib import pyplot as plt 
import pandas as pd 
from timple.timedelta import strftimedelta 
import fastf1 
import fastf1.plotting 
import sqlite3 

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS laps(race text, driver text, lap_time real)')

cursor.execute('INSERT INTO laps VALUES(?, ?, 0)', (race, driver))

connection.commit()
connection.close()

fastf1.Cache.enable_cache('/Users/jamie/Desktop/Uni/Year3/Semester2/FormulaOneRacewatch')

#session = fastf1.get_session(2019, 'Monza', 'Q')
#session.load()
#fast_leclerc = session.laps.pick_driver('LEC').pick_fastest()
#lec_car_data = fast_leclerc.get_car_data()
#t = lec_car_data['Time']
#vCar = lec_car_data['Speed']

#fig, ax = plt.subplots()
#ax.plot(t, vCar, label='Fast')
#ax.set_xlabel('Time')
#ax.set_ylabel('Speed [Km/h]')
#ax.set_title('Leclerc')
#ax.legend()
#plt.show()

session = fastf1.get_session(2022, 1, 'Q')
session.load()

drivers = pd.unique(session.laps['Driver'])
print(drivers)


