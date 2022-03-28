import os
from PIL import Image

#You can copy the following lines (6-18) into the notebook or run this file as a script :) 

image_folder =  "p:\\workspaces\\nbl-communicativebrain\\working_data\\Noor\\teaching\\IMPRS_Python\\session2a-image-master\\raw" #Make sure this folder corresponds to your own folder structure!
img_list = os.listdir(img_folder)
print(img_list)

new_folder =  "p:\\workspaces\\nbl-communicativebrain\\working_data\\Noor\\teaching\\IMPRS_Python\\session2a-image-master\\the_new_folder" #Make sure this folder corresponds to your own folder structure!
#os.mkdir(new_folder)

for image_to_copy in img_list:
    print(image_to_copy)
    img_path = os.path.join(img_folder, image_to_copy)
    img_open = Image.open(img_path)
    filename, extension = os.path.splitext(image_to_copy)
    img_open.save(os.path.join(new_folder, filename + ".png"), "PNG")


#OR IF YOU ONLY WANT TO COPY THE JPG FILES AND IGNORE THE PNG FILES (see line 31 below): 

image_folder =  "p:\\workspaces\\nbl-communicativebrain\\working_data\\Noor\\teaching\\IMPRS_Python\\session2a-image-master\\raw" #Make sure this folder corresponds to your own folder structure!
img_list = os.listdir(img_folder)
print(img_list)

new_folder =  "p:\\workspaces\\nbl-communicativebrain\\working_data\\Noor\\teaching\\IMPRS_Python\\session2a-image-master\\the_new_folder2" #Make sure this folder corresponds to your own folder structure!
os.mkdir(new_folder)

for image_to_copy in img_list:
    if image_to_copy.endswith(".jpg"):
        img_path = os.path.join(img_folder, image_to_copy)
        img_open = Image.open(img_path)
        filename, extension = os.path.splitext(image_to_copy)
        img_open.save(os.path.join(new_folder, filename + ".png"), "PNG")
