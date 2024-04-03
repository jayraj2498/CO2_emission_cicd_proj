# we will take data from mysql --> train_tesy_split -->  train_set,test_set


import os 
import sys
sys.path.append('E:\\END_TO_END_Deployed\\mlproject\\src')

# python -m src.components.data_ingestion    # plz use these line when error raise 


from src.exception import CustomException 
from src.logger import logging
import pandas as pd

from src.utils import read_sql_data    # for read_sql_data 

from sklearn.model_selection import train_test_split
from dataclasses import dataclass   

from src.components.data_transformation  import DataTransformationConfig 
from src.components.data_transformation  import DataTransformation 

from src.components.model_trainer import ModelTrainerConfig 
from src.components.model_trainer import ModelTrainer  



@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # df=pd.read_csv('E:\\zomato_project\\notebook\\data\\Realzomatodata.csv')
            # logging.info('Read the dataset as dataframe') 
            
            df=read_sql_data()
            logging.info('Read the dataset from mysql database completed ')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
# if __name__=="__main__":
#     obj=DataIngestion()
#     train_data ,test_data =obj.initiate_data_ingestion() 
    
#     data_transformation=DataTransformation() 
#     train_arr ,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)  # we are giving data 

#     modeltrainer=ModelTrainer()
#     print(modeltrainer.initiate_model_trainer(train_arr,test_arr))






# if these error is raise 
# Traceback (most recent call last):
#   File "E:\END_TO_END_Deployed\mlproject\src\components\data_ingestion.py", line 6, in <module>
#     from src.exception import CustomException 
# ModuleNotFoundError: No module named 'src'
# (E:\END_TO_END_Deployed\mlproject\venv) PS E:\END_TO_END_Deployed\mlproject> 

# python -m src.components.data_ingestion    # <-- plz use these line in terminal when error raise(dont use .py) 