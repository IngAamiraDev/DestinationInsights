import os

#print(len('Comparisons_From_2022-09-09_CY__FLIGHT__30_.csv')) #->47
#print(len('Comparisons_From_2022-09-09_CY__ACCOMMODATION__30_.csv')) #->54

cod_contry = ['DE','AR','AU','AT','BE','CA','CZ','CN','CY','CO','KR','HR','DK','EG','AE','ES','US','FI','FR','GR','IN','IE','IL','IT','JP','MA','MX','NO','NL','PL','PT','GB','RU','SE','CH','TN','TR']

file_source = 'C:\\Users\\user\\Downloads\\'
file_flight = 'C:\\Users\\user\\Downloads\\Vuelos'
file_accomm = 'C:\\Users\\user\\Downloads\\Alojamientos'

get_files = os.listdir(file_source)

flight_csv = [i for i in get_files if i.startswith('FLIGHT',32,47)]
accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION',32,54)]


def extract_cod_country(list):
        if len(list) == 47:
            return list[28:-17]
        else:
            return list[28:-24]


def cod_country_flight():
    print('Flight')
    download_flight = [extract_cod_country(i) for i in flight_csv]
    return print(download_flight)


def cod_country_accomm():
    print('Accomm')
    download_accomm = [extract_cod_country(i) for i in accom_csv]
    return print(download_accomm)


download_flight = [extract_cod_country(i) for i in flight_csv]
print(download_flight)

missing_country = [i for i in cod_contry if i not in download_flight]
print(missing_country)
