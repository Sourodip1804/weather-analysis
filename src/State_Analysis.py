import mysql.connector as mc
from matplotlib import pyplot as plt

dataBase = mc.connect(host = "localhost" , user = "root" , passwd = "" , database = "weather_data")
c = dataBase.cursor()

c.execute("select precipitation , avg_temp , station_state , max_temp from data")

rows = c.fetchall()

t_alaska = []
p_alaska = []
t_california = []
p_california = []
t_texas = []
p_texas = []

for prec , temp , state in rows:
    if state == "Alaska":
        t_alaska.append(temp)
        p_alaska.append(prec)
    elif state == "California":
        t_california.append(temp)
        p_california.append(prec)
    elif state == "Texas":
        t_texas.append(temp)
        p_texas.append(prec)

plt.figure(figsize=(10,6))
plt.scatter(t_alaska , p_alaska , s=5 , alpha=0.5 , label = 'Alaska' , color = 'red')
plt.scatter(t_california , p_california , s=5 , alpha=0.6 , label = 'California' , color = 'black')
plt.scatter(t_texas , p_texas , s=5 , alpha=0.7 , label = 'Texas' , color = 'green')
plt.xlabel('Temperature')
plt.ylabel('Precipitation')
plt.title('Weather Data Analysis of USA')

plt.legend()
plt.show()

c.close()
