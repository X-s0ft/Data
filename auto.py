import os

path = "G:\\new\Friday"
files = os.listdir(path)

for h, file in enumerate(files):

    nameFolders = str(files[h])
    filesFolders = os.listdir(f"{path}\\{nameFolders}")#bread coffee i td 

    for j, file in enumerate(filesFolders):

         nameFoldersBadOrGood = str(filesFolders[j])# good or bad 
         imagesFiles = os.listdir(f"{path}\\{nameFolders}\\{nameFoldersBadOrGood}")# imagesfiles

         for i, file in enumerate(imagesFiles):

                from PIL import Image
                check = False

                try:
                    image_path = f"{path}\\{nameFolders}\\{nameFoldersBadOrGood}\\{i}.jpg"
                    img = Image.open(image_path)     
                except FileNotFoundError: 

                    image_path = f"{path}\\{nameFolders}\\{nameFoldersBadOrGood}\\{i}.jpeg"
                    img = Image.open(image_path)
                    check = True
                fixed_width = 300    
                width_percent = (fixed_width / float(img.size[0]))
                height_size = int(300)
                new_image = img.resize((fixed_width, height_size)).convert('L')
            
                if(check):
                    new_image.save(f"{path}\\{nameFolders}\\{nameFoldersBadOrGood}\\{i}.jpeg")
                else:
                    new_image.save(f"{path}\\{nameFolders}\\{nameFoldersBadOrGood}\\{i}.jpg")
