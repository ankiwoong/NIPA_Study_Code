import pandas as pd

# DataFrame : 여러 개의 Series가 모여서 행과 열을 이룬 데이터
population_dict = {
    "korea": 5180,
    "japan": 12718,
    "china": 141500,
    "usa": 32676,
}
polulation = pd.Series(population_dict)

gdp_dict = {
    "korea": 169320000,
    "japan": 517670000,
    "china": 1409250000,
    "usa": 2041280000,
}
gdp = pd.Series(gdp_dict)

country = pd.DataFrame({"population": polulation, "gdp": gdp})

print(country)

print("-" * 20)

# 딕셔너리로 만들수 있다.
print(country.index)  # 인덱스 확인
print(country.columns)  # 컬럼 확인
print(country["gdp"])  # 컬럼 값 확인
print(type(country["gdp"]))  # 컬럼 타입 확인

print("-" * 20)

# Series도 numpy array 처럼 연산자를 쓸 수 있다.
gdp_per_capita = country["gdp"] / country["population"]
country["gdp per capita"] = gdp_per_capita

print(country)

print("-" * 20)

# 만든 데이터 프레임을 저장할 수 있다.
country.to_csv(
    "D:\\Code\\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\Pandas 기본 알아보기\\result\\country.csv"
)  # csv 파일 생성
country.to_excel(
    "D:\\Code\\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\Pandas 기본 알아보기\\result\\country.xlsx"
)  # excel 파일 생성

country_csv = pd.read_csv(
    "D:\\Code\\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\Pandas 기본 알아보기\\result\\country.csv"
)  # csv 파일 읽기
country_excel = pd.read_excel(
    "D:\\Code\\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\Pandas 기본 알아보기\\result\\country.xlsx"
)  # excel 파일 읽기

print(country_csv)
print(country_excel)