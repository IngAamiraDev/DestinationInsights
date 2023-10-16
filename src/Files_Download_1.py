import shutil
import os
import glob
import collections
import Index_Download_1

PRIMARY_COUNTRY_NAMES = ['Germany', 'Argentina', 'Australia', 'Austria', 'Belgium', 'Canada', 'Czechia', 'China', 'Cyprus', 'Colombia', 'South Corea', 'Croatia', 'Denmark', 'Egypt', 'United Arab Emirates', 'Spain', 'United States', 'Finland', 'France', 'Greece', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Morocco', 'Mexico', 'Norway', 'Netherlands', 'Poland', 'Portugal', 'United Kingdom', 'Russia', 'Sweden', 'Switzerland', 'Tunisia', 'Turkey']
PRIMARY_COUNTRY_CODES = ['DE', 'AR', 'AU', 'AT', 'BE', 'CA', 'CZ', 'CN', 'CY', 'CO', 'KR', 'HR', 'DK', 'EG', 'AE', 'ES', 'US', 'FI', 'FR', 'GR', 'IN', 'IE', 'IL', 'IT', 'JP', 'MA', 'MX', 'NO', 'NL', 'PL', 'PT', 'GB', 'RU', 'SE', 'CH', 'TN', 'TR']

source_directory = 'C:\\Users\\user\\Downloads\\'
flight_directory = 'C:\\Users\\user\\Downloads\\Vuelos'
accom_directory = 'C:\\Users\\user\\Downloads\\Alojamientos'


def extract_cod_country(filename):
    """
    Extracts the country code from the file name.

    Args:
        filename (str): File name.

    Returns:
        str: Extracted country code from the file name.
    """
    return filename[28:-17] if len(filename) == 47 else filename[28:-24]



def files_path():
    """
    Moves the downloaded files to the corresponding directories and displays the path of moved files.
    """
    get_files = os.listdir(source_directory)
    flight_csv = [i for i in get_files if i.startswith('FLIGHT', 32, 47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION', 32, 54)]
    for i in flight_csv:
        shutil.move(source_directory + i, flight_directory)
    for i in accom_csv:
        shutil.move(source_directory + i, accom_directory)
    print('Files in path: ' + str(flight_directory) + ' and ' + str(accom_directory))


def remove_wrong_files():
    """
    Removes incorrect or invalid files based on certain criteria from the download directory.
    """
    get_files = os.listdir(source_directory)
    all_wrong_csv = [i for i in get_files if i.startswith('ALL', 32, 47)]
    flight_csv = [i for i in get_files if i.startswith('FLIGHT', 32, 47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION', 32, 54)]
    flight_csv_1 = [i for i in get_files if i.startswith(
        'FLIGHT__30_ (', 32, 47)]
    accom_csv_1 = [i for i in get_files if i.startswith(
        'ACCOMMODATION__30_ (', 32, 54)]
    download_flight = [extract_cod_country(i) for i in flight_csv]
    download_accomm = [extract_cod_country(i) for i in accom_csv]
    download_file = [i for i in download_flight if i in download_accomm]
    download_missing = [
        i for i in PRIMARY_COUNTRY_CODES if i not in download_file]
    country_wrong = [i for i in get_files if i.startswith(
        tuple(download_missing), 28, 50)]
    if len(all_wrong_csv) > 0:
        for i in range(len(all_wrong_csv)):
            files_path = os.path.join(source_directory, all_wrong_csv[i])
            files = sorted(glob.iglob(files_path),
                           key=os.path.getctime, reverse=True)
            os.remove(files[0])
    if len(flight_csv_1) > 0:
        for i in range(len(flight_csv_1)):
            files_path = os.path.join(source_directory, flight_csv_1[i])
            files = sorted(glob.iglob(files_path),
                           key=os.path.getctime, reverse=True)
            os.remove(files[0])
    if len(accom_csv_1) > 0:
        for i in range(len(accom_csv_1)):
            files_path = os.path.join(source_directory, accom_csv_1[i])
            files = sorted(glob.iglob(files_path),
                           key=os.path.getctime, reverse=True)
            os.remove(files[0])
    if len(country_wrong) > 0:
        for i in range(len(country_wrong)):
            files_path = os.path.join(source_directory, country_wrong[i])
            files = sorted(glob.iglob(files_path),
                           key=os.path.getctime, reverse=True)
            os.remove(files[0])
    else:
        print('No wrong files to delete')


def download_status():
    """
    Checks the download status and displays messages based on whether the download was successful or not.

    Returns:
        int: 1 if download was successful, 0 if not.
    """    
    get_files = os.listdir(source_directory)
    flight_csv = [i for i in get_files if i.startswith('FLIGHT', 32, 47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION', 32, 54)]
    download_flight = [extract_cod_country(i) for i in flight_csv]
    download_accomm = [extract_cod_country(i) for i in accom_csv]
    download_file = [i for i in download_flight if i in download_accomm]
    download_missing = [
        i for i in PRIMARY_COUNTRY_CODES if i not in download_file]
    if (collections.Counter(download_file) == collections.Counter(PRIMARY_COUNTRY_CODES)):
        print('Download process 1 Ok')
        x = 1
    else:
        print('Failed process download 1')
        print('Downloaded countries: ' + str(download_file))
        print('Pending countries: ' + str(download_missing))
        x = 0
    return x


def delete_last_file():
    """
    Deletes the last downloaded file if there are more files of one type than the other.
    """    
    get_files = os.listdir(source_directory)
    flight_csv = [i for i in get_files if i.startswith('FLIGHT', 32, 47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION', 32, 54)]
    if len(accom_csv) > len(flight_csv):
        files_path = os.path.join(source_directory, '*')
        files = sorted(glob.iglob(files_path),
                       key=os.path.getctime, reverse=True)
        os.remove(files[0])
    elif len(flight_csv) > len(accom_csv):
        files_path = os.path.join(source_directory, '*')
        files = sorted(glob.iglob(files_path),
                       key=os.path.getctime, reverse=True)
        os.remove(files[0])
    else:
        pass


def len_country_missing():
    get_files = os.listdir(source_directory)
    flight_csv = [i for i in get_files if i.startswith('FLIGHT', 32, 47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION', 32, 54)]
    download_flight = [extract_cod_country(i) for i in flight_csv]
    download_accomm = [extract_cod_country(i) for i in accom_csv]
    download_file = [i for i in download_flight if i in download_accomm]
    download_missing = [
        i for i in PRIMARY_COUNTRY_CODES if i not in download_file]
    kick_off = len(PRIMARY_COUNTRY_NAMES) - len(download_missing)
    return kick_off


def index_primary_country_cod():
    """
    Gets the index of the first missing country in the primary country codes list.

    Returns:
        int: Index of the first missing country.
    """    
    get_files = os.listdir(source_directory)
    x = 0
    flight_csv = [i for i in get_files if i.startswith('FLIGHT', 32, 47)]
    accom_csv = [i for i in get_files if i.startswith('ACCOMMODATION', 32, 54)]
    download_flight = [extract_cod_country(i) for i in flight_csv]
    download_accomm = [extract_cod_country(i) for i in accom_csv]
    download_file = [i for i in download_flight if i in download_accomm]
    download_missing = [
        i for i in PRIMARY_COUNTRY_CODES if i not in download_file]
    index = [i for i, j in enumerate(
        PRIMARY_COUNTRY_CODES) if j in download_missing]
    if len(index) != 0:
        x = index[0]
    else:
        pass
    return x


def download_status_path():    
    """
    Checks the download status in specific directories and displays messages based on whether the download was successful or not.

    Returns:
        int: 1 if download was successful, 0 if not.
    """
    get_files_flight = os.listdir(flight_directory)
    get_files_accomm = os.listdir(accom_directory)
    flight_csv = [i for i in get_files_flight if i.startswith(
        'FLIGHT', 32, 47)]
    accom_csv = [i for i in get_files_accomm if i.startswith(
        'ACCOMMODATION', 32, 54)]
    download_flight = [extract_cod_country(i) for i in flight_csv]
    download_accomm = [extract_cod_country(i) for i in accom_csv]
    download_file = [i for i in download_flight if i in download_accomm]
    download_missing = [
        i for i in PRIMARY_COUNTRY_CODES if i not in download_file]
    if (collections.Counter(download_file) == collections.Counter(PRIMARY_COUNTRY_CODES)):
        print('Download process 1 Ok')
        x = 1
    else:
        print('Failed process download 1')
        print('Downloaded countries: ' + str(download_file))
        print('Pending countries: ' + str(download_missing))
        x = 0
    return x


def run():
    """
    Main function that executes necessary operations to check and manage downloaded files.
    """    
    remove_wrong_files()
    if (download_status() == 1):
        files_path()
    else:
        Index_Download_1.run()
        print('Download process 1 Ok')


if __name__ == '__main__':
    run()