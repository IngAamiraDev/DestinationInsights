import shutil
import os
import collections
import Test_Index_Download_2

primary_country_cod = ['DE','AR','AU','AT','BE','CA','CZ','CN','CY','CO','KR','HR','DK','EG','AE','ES','US','FI','FR','GR','IN','IE','IL','IT','JP','MA','MX','NO','NL','PL','PT','GB','RU','SE','CH','TN','TR']
file_source = 'C:\\Users\\user\\Downloads\\'
file_flight = 'C:\\Users\\user\\Downloads\\Vuelos'
file_accomm = 'C:\\Users\\user\\Downloads\\Alojamientos'


def extract_cod_country(list):
        if len(list) == 47:
            return list[28:-17]
        else:
            return list[28:-24]
        

def extract_file(list):
    return list[0:-4]


def rename_file_download():
    get_files = os.listdir(file_source)
    flight_csv = [i for i in get_files if i.startswith('FLIGHT', 32, 47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION', 32, 54)]
    download_file = flight_csv + accom_csv
    rename_new_file = [extract_file(i) for i in download_file]
    for i in range(len(rename_new_file)):
        rename_new_file[i] = (rename_new_file[i] + ' (1).csv')
        source = file_source + download_file[i]
        destination = file_source + rename_new_file[i]
        os.rename(source,destination)
    return print('Process rename file download process 2 Ok')


def files_path():
    get_files = os.listdir(file_source)
    flight_csv = [i for i in get_files if i.startswith('FLIGHT',32,47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION',32,54)]
    for i in flight_csv:  
        shutil.move(file_source + i, file_flight)
    for i in accom_csv:
        shutil.move(file_source + i, file_accomm)
    print('Files in path: ' + str(file_flight) + ' and ' + str(file_accomm))


def download_status():
    get_files = os.listdir(file_source)
    flight_csv = [i for i in get_files if i.startswith('FLIGHT',32,47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION',32,54)]
    download_flight = [extract_cod_country(i) for i in flight_csv]
    download_accomm = [extract_cod_country(i) for i in accom_csv]
    download_file = [i for i in download_flight if i in download_accomm]
    download_missing = [i for i in primary_country_cod if i not in download_file]
    if (collections.Counter(download_file) == collections.Counter(primary_country_cod)):
        print('Download process 2 Ok')
        x = 1
        rename_file_download()
        files_path()
    else:
        print('Failed process download 2')
        print('Downloaded countries: ' + str(download_file))
        print('Pending countries: ' + str(download_missing))
        x = 0
    return x
 

def run():
    if (download_status() == 0):
        Test_Index_Download_2.run()
    print('Download process 2 Ok')


if __name__ == '__main__':
    run()