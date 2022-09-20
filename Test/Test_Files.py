import shutil
import os
import collections
from xml.dom.minidom import Element

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


def index_primary_country_cod():
    flight_csv = [i for i in get_files if i.startswith('FLIGHT',32,47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION',32,54)]
    download_flight = [extract_cod_country(i) for i in flight_csv]
    download_accomm = [extract_cod_country(i) for i in accom_csv]
    download_file = [i for i in download_flight if i in download_accomm]
    download_missing = [i for i in primary_country_cod if i not in download_file]
    index = [i for i, j in enumerate(primary_country_cod) if j in download_missing]
    return print(index)
        

def run():
    index_primary_country_cod()


if __name__ == '__main__':    
    run()