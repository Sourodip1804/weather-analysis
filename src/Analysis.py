import mysql.connector as mc
from matplotlib import pyplot as plt

dataBase = mc.connect(host = "localhost" , user = "root" , passwd = "" , database = "weather_data")
c = dataBase.cursor()

c.execute("select precipitation , avg_temp , station_state from data")

temp = []
prec = []

rows = c.fetchall()

for row in rows:
    temp.append(row[1])
    prec.append(row[0])

plt.scatter(temp , prec , s=5 , alpha=0.7)
plt.xlabel('Temperature')
plt.ylabel('Precipitation')
plt.title('USA Weather Data Analysis')
plt.show()

c.close()
