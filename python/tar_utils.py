import os
import tarfile


def extractTarFile(tarFilename: str, path: str = os.getcwd(), force=False):
    extractedFilename = tarFilename.split(".")[0]  # remove .tar.gz
    tarFileRoot = path + "/" + tarFilename
    extractedFileRoot = path + "/" + extractedFilename
    if os.path.isdir(extractedFileRoot) and not force:
        # You may override by setting force=True.
        print(f'{extractedFilename} already present - Skipping extraction of {tarFilename}')
    elif tarfile.is_tarfile(tarFileRoot):
        print(f'Extracting data for {tarFilename}. This may take a while. Please wait.')
        try:
            tarFileObj = tarfile.open(tarFileRoot, "r")
            # sys.stdout.flush()
            tarFileObj.extractall(tarFileRoot)
            tarFileObj.close()
        except Exception as e:
            print(f'Unable to process data from {tarFilename}: {e}')
            raise
    else:
        print("[*] tarfile error")

def createTarFile(foldername: str, path: str = os.getcwd()):
    print(f"tar file: {foldername}")
    fileRoot = path + "/" + foldername
    try:
        tarFileObj = tarfile.open(fileRoot, "w")
        tarFileObj.add(foldername)
        tarFileObj.close()

    except Exception as e:
        print(f"unable to tar file: {foldername}: {e}")
        raise

def appendToTarFile(tarFilename: str, files: list, path: str = os.getcwd()):
    # files should be list of path like strings
    print(f"appending files to tarfile: {tarFilename}")
    tarFileRoot = path + "/" + tarFilename
    try:
        tarFileObj = tarfile.open(tarFileRoot, "a")
        for file in files:
            print(f"adding {file} to tar file")
            tarFileObj.add(file)
        tarFileObj.close()
    except Exception as e:
        print(f"unable to append to {tarFilename}: {e}")
        raise
