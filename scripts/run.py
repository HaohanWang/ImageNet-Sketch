from google_images_download import google_images_download
import os, errno
import time


def silent_remove_of_file(file):
    try:
        os.remove(file)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise e
        return False
    return True


def test_download_images_to_default_location():
    start_time = time.time()
    argumnets = {
        "keywords": "Polar bears",
        "limit": 5,
        "print_urls": False
    }
    try:
        temp = argumnets['output_folder']
    except KeyError:
        pass
    else:
        assert False, "This test checks download to default location yet an output folder was provided"

    output_folder_path = os.path.join(os.path.realpath('.'), 'downloads', '{}'.format(argumnets['keywords']))
    if os.path.exists(output_folder_path):
        start_amount_of_files_in_output_folder = len([name for name in os.listdir(output_folder_path) if os.path.isfile(os.path.join(output_folder_path, name)) and os.path.getctime(os.path.join(output_folder_path, name)) < start_time])
    else:
        start_amount_of_files_in_output_folder = 0

    response = google_images_download.googleimagesdownload()
    response.download(argumnets)
    files_modified_after_test_started = [name for name in os.listdir(output_folder_path) if os.path.isfile(os.path.join(output_folder_path, name)) and os.path.getmtime(os.path.join(output_folder_path, name)) > start_time]
    end_amount_of_files_in_output_folder = len(files_modified_after_test_started)
    print("Files downloaded by test {__name__}:")
    for file in files_modified_after_test_started:
        print(os.path.join(output_folder_path, file))


    # assert end_amount_of_files_in_output_folder - start_amount_of_files_in_output_folder == argumnets['limit']
    assert end_amount_of_files_in_output_folder == argumnets['limit']

    print("Cleaning up all files downloaded by test {__name__}...")
    for file in files_modified_after_test_started:
        if silent_remove_of_file(os.path.join(output_folder_path, file)):
            print("Deleted {os.path.join(output_folder_path, file)}")
        else:
            print("Failed to delete {os.path.join(output_folder_path, file)}")

def downloadASetImage(keyWord, folderName):
    start_time = time.time()
    output_folder_path = os.path.join(os.path.realpath('.'), folderName)

    print output_folder_path

    argumnets = {
        "keywords": keyWord,
        "limit": 100,
        "print_urls": False,
        # "output_folder": output_folder_path,
        "color_type": "black-and-white",
    }

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    if os.path.exists(output_folder_path):
        start_amount_of_files_in_output_folder = len([name for name in os.listdir(output_folder_path) if os.path.isfile(os.path.join(output_folder_path, name)) and os.path.getctime(os.path.join(output_folder_path, name)) < start_time])
    else:
        start_amount_of_files_in_output_folder = 0

    response = google_images_download.googleimagesdownload()
    response.download(argumnets)
    files_modified_after_test_started = [name for name in os.listdir(output_folder_path) if
                                         os.path.isfile(os.path.join(output_folder_path, name)) and os.path.getmtime(
                                             os.path.join(output_folder_path, name)) > start_time]
    end_amount_of_files_in_output_folder = len(files_modified_after_test_started)
    print("Files downloaded by test {__name__}:")
    for file in files_modified_after_test_started:
        print(os.path.join(output_folder_path, file))



def runDownloadImages():
    text = [line.strip() for line in open('../data/folder2class.txt')]
    c = 0
    for line in text:
        c += 1
        print '---------------'
        print 'We are working on class', c
        if c <= 105:
            continue
        folderName, className = line.split()
        folderName = '../results/' + folderName
        keyWords = 'sketch of ' + ' '.join(className.split('_'))
        print keyWords
        downloadASetImage(keyWord=keyWords, folderName=folderName)

if __name__ == '__main__':
    runDownloadImages()