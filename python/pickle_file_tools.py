#!/usr/bin/python3
import os
import pickle


class pickleFileTools:

    def __init__(self):
        pass

    def pickleFile(self, data: any, filename: str, path: str = os.getcwd(), force: bool = False):
        pickleFilename = filename + '.pickle'
        pickelFileRoot = path + "/" + pickleFilename
        # print(pickelFileRoot)
        if os.path.exists(pickelFileRoot) and not force:
            print("pickle file exists, skipping")
        else:
            # print(f'Pickling {filename}')
            try:
                with open(pickelFileRoot, 'wb') as f:
                    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
                    print(f'file is pickled: {pickleFilename}')
                    statinfo = os.stat(pickelFileRoot)
                    print('Compressed pickle size:', statinfo.st_size)
            except Exception as e:
                print('Unable to save data to', pickelFileRoot, ':', e)
                raise

    def returnPickleFileData(self, filename: str, path: str = os.getcwd()):
        pickleFilename = filename + '.pickle'
        pickelFileRoot = path + "/" + pickleFilename
        print(f'return data from: {pickleFilename}')
        try:
            with open(pickelFileRoot, 'rb') as f:
                fileData = pickle.load(f)
            return fileData
        except Exception as e:
            print('Unable to process data from', filename, ':', e)
            return None
        


if __name__ == '__main__':
    print(f"cur dir: {os.getcwd()}")
    fakeData = {"a": 1, "b": 2}
    c = pickleFileTools()
    c.pickleFile(fakeData, "testPickle")
    data = c.returnPickleFileData("testPickle.pickle")
    print(data)
    print(type(data))
