import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline


from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_ob_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        self.numerical_columns = ['writing_score','reading_score']
        self.categorical_columns = ['gender',
                                'race_ethnicity',
                                'parental_level_of_education',
                                'lunch',
                                'test_preparation_course']
        self.target_column_name = 'math_score'

    def get_data_transformer_object(self):
        """

        function performs data transformation
        """
        try:
            
        
            num_pipeline = Pipeline(steps=[
            ('imputer',SimpleImputer(strategy='median')),
            ('scaller',StandardScaler())
        ])
            logging.info(f"numerical columns: {self.numerical_columns}")

            cat_pipeline = Pipeline(steps=[
            ('imputer',SimpleImputer(strategy='most_frequent')),
            ('ohe',OneHotEncoder(drop='first',handle_unknown='ignore'))

        ])
            logging.info(f"categorical columns: {self.categorical_columns}")

            preprocessor = ColumnTransformer([ 
                ('num_pipeline',num_pipeline,self.numerical_columns),
                ('cat_pipeline',cat_pipeline,self.categorical_columns)
            ]
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_tranformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('read train and test data completed')

            logging.info('obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformer_object() 

            input_feature_train_df = train_df.drop(self.target_column_name,axis=1)
            target_feature_train_df = train_df[self.target_column_name]


            input_feature_test_df = test_df.drop(self.target_column_name,axis=1)
            target_feature_test_df = test_df[self.target_column_name]

            logging.info(f"applying preprocessing object on training and testing dataframe")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            
            

            save_object(
                file_path = self.data_transformation_config.preprocessor_ob_file_path,
                obj = preprocessing_obj
            )
            logging.info(f"saved preprocessing object.")

            return (
                train_arr,
                test_arr, 
                self.data_transformation_config.preprocessor_ob_file_path
            )


        except Exception as e:
            raise CustomException(e,sys)
            
