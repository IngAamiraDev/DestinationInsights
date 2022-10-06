import Download_1
import Download_2
import Files_Download_1
import Files_Download_2


def run():
    if (Files_Download_1.download_status_path() == 0):
        Download_1.run()
        Files_Download_1.run()
    else:
        pass
    if (Files_Download_2.download_status_path() == 0):
        Download_2.run()
        Files_Download_2.run()
    else:
        pass


if __name__ == '__main__':
    run()
