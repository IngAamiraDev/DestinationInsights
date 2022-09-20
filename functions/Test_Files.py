import shutil
import os
import glob
import collections

#Crea un directorio
#os.makedirs("C:/Users/user/Downloads/CSV GDI")

"""
print(len('Comparisons_From_2022-09-09_CY__FLIGHT__30_.csv'))
print(len('Comparisons_From_2022-09-09_CY__ACCOMMODATION__30_.csv'))
print(len('Comparisons_From_2022-09-16_DE__FLIGHT__30_ (1)'))
print(len('Comparisons_From_2022-09-16_AR__ACCOMMODATION__30_ (1)'))
"""

file_source = 'C:\\Users\\user\\Downloads\\'
file_flight = 'C:\\Users\\user\\Downloads\\Vuelos'
file_accomm = 'C:\\Users\\user\\Downloads\\Alojamientos'

primary_country_cod = ['DE','AR','AU','AT','BE','CA','CZ','CN','CY','CO','KR','HR','DK','EG','AE','ES','US','FI','FR','GR','IN','IE','IL','IT','JP','MA','MX','NO','NL','PL','PT','GB','RU','SE','CH','TN','TR']
primary_country_name = ['Germany','Argentina','Australia','Austria','Belgium','Canada','Czechia','China','Cyprus','Colombia','South Corea','Croatia','Denmark','Egypt','United Arab Emirates','Spain','United States','Finland','France','Greece','India','Ireland','Israel','Italy','Japan','Morocco','Mexico','Norway','Netherlands','Poland','Portugal','United Kingdom','Russia','Sweden','Switzerland','Tunisia','Turkey']


def extract_cod_country(list):
        if len(list) == 47:
            return list[28:-17]
        else:
            return list[28:-24]

"""(1)
def extract_cod_country(list):
        if len(list) == 51:
            return list[28:-21]
        else:
            return list[28:-28]
"""

get_files = os.listdir(file_source)
flight_csv_full = [i for i in get_files if i.startswith('FLIGHT',32,47)]
accom_csv_full = [i for i in get_files if i.startswith('ACCOMMODATION',32,54)]
flight_csv = [i for i in get_files if i.startswith('FLIGHT__30_.csv',32,47)]
accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION__30_.csv',32,54)]
flight_csv_1 = [i for i in get_files if i.startswith('FLIGHT__30_ (1)',32,47)]
accom_csv_1 = [i for i in get_files if i.startswith('ACCOMMODATION__30_ (1)',32,54)]
download_flight = [extract_cod_country(i) for i in flight_csv_1]
download_accomm = [extract_cod_country(i) for i in accom_csv_1]
download_file = [i for i in download_flight if i in download_accomm]
download_missing = [i for i in primary_country_cod if i not in download_file]



def len_country_missing():
    kick_off = len(primary_country_name) - len(download_missing)
    return kick_off


def delete_last_file():
    if len(accom_csv) > len(flight_csv):
        files_path = os.path.join(file_source, '*')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        os.remove(files[0])
    elif len(flight_csv) > len(accom_csv):
        files_path = os.path.join(file_source, '*')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        os.remove(files[0])
    else: 
        pass


def status():
    if (len_country_missing()%2 == 0):
        delete_last_file()
    download_status()


def download_status():
    print('Downloaded countries:' + str(download_file))
    print('Pending countries:' + str(download_missing))


def download_status():
    if (collections.Counter(download_file) == collections.Counter(primary_country_cod)):
        print('Download process Ok')
    else:
        print('Downloaded countries: ' + str(download_file))
        print('Pending countries: ' + str(download_missing))

status()

"""
def delete_last_file_2():
    if len(accom_csv) > len(flight_csv):
        files_path = os.path.join(file_source, '*')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        os.remove(files[0])
    elif len(flight_csv) > len(accom_csv):
        files_path = os.path.join(file_source, '*')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        os.remove(files[0])
    else: 
        pass
"""


"""
def move_files():
    for i in flight_csv:  
        shutil.move(file_source + i, file_flight)
    for i in accom_csv:
        shutil.move(file_source + i, file_accomm)
"""








