# Bring in mss
from mss import mss
import os
import glob

Escape = True

class DataCollectionBase():
    
    def __init__(self, left, top, width, height, datalocation): 
        # Setup the game area 
        self.__game_area = {"left": left, "top": top, "width": width, "height": height}
        self.capture = mss()
        self.current_keys = []
        self.__datalocation = datalocation
        self.__folderpath = f"C:/Users/ayman/Documents/GitHub/COURSEWORK/{self.__datalocation}"
        self.check_folder()
    
    def check_folder(self):
        exists = os.path.exists(self.__folderpath)
        if exists == True:
            print(f"Data location, {self.__folderpath},  already exits")
            print(f"Do you want to reset data location or carry on creating training data")
            while True:
                reset = input("Y/N ")
                if reset == "Y":
                    print("You have decided to clear the folder")
                    files = glob.glob(os.path.join(self.__folderpath, '*'))
                    for f in files:
                        os.remove(f)
                    break
                elif reset == "N":
                    print("You have decided not to clear the folder")
                    break
                else:
                    print("Please enter Y or N")
        elif exists == False:
            print(f"Data location does not exist")
            print(f"Creating folder for the data...")
            os.mkdir(self.__folderpath)
            print(f"{self.__folderpath} has been created!")

            
            



    def collect_gameplay(self):
        pass
        #change for each 

dc = DataCollectionBase(100, 425, 662, 470, "testdata1")