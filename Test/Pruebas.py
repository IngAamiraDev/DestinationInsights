import os

#'Comparisons_From_2022-09-24_DE__FLIGHT__30_.csv'

file_source = 'C:\\Users\\user\\Downloads\\'


def extract_file(list):
    return list[0:-4]


def rename_file():
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
    return print('Process rename file Ok')
        
rename_file()

#new_file = [rename_new_file(i) for i in new_file]



#new_file = [extract_file(i) for i in accom_csv]

