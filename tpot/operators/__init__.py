#### Statistical learning operators
from .C_SVM import C_SVM
from .DecisionTree import DecisionTree
from .KNNc import KNNc
from .GradientBoosting import GradientBoosting
from .LogisticRegressionGLM import LogisticRegressionGLM
from .PCA import PCAoperator
from .PolynomialFeaturesOperator import PolynomialFeaturesOperator
from .RandomForest import RandomForest
from .RecursiveFeatureElim import RecursiveFeatureElim
from .RobustScalerOperator import RobustScalerOperator
from .SelectPercentileOperator import SelectPercentileOperator
from .StandardScalerOperator import StandardScalerOperator
from .SelectKBestOperator import SelectKBestOperator

#### Misc transformation operators
#from .CombineDFs import CombineDFs

operator_registry = {
    #### Statistical learning operators
    'C_SVM':C_SVM(),
    'DecisionTree':DecisionTree(),
    'KNNc':KNNc(),
    'GradientBoosting':GradientBoosting(),
    'LogisticRegressionGLM':LogisticRegressionGLM(),
    'RandomForest':RandomForest(),
    
    ### Misc transformation operators
    ##'CombineDFs':CombineDFs() ## Does not work properly. I think it's a problem with preprocess_arguments()
    'PCAoperator':PCAoperator(),
    'PolynomialFeaturesOperator':PolynomialFeaturesOperator(),
    'RobustScalerOperator':RobustScalerOperator(),
    'StandardScalerOperator':StandardScalerOperator(),
    'RecursiveFeatureElim':RecursiveFeatureElim(),
    'SelectKBestOperator':SelectKBestOperator(),
    'SelectPercentileOperator':SelectPercentileOperator()
    }