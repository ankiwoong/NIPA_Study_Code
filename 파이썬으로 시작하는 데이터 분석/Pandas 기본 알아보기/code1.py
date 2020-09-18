import pandas as pd

# Pandas
# 구조화된 데이터를 효과적으로 처리하고 저장할 수 있는 파이썬 라이브러리.
# Array 계산에 특화된 Numpy를 기반으로 만들어져서 다양한 기능들을 제공한다.

# Series : numpy array가 보강된 형태 Data와 Index를 가지고 있다.
data = pd.Series([[1, 2, 3, 4]])
print(data)

# 인덱스를 가지고 있고 인덱스로 접근 가능하다.
data = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(data)
print(data[2])

# 딕셔너리로 만들수 있다.
population_dict = {"korea": 5180, "japan": 12718, "china": 141500, "usa": 32676}

polulation = pd.Series(population_dict)

print(polulation)
print(polulation.values)