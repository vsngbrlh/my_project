import matplotlib
import matplotlib.font_manager
import matplotlib as mpl
import matplotlib.pyplot as plt
# [f.name for f in matplotlib.font_manager.fontManager.ttflist if 'Nanum' in f.name]

#유니코드가 깨지는 현상을 방지
mpl.rcParams['axes.unicode_minus'] = False #minus 값이 깨지지 않도록

#폰트 설정
plt.rcParams['font.family'] = 'NanumGothic'

import pandas as pd
import numpy as np
import os
import warnings as wr #경고문을 출력하지 않는다

#엑셀 파일 불러오기
>>> import openpyxl #패키지 불러오기
>>> filename = "iris.xlsx" #파일명
>>> book = openpyxl.load_workbook(filename) #엑셀파일 book 변수에 저장
