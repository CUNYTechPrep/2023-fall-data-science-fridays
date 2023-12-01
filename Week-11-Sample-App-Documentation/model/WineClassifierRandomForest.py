import os
import re
import pickle

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


from sklearn.ensemble import RandomForestClassifier





class WineClassifierRandomForest:
    """
    Class object that loads latest saved RandomForestClassifier model
    to predict Wine Class trained using the Wine dataset from sklearn.
    It also allows to create new models and save them easily.
    """
    
    def __init__(self):
        self.model_path = '../sample-app/model/models'
        self.model_base_name = self.model_path + '/' + 'wine_random_forest_classifier'
        
        self.model_number = self.__get_model_number()
        self.model = self.load_model()
        
        
    def __get_model_name(self):
        """
        Private method that get the name of the to load the model.

        Return:
            * model_file_name - str: name of file of the latest model.
        """
        models_list = []

        files = os.walk(self.model_path)

        for f in files:
            models = [self.model_path + '/' + model for model in f[2] if model.endswith('.pkl')]
            models_list.extend(models)
        model_file_name = sorted(models_list)[-1]

        return model_file_name
    
    
    def __get_model_number(self):
        """
        Private method that returns the number assigned of the latest model.

        Return:
            * model_number - int: number of latest saved model.
        """
        model_number = int(re.findall(r'\d+', self.__get_model_name())[0])
        return model_number
        
        
    def load_model(self):
        """
        Method to load and return latest saved model.

        Return:
            * model - RandomForestClassifier; classification model.
        """
        model_name = self.__get_model_name()
        
        with open(model_name, 'rb') as model_file:
            model = pickle.load(model_file)
        return model
            
        
    def predict(self, X: pd.DataFrame) -> list:
        """
        Predicts wine class (0, 1, 2) based on the features passed.

        Parameters:
            * X - pd.DataFrame: Pandas DataFrame of shape (13, {...}).

        Return:
            * prediction - list: list of wine classes (0, 1, 2).
        """
        prediction = self.model.predict(X)
        return prediction
            
            
    def __load_train_data(self):
        """
        Private method that loads Wine Dataset from Sklearn to retrain the model.

        Return:
            * wine_df - pd.DataFrame: Input features with 13 attributes.
            * target - np.array: Dependent variables of shape (1, {..}).
        """
        wine_data = datasets.load_wine()
        
        wine_df = pd.DataFrame(wine_data['data'], columns=wine_data['feature_names'])
        target = pd.DataFrame(wine_data['target'], columns=['target'])
        
        return wine_df, target
    
    
    def __split_train_data(self, random_state: int = 42, test_size: float = 0.2):
        """
        Private method to split Wine Dataset into training and testing.

        Parameters:
            * random_state - int: number to seed the split of training
                and testing data.
            * test_size - float: decimal number to partition testing
               data (0, 1).

        Return:
            * x_train - pd.DataFrame: training independent variables.
            * x_test - pd.DataFrame: testing independent variables.
            * y_train - np.array: training dependent variables.
            * y_test - np.array: testing dependent variables.
        """
        wine_df, target = self.__load_train_data()
        
        x_train, x_test, y_train, y_test = train_test_split(
            wine_df,
            target,
            stratify=target,
            test_size=test_size,
            random_state=random_state
        )
        
        return x_train, x_test, y_train, y_test
    
    
    def __incerment_model_number(self):
        """
        Private method to increment the number from the latest saved model.
        """
        self.model_number += 1
        
            
    def retrain_model(self, n_estimators:int = 11, random_seed: int = 42, random_state: int = 42, test_size: float = 0.2):
        """
        Creates new RandomForestClassifier model with the option to tweak
        some parameters.

        Parameters:
            * n_estimators - int: number of Desicion trees to be used.
            * random_seed - int: number to seed the model to make reproducible.
            * random_state - int: number to seed the split of training
                and testing data.
            * test_size - float: decimal number to partition testing
               data (0, 1).
        """
        np.random.seed(random_seed)
        
        x_train, x_test, self.y_train, self.y_test = self.__split_train_data(random_state=random_state, test_size= test_size)
        
        self.new_model = RandomForestClassifier(n_estimators=n_estimators)
        
        self.new_model.fit(x_train, self.y_train)
        
        self.y_train_pred = model.predict(x_train)
        self.y_test_pred = model.predict(x_test)
        
        
    def save_retrained_model(self):
        """
        Method that saves new model and automatically assigns new model
        to be used.
        """
        self.__incerment_model_number()
        
        model_name = f'{self.model_base_name}_{self.model_number}.pkl'
        
        with open(model_name, 'wb') as model_file:
            pickle.dump(self.new_model, model_file)
            
        self.model = self.load_model()
        
        
    def get_retrained_model_accuracy_score(self):
        """
        Prints accuracy score of new retrained model for the training
        and testing datasets.
        """
        train_accuracy_score = accuracy_score(self.y_train, self.y_train_pred)
        test_accuracy_score = accuracy_score(self.y_test, self.y_test_pred)
        
        print('*'*200)
        print(f'Training Accuracy Score: {train_accuracy_score} \n')
        print(f'Testing Accuracy Score: {test_accuracy_score} \n')
        print('*'*200)
        
        
    def get_retrained_model_confusion_matrix(self):
        """
        Prints Confusion Matrix of new retrained model for the training
        and testing datasets.
        """
        print('*'*200)
        print('Training Confusion Matrix: \n')
        print(confusion_matrix(self.y_train, self.y_train_pred))
        print('\n\n')
        print(f'Testing Confusion Matrix: \n')
        print(confusion_matrix(self.y_test, self.y_test_pred))
        print('*'*200)
        
        
    def get_retrained_model_classification_report(self):
        """
        Prints Classification Report of new retrained model for the training
        and testing datasets.
        """
        print('*'*200)
        print('Training Classification Report: \n')
        print(classification_report(self.y_train, self.y_train_pred))
        print('\n\n')
        print(f'Testing Classification Report: \n')
        print(classification_report(self.y_test, self.y_test_pred))
        print('*'*200)
        
if __name__ == '__main__':
    # test 1: check first model works
    print('Test 1:')
    wine_data = datasets.load_wine()
    wine_df = pd.DataFrame(wine_data['data'], columns=wine_data['feature_names'])
    wine_df_head = wine_df.head(1)
    wine_df_tail = wine_df.tail(1)
    
    model = WineClassifierRandomForest()
    prediction_head = model.predict(wine_df_head)
    prediction_tail = model.predict(wine_df_tail)
    
    print(prediction_head)
    print(prediction_tail)
    
    print('-'*200)
    
    # Test 2: checking retrained model
    model.retrain_model(n_estimators=9, random_seed=40, random_state=40, test_size=0.15)
    model.get_retrained_model_accuracy_score()
    model.get_retrained_model_confusion_matrix()
    model.get_retrained_model_classification_report()
    model.save_retrained_model()
    
    prediction_head = model.predict(wine_df_head)
    prediction_tail = model.predict(wine_df_tail)
    
    print(prediction_head)
    print(prediction_tail)
                