from statslibx.descriptive import DescriptiveStats
from typing import Optional, Literal, List, Union
import pandas as pd
import numpy as np

class Descriptive:
    def __init__(self, data: Union[pd.DataFrame, np.ndarray], sep: str = None, decimal: str = None, thousand: str = None):
        self.stats = DescriptiveStats(
            data,
            sep=sep or ',',
            decimal=decimal,
            thousand=thousand
        )

    def mean(self, column: Optional[str] = None):
        return self.stats.mean(column=column)

    def median(self, column: Optional[str] = None):
        return self.stats.median(column=column)
    
    def mode(self, column: Optional[str] = None):
        return self.stats.mode(column=column)

    def variance(self, column: Optional[str] = None):
        return self.stats.variance(column=column)
    
    def std(self, column: Optional[str] = None):
        return self.stats.std(column=column)
    
    def skewness(self, column: Optional[str] = None):
        return self.stats.skewness(column=column)
    
    def kurtosis(self, column: Optional[str] = None):
        return self.stats.kurtosis(column=column)
    
    def quantile(self, q: Union[float, List[float]], column: Optional[str] = None):
        return self.stats.quantile(q, column=column)
    
    def outliers(self, column=None, threshold=1.5, method='iqr'):
        return self.stats.outliers(column=column, threshold=threshold, method=method)
    
    def correlation(self, method='pearson', columns=None):
        return self.stats.correlation(method=method, columns=columns)
    
    def covariance(self, columns=None):
        return self.stats.covariance(columns=columns)
    
    def summary(self, columns=None):
        return self.stats.summary(columns=columns)
    
    def linear_regression(self, 
                        X: Union[str, List[str]], 
                        y: str,
                        engine: Literal['statsmodels', 'scikit-learn'] = 'statsmodels',
                        fit_intercept: bool = True,
                        show_plot: bool = False,
                        plot_backend: str = 'seaborn',
                        handle_missing: Literal['drop', 'error', 'warn'] = 'drop') -> tuple:
        return self.stats.linear_regression(X, y, engine, fit_intercept, show_plot, plot_backend, handle_missing)

