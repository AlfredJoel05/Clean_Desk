import os,shutil
from datetime import datetime

year = datetime.today().strftime("%Y")
month = datetime.today().strftime("%m")
day = datetime.today().strftime("%d")
year_folder_exists = False
month_folder_exists = False

for file in os.listdir("C:/Users/arunk/Desktop"):
    source = os.path.abspath(os.path.join('C:/Users/arunk/Desktop',file))
    ext = os.path.splitext(file)[-1].lower()
    destination='D:/temp/test'

    if year_folder_exists == False:
        os.makedirs(destination + "/" + year + '/')
        year_folder_exists = os.path.abspath(os.path.join(destination,year))
        year_folder_exists = os.path.exists(year_folder_exists)

        if year_folder_exists == True:
            os.makedirs(destination + "/" + year + '/' + month + '/')
            month_folder_exists = os.path.abspath(os.path.join(year_folder_exists, month))
            month_folder_exists = os.path.exists(month_folder_exists)

            if month_folder_exists == True:
                final_destination = os.path.abspath(os.path.join(month_folder_exists , file))

                if ext == '.jpg':
                    shutil.move(source,final_destination)
                else:
                    print("files with new extions found")
            else:
                print("can't create month folder")
        else:
            print("can't create year folder")