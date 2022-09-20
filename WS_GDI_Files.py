import shutil
import os
import collections
import Index_Download_1
import Index_Download_2

primary_country_cod = ['DE','AR','AU','AT','BE','CA','CZ','CN','CY','CO','KR','HR','DK','EG','AE','ES','US','FI','FR','GR','IN','IE','IL','IT','JP','MA','MX','NO','NL','PL','PT','GB','RU','SE','CH','TN','TR']
file_source = 'C:\\Users\\user\\Downloads\\'
file_flight = 'C:\\Users\\user\\Downloads\\Vuelos'
file_accomm = 'C:\\Users\\user\\Downloads\\Alojamientos'
get_files = os.listdir(file_source)
flight_csv_full = [i for i in get_files if i.startswith('FLIGHT',32,47)]
accom_csv_full = [i for i in get_files if i.startswith('ACCOMMODATION',32,54)]


def extract_cod_country(list):
        if len(list) == 47:
            return list[28:-17]
        else:
            return list[28:-24]
        

def extract_cod_country_1(list):
        if len(list) == 51:
            return list[28:-21]
        else:
            return list[28:-28]


def download_status():
    flight_csv = [i for i in get_files if i.startswith('FLIGHT',32,47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION',32,54)]
    download_flight = [extract_cod_country(i) for i in flight_csv]
    download_accomm = [extract_cod_country(i) for i in accom_csv]
    download_file = [i for i in download_flight if i in download_accomm]
    download_missing = [i for i in primary_country_cod if i not in download_file]
    if (collections.Counter(download_file) == collections.Counter(primary_country_cod)):
        print('Download process 1 Ok')
        x = 1
    else:
        print('Failed process download 1')
        print('Downloaded countries: ' + str(download_file))
        print('Pending countries: ' + str(download_missing))
        x = 0
    return x


def download_status_2():
    flight_csv_1 = [i for i in get_files if i.startswith('FLIGHT__30_ (1)',32,47)]
    accom_csv_1 = [i for i in get_files if i.startswith('ACCOMMODATION__30_ (1)',32,54)]
    download_flight_1 = [extract_cod_country_1(i) for i in flight_csv_1]
    download_accomm_1 = [extract_cod_country_1(i) for i in accom_csv_1]
    download_file_1 = [i for i in download_flight_1 if i in download_accomm_1]
    download_missing_1 = [i for i in primary_country_cod if i not in download_file_1]
    if (collections.Counter(download_file_1) == collections.Counter(primary_country_cod)):
        print('Download process 2 Ok')
        x = 1
    else:
        print('Failed process download 2')
        print('Downloaded countries: ' + str(download_file_1))
        print('Pending countries: ' + str(download_missing_1))
        x = 0
    return x
        

def files_path():
    for i in flight_csv_full:  
        shutil.move(file_source + i, file_flight)
    for i in accom_csv_full:
        shutil.move(file_source + i, file_accomm)
    print('Files in path:' + str(file_flight) + ' and ' + str(file_accomm))


def run():
    if (download_status() == 0):
        Index_Download_1.run()
        y = False
    else: 
        y = False
    if (download_status_2() == 0):
        Index_Download_2.run()
        z = False
    else:
        z = False
    if ( (y != True) and (z != True) ):
        pass
        #files_path()       
    else:
        print('Failed process')


if __name__ == '__main__':    
    run()