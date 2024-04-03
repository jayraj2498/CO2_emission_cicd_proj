import sys 
import os 
import pandas as pd 
from src.exception import CustomException 
from src.utils import load_object


class predictpipeline : 
    def __init__(self):
        pass 
    
    def predict(self,features):
        try:
            
            # preprocessor_path=os.path.join('artifacts','preprocessor.pkl')  do that 
            # model_path=os.path.join('artifacts','model.pkl')
            
            model_path=os.path.join("E:\\co2_emssion\\artifacts\\model.pkl")
            preprocessor_path=os.path.join('E:\\co2_emssion\\artifacts\\proprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
    
class CustomData :             # the class uis responsible for mapping all the input we are giving in html to backend with particular val  
     
    def __init__(self, 
        YEAR: int,
        MAKE: str,
        ENGINE_SIZE: float,
        CYLINDERS: float,
        FUEL: str,
        FUEL_CONSUMPTION: float,
        HWY_L_PER_100KM: float,
        COMB_L_PER_100KM: float,
        COMB_MPG: float,
        BROAD_VEHICLE_CLASS: str,
        TRANSMISSION_GROUP: str):
        
        self.YEAR = YEAR
        self.MAKE = MAKE
        self.ENGINE_SIZE = ENGINE_SIZE
        self.CYLINDERS = CYLINDERS
        self.FUEL = FUEL
        self.FUEL_CONSUMPTION = FUEL_CONSUMPTION
        self.HWY_L_PER_100KM = HWY_L_PER_100KM
        self.COMB_L_PER_100KM = COMB_L_PER_100KM
        self.COMB_MPG = COMB_MPG
        self.BROAD_VEHICLE_CLASS = BROAD_VEHICLE_CLASS
        self.TRANSMISSION_GROUP = TRANSMISSION_GROUP
        
        
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "YEAR": [self.YEAR],
                "MAKE": [self.MAKE],
                "ENGINE_SIZE": [self.ENGINE_SIZE],
                "CYLINDERS": [self.CYLINDERS],
                "FUEL": [self.FUEL],
                "FUEL_CONSUMPTION": [self.FUEL_CONSUMPTION],
                "HWY_L_PER_100KM": [self.HWY_L_PER_100KM],
                "COMB_L_PER_100KM": [self.COMB_L_PER_100KM],
                "COMB_MPG": [self.COMB_MPG],
                "BROAD_VEHICLE_CLASS": [self.BROAD_VEHICLE_CLASS],
                "TRANSMISSION_GROUP": [self.TRANSMISSION_GROUP]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)
        
        
        
        
# these funct return input in the form of dataframe 
# inshort from our  web application  whatever input is comming same input we are get mapp with the our abouve particaular val 