#!/usr/bin/env python
# coding: utf-8

# ### 문제.  다음 셀에 우리가 배운 데이터시각화 라이브러리 두 가지, 데이터 분석 라이브러리, 수학 연산 라이브러리를 약어별칭(alias)과 함께 불러오세요.

# In[1]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### 문제. finaltaskdata.csv 파일을 msleep 이라는 데이터 프레임으로 불러오세요. 

# In[2]:
# import finaltaskdata.csv whose seperator is ; in database folder as msleep dataframe
msleep = pd.read_csv('./database/finaltaskdata.csv', sep=';')
pd.options.display.max_columns = None
pd.options.display.max_rows = None



# ### 문제. 데이터 앞부분 10개 행을 확인하세요.

# In[3]:
pd.set_option('max_columns', None)
print(msleep.head(10))



# ### 문제.  데이터에 대한 전반적인 정보를 확인하세요.

# In[4]:
#print(msleep.info())




# ### 문제.  데이터의 칼럼명을 확인하세요.

# In[5]:
#print(msleep.columns)



# ### 문제. brainwt과 bodywt 칼럼명을 brain_weight과 body_weight으로 변경하고 다시 칼럼명을 확인하세요.

# In[6]:
msleep.rename(columns={'brainwt':'brain_weight', 'bodywt':'body_weight'}, inplace=True, errors='raise')
#print(msleep.columns)


# ### 문제.  데이터의 칼럼별 요약통계량을 확인하세요.

# In[7]:
#print(msleep.describe())




# ### 문제. 요약통계량에서 음수가 있는지 확인한 것을 바탕으로 이상치가 있는 칼럼의 이상치를 제거하고, 해당 칼럼의 최소값을 확인하세요.

# In[8]:
msleep = msleep[msleep['sleep_total'] > 0]
msleep = msleep[msleep['sleep_rem'] > 0]
msleep = msleep[msleep['sleep_cycle'] > 0]
msleep = msleep[msleep['awake'] > 0]
msleep = msleep[msleep['brain_weight'] > 0]
msleep = msleep[msleep['body_weight'] > 0]

# print minimum value of each column excluding column name
print(msleep.min(axis=0, skipna=True))

# In[9]:





# ### 문제. conservation status의 고유값별 빈도를 다음과 같이 확인하세요.

# In[10]:





# ### 문제. 멸종 위기가 높은 순서대로 아래와 같이 값을 변경하고 다시 고유값별 빈도를 확인하세요.
# - en => 1_endangered
# - vu => 2_vulnerable
# - nt => 3_near_threatened
# - lc => 4_least_concern
# - domesticated => 5_domesticated

# In[11]:





# ### 문제.  칼럼별 결측치의 개수를 한번에 확인해보세요.

# In[12]:





# ### 문제. 식성(vore) 변수에 대해서 결측치들을 "unknown"으로 대체하여 재할당하세요. 해당 칼럼의 고유값별 빈도를 다음과 같이 확인하세요.

# In[13]:





# ### 문제. 총수면량의 극단치를 확인해보세요.

# In[14]:





# ### 문제. 총수면량의 극단치를 제거하고, 다시 확인해보세요.
# - 복사본을 만들 필요는 없습니다.

# In[15]:





# ### 문제. 총수면량에서 렘수면량을 제외한 비렘수면량(sleep_nonrem)을 파생변수로 만들어 추가보세요.

# In[16]:





# ### 문제. 총수면량과 렘수면량, 비렘수면량에 대해서 분단위(in hours to minutes)로 계산된 파생변수를 각각 만들어 추가해보세요.(기존 변수명 뒤에 '_min'을 붙이세요)
# - msleep 데이터 안에 파생변수가 존재하도록 진행해야 됩니다.

# In[17]:





# ### 문제. 식성(육/초/충/잡/모름)별로 총수면량(시간단위)의 평균을 출력해보세요.
# - 그룹으로 묶은 뒤 해당하는 칼럼만 추출하여 진행하도록 하세요. 마찬가지로 한줄로 작성하도록 합니다.

# In[18]:





# ### 문제. 아래의 표는 멸종 위협에 대해서 High와 Low, Non으로 구분한 표입니다. red_list라는 데이터 프레임으로 만들어보세요. 
# ```python
# conservation               risk
# 
# 1_endangered               high
# 2_vulnerable               high
# 3_near_threatened          low
# 4_least_concern            low
# 5_domesticated             non
# unknown                    non
# ```
# - 상단의 칼럼명(변수명)은 데이터에 입력할 필요는 없습니다.

# In[19]:





# ### 문제. red_list 데이터 프레임을 활용하여 msleep 데이터에 risk 라는 변수가 추가되도록 재할당하세요. 데이터 앞부분을 확인해보세요.
# - 적절하게 병합하여 파생변수가 생성되는 것과 같이 추가되도록 하세요.

# In[20]:





# ### 문제. 멸종 위기(risk)가 높은지 낮은지 없는지에 따라 깨어있는 시간(awake) 분포를 막대그래프로 다음과 같이 출력해보세요.
# - 투명도는 멸종 위기가 높은 경우 0.7, 낮은 경우 0.5, 없는 경우 0.3으로 지정하세요.

# In[21]:





# In[22]:




