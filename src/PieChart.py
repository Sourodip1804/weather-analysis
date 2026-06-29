import mysql.connector as mc
from matplotlib import pyplot as plt
import random

dataBase = mc.connect(host = "localhost" , user = "root" , passwd = "" , database = "weather_data")
c = dataBase.cursor()

c.execute("select max_temp , min_temp , station_state from data group by station_state")

rows = c.fetchall()
states = []
M_temp = []
m_temp = []

for max_temp , min_temp , state in rows:
    if max_temp >= 0 or min_temp >= 0:
        states.append(state)
        M_temp.append(max_temp)
        m_temp.append(min_temp)

r_M_temp = random.sample(M_temp , 10)
r_m_temp = random.sample(m_temp , 10)
r_states = random.sample(states , 10)

fig , axs = plt.subplots(1 , 2 , figsize =(12,6))
plt.subplots_adjust(wspace=0.5)

axs[0].pie(r_M_temp , labels = r_states , autopct = '%1.1f%%' , startangle=90 , shadow = True)
axs[0].set_title('Maximum Temperature')

axs[1].pie(r_m_temp , labels = r_states , autopct = '%1.1f%%' , startangle=90 , shadow = True)
axs[1].set_title('Minimum Temperature')

plt.show()

c.close()
