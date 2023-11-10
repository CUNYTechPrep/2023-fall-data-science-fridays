# PANDAS IS FOR DATA WRANGLING
import pandas as pd
import numpy as np

# SEABORN IS A PLOTTING LIBRARY
import seaborn as sns

# MATPLOT LIB IS ALSO A PLOTTING LIBRARY
import matplotlib.pyplot as plt

# SKLEARN IS OUR MACHINE LEARNING PACKAGE
from sklearn.linear_model import LinearRegression

# IMPORT OUR RANDOM FOREST REGERSSOR
from sklearn.ensemble import RandomForestRegressor

# METRICS HELP US SCORE OUR MODEL
from sklearn import metrics

# HELP US SPLIT OUR DATA INTO TESTING A TRAINING
from sklearn.model_selection import train_test_split

# Good ol statsmodels
import statsmodels.api as sm

# Specific root mean squared error for stats models
from statsmodels.tools.eval_measures import rmse

from statsmodels.stats.outliers_influence import variance_inflation_factor

from statsmodels.api import qqplot


class CTP_LinReg():
    def __init__(self, 
                 df: pd.DataFrame, 
                 independent_variables: [str, list], 
                 dependent_variable: str, 
                 simple=False):
        ######################################################################
        self.df = df
        if simple:
            self.independent_variables = [independent_variables]
        else:
            self.independent_variables = independent_variables
        self.dependent_variable = dependent_variable
        self.X = df[self.independent_variables]
        self.X = sm.add_constant(self.X)
        self.y = df[self.dependent_variable]
    
    def build_model(self):
        self.model = sm.OLS(self.y, self.X).fit()
        self.y_pred = self.model.predict(self.X)
        print(self.model.summary())
        print('\n')
        print('#'*79)
        root_mean_squared_error = rmse(self.y, self.y_pred)
        print( 'Dependent Variable %s average: ' % self.dependent_variable, self.y.mean())
        print( 'RMSE:', root_mean_squared_error)
        try:
            print( 'RMSEs Percentage off average:', ((root_mean_squared_error / self.y.mean())*100).round(2))
        except:
            pass
        print('#'*79)
        pass
    
    def check_linearity(self):
        for col in self.independent_variables:
            sns.jointplot(x=col, y=self.dependent_variable, data=self.df, kind="reg");
        pass

    def check_normality(self):
        print('#'*79)
        print('Checking Normality')
        self.residuals =  self.y.values - self.y_pred.values 

        # histogram
        sns.histplot(self.residuals)
        plt.show()

        # qq plot
        qqplot(self.residuals, line='q');
        plt.show()
        print('#'*79)
        pass 

    def plot_homo(self):
        plt.scatter(self.model.fittedvalues, self.model.resid, alpha=0.5)
        plt.xlabel('Fitted Values')
        plt.ylabel('Residuals')
        plt.axhline(y = 0, color = 'r')
        plt.show()
        pass

    ##########################################################################    
    def plot_correlation(self):
        plt.figure(figsize = (13,13))
        all_vars = self.independent_variables
        all_vars.append(self.dependent_variable)

        ax = sns.heatmap( self.df[all_vars].corr(numeric_only=True), 
                    annot=True, 
                    cmap='coolwarm',
                    vmin=-1, vmax=1);
        plt.show()
        

    ##########################################################################
    def get_vif(self):
        vif = [variance_inflation_factor(self.X.values, i) for i in range(self.X.shape[1])]
        self.vif_df = pd.DataFrame(columns=self.X.columns, data=[vif])
        print('#'*79)
        print('Variance Inflaction Factors')
        print(self.vif_df)
        print('#'*79)
        pass

    def check_colin(self):
        self.plot_correlation()
        self.get_vif()
        pass

    def run_all(self):
        self.build_model()
        self.check_linearity()
        self.check_colin()
        self.check_normality()
        self.plot_homo()




