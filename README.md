## End to End MAchine Learning Project 

# CO2 Emission Prediction Project

This project aims to predict CO2 emissions for vehicles using machine learning models and provides a web interface for users to make predictions.

## Overview

The project consists of the following components:

1. **Data Ingestion**: Data is collected from various sources using the `data_ingestion.py` script and stored locally.

2. **Data Transformation**: The collected data undergoes preprocessing and feature engineering using the `data_transformation.py` script.

3. **Model Training**: Machine learning models are trained on the preprocessed data using the `model_training.py` script. Model evaluation and selection are performed to identify the best-performing model.

4. **Pipeline Process**: The entire process is organized into a pipeline using the following modules:
   - `logger.py`: Contains logging configurations for the project.
   - `exception.py`: Handles exceptions and errors in the pipeline.
   - `data_ingestion.py`: Handles data collection and storage.
   - `data_transformation.py`: Preprocesses and transforms the data.
   - `model_training.py`: Trains machine learning models.
   - `pipeline/training_pipeline.py`: Defines the training pipeline.
   - `pipeline/prediction_pipeline.py`: Defines the prediction pipeline.

5. **Flask App**: A Flask web application (`app.py`) is developed to provide a user interface for predicting CO2 emissions. Users can input vehicle details through a form, and the application provides the predicted CO2 emissions value.

6. **Model Deployment**: Trained models are serialized using pickle and deployed within the Flask application.

7. **Docker Integration**: Docker is utilized for containerization, allowing for easy deployment and portability of the application.

8. **CI/CD Integration on AWS**: Continuous Integration/Continuous Deployment (CI/CD) pipelines are set up on AWS to automate the deployment process. The application is automatically built, tested, and deployed to the cloud environment whenever changes are made to the codebase.

9. **Version Control**: Data version control is implemented using DVC (Data Version Control), allowing for efficient management and tracking of datasets.

10. **Experiment Tracking**: MLflow is used for experiment tracking, enabling easy comparison of model performance and parameters.

11. **Collaboration and Sharing**: DAGsHub is utilized for collaboration, code sharing, and version control of the project.

## Installation

To run the project locally, follow the installation steps mentioned in the respective scripts and modules. Ensure that all dependencies are installed and configured correctly.

## Usage

1. Run the necessary scripts/modules to preprocess the data and train the machine learning models.
2. Start the Flask application by running `python app.py`.
3. Access the web interface in your browser and input vehicle details to predict CO2 emissions.


#### we will track our data by using DVC :- data version control 
- we will track our data store in our artifacts folder 
- usually we have to big data so we can put them in CI or it is not posible we store our bigdata in our repository  
- we have to control that data so we track our file (artifact file ) by using DVC 
- as git has command DVC also have the command 
    -- to initiallize dvc --> dvc init  
       you get .dvc folder and .devcignore file -> in that you get more folder we will  commit it our main git tht'y 
- inside .dvc folder our data tracking happend  
- .devcignore inside 

- first we have to untrack artifacts folder file for next to track it y dvc 
- dvc add artifacts/data.csv  we run these 
- we get file 2 file in artifacts folder data.csv.dvc  , .gitignore 
- file looks like 
    outs:
- md5: 6206fc08bd4965cee784139be0b4640d
  size: 318565
  hash: md5
  path: data.csv

- we send  data.csv.dvc  to git  to track not our full data.csv file 
- we track data by-- >  dvc file    , data configration file --> github 
- incase if you have big data you put it into cloud that configraion info track by git 




#### Ml Flow - experiment tracking ( integrate the code ) 

- if run our model various time we should know everytime our model :
  - accuracy , r2score  , evalution matrix : all these thing we track by using MLflows 

Ml flows is the platform for entire ML lifecycle 



#### Dagshub - : public repository 
- till now we putting our code in the github 
- now in dagshub we will connect that repository  and track that specific repository 
-  and see    


- we have to setup all thing in the environment variable all the commmand in git bash 
'''
export MLFLOW_TRACKING_URI=https://dagshub.com/jayraj2498/CO2_emission_cicd-.mlflow \
export MLFLOW_TRACKING_USERNAME=jayraj2498 \
export MLFLOW_TRACKING_PASSWORD=777e2be0b0c43fcc2efbc898716cbaebe35c912b \
export python script.py  '''   <-- optional >

from that command it get to know what mlflow log need to do  in dagshub repository  