from PIL import Image
import os

def merge_images():
    """
    Merge all images, of type set below, into one long image
    images are stacked on top of each other
    """
    imgType = ".png"
    files = os.listdir(os.getcwd())
    imageNames = []
    for f in files:
        if imgType in f:
            imageNames.append(f)
    imageNames.sort()
    print("images found: ")
    print(imageNames)
    # create new global variable for each image and open image
    x = 0
    for img in imageNames:
        path = f"{os.getcwd()}/{img}"
        globals()[f"name{x}"] = Image.open(path)
        x += 1
    # get height and widths of each image for final image size calculation
    allWidths = []
    totalHeight = 0
    for i in range(x):
        (width1, height1) = globals()[f"name{i}"].size
        allWidths.append(width1)
        if i < x-1:
            totalHeight += height1

    result_width = max(allWidths)
    # create new long image
    result = Image.new('RGB', (result_width, totalHeight))
    # paste each image into the new image
    currentHeight = 0
    for x in range(x):
        result.paste(im=globals()[f"name{x}"], box=(0, currentHeight))  # width, height
        currentHeight += allWidths[x]

    result.save(f"{os.getcwd()}/mergedImage.png", "png")

merge_images()

