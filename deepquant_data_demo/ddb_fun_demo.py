# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
os.environ["deepquantsdk_env"] = 'inner'
from deepquant.data.interface.dataApi import DataApi
import pandas as pd
import numpy as np
from deepquant.data.gqclient.commons import FunctionMode

if __name__ == '__main__':

    row_num = 10
    data2 = "string_1"
    data5 = pd.DataFrame({'Code': np.random.randint(1, 3, row_num), 'Price': np.random.randn(row_num)})
    data6 = 42.42
    data7 = {'k1': 'v1'}


    data = DataApi('<域用户名>', '<token>', timeout=30)
    data,_,_=data.function_compute(function_name="funTest", mode=FunctionMode.COMPLEX, params=[data2, data6])
    print(data)

