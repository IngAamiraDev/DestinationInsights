import shutil
import os

#Crea un directorio
#os.makedirs("C:/Users/user/Downloads/CSV GDI")

#print(len('Comparisons_From_2022-09-09_CY__FLIGHT__30_.csv'))
#print(len('Comparisons_From_2022-09-09_CY__ACCOMMODATION__30_.csv'))

file_source = 'C:\\Users\\user\\Downloads\\'
file_flight = 'C:\\Users\\user\\Downloads\\Vuelos'
file_accomm = 'C:\\Users\\user\\Downloads\\Alojamientos'

get_files = os.listdir(file_source)

flight_csv = [i for i in get_files if i.startswith('FLIGHT',32,47)]
accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION',32,54)]

print(flight_csv)

for i in flight_csv:  
    shutil.move(file_source + i, file_flight)

for i in accom_csv:
    shutil.move(file_source + i, file_accomm)





