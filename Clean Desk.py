import os,shutil
from datetime import datetime

year=datetime.today().strftime('%Y')
month=datetime.today().strftime('%m')
day=datetime.today().strftime('%d')
year_folder_exists=False
month_folder_exists=False

def year_folder():
    os.makedirs(destination + '/' + year + '/')
    year_folder_path=os.path.abspath(os.path.join(destination, year))
    year_folder_exists=os.path.exists(year_folder_path) #True
    return year_folder_path,year_folder_exists

def month_folder():
    os.makedirs(destination + '/' + year + '/' + month + '/')
    month_folder_path=os.path.abspath(os.path.join(year_folder_path, month))
    month_folder_exists=os.path.exists(month_folder_path) #True
    return month_folder_path

def move(source,final_destination):
    shutil.move(source,final_destination)


if __name__ == "__main__":

    for file in os.listdir('C:/Users/Alfred Joel/Desktop'):
        source=os.path.abspath(os.path.join('C:/Users/Alfred Joel/Desktop', file))
        print(file)
        ext=os.path.splitext(file)[-1].lower()
        print(ext)
        destination='D:/Temp/Test/'
  
        if year_folder_exists == False:
            year_path=year_folder()
        elif year_folder_exists == True:
            month_path=month_folder()
            if month_folder_exists = False:

            elif month_folder_exists == True:
                
                if ext =='.jpg':
                    final_destination=os.path.abspath(os.path.join(month_folder_path, file))
                else:
                    print('Files with New Extensions Found')
            else:
                month_folder_exists=False
        else:
            year_folder_exists=False