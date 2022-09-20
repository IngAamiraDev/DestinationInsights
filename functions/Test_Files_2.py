import os


file_source = 'C:\\Users\\user\\Downloads\\'
primary_country_cod = ['DE','AR','AU','AT','BE','CA','CZ','CN','CY','CO','KR','HR','DK','EG','AE','ES','US','FI','FR','GR','IN','IE','IL','IT','JP','MA','MX','NO','NL','PL','PT','GB','RU','SE','CH','TN','TR']

string_1 = 'Comparisons_From_2022-09-20_AE__FLIGHT__30_ (1).csv'
string_2 = 'Comparisons_From_2022-09-20_AE__ACCOMMODATION__30_ (1).csv'


def extract_cod_country(list):
        if len(list) == 51:
            return list[28:-21]
        else:
            return list[28:-28]


get_files = os.listdir(file_source)
flight_csv_1 = [i for i in get_files if i.startswith('FLIGHT__30_ (1)',32,47)]
accom_csv_1 = [i for i in get_files if i.startswith('ACCOMMODATION__30_ (1)',32,54)]
download_flight = [extract_cod_country(i) for i in flight_csv_1]
download_accomm = [extract_cod_country(i) for i in accom_csv_1]
download_file = [i for i in download_flight if i in download_accomm]
download_missing = [i for i in primary_country_cod if i not in download_file]

print(download_file)
print(download_missing)

