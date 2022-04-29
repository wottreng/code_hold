import os
import time
from pdf2image import convert_from_path
from os import listdir
from os.path import isfile, join
# import sys
start = time.time()

mypath = os.getcwd() # sys.argv[1]
outpath = os.getcwd()  # sys.argv[2]
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath, f))]

for n in range(0, len(onlyfiles)):
    # get number of pages in each document
    if ".pdf" in onlyfiles[n] and not "JPEG" in onlyfiles[n]:
        print(f"File Name: {onlyfiles[n]}")
        pages = convert_from_path(join(mypath, onlyfiles[n]), 500)
        # set image counter to 1
        image_counter = 1
        for page in pages:
            # Convert each page in the PDF file into .JPEG Image
            # image_name = f"page_{image_counter}.png"
            # Save every image
            #page.save(f"{outpath}/{onlyfiles[n]}.{image_name}", 'JPEG')
            page.save(f"{outpath}/{image_counter}.png", "png")
            image_counter += 1
print(f"Finished, time: {round(time.time()-start,2)} seconds")
