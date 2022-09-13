import os

#print(len('Comparisons_From_2022-09-09_CY__FLIGHT__30_.csv')) #->47
#print(len('Comparisons_From_2022-09-09_CY__ACCOMMODATION__30_.csv')) #->54

cod_contry = ['DE','AR','AU','AT','BE','CA','CZ','CN','CY','CO','KR','HR','DK','EG','AE','ES','US','FI','FR','GR','IN','IE','IL','IT','JP','MA','MX','NO','NL','PL','PT','GB','RU','SE','CH','TN','TR']
primary_country_id = ['select_option_637','select_option_565','select_option_568','select_option_569','select_option_575','select_option_593','select_option_612','select_option_600','select_option_611','select_option_603','select_option_761','select_option_608','select_option_614','select_option_619','select_option_790','select_option_763','select_option_792','select_option_630','select_option_631','select_option_640','select_option_656','select_option_660','select_option_662','select_option_663','select_option_665','select_option_701','select_option_695','select_option_718','select_option_707','select_option_729','select_option_730','select_option_791','select_option_736','select_option_768','select_option_769','select_option_782','select_option_783']

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


print('download_flight')
download_flight = [extract_cod_country(i) for i in flight_csv]
print(download_flight)


print('missing_country')
missing_country = [i for i in cod_contry if i not in download_flight]
print(missing_country)


print('cod_dict')
cod_dict = {
    "cod_country": cod_contry, "id_html": primary_country_id
}
print(cod_dict)

