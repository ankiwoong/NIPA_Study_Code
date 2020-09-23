Q>
다음 중 DataFrame 연산에 대한 설명으로 틀린 것을 고르세요.

1. Series 연산을 사용 가능하다.
2. 사칙 연산은 add, mul과 같은 함수로 사용한다.
3. sum, mean과 같은 집계 함수가 사용이 가능하다.
4. null 데이터를 체크할 수 없다.다음 중 DataFrame 연산에 대한 설명으로 틀린 것을 고르세요.

A>
4

해설>

실제 데이터셋에선 누락된 null 데이터가 많으므로, 이를 체크하는 것이 중요합니다.<br>
데이터 프레임 내에서 다음과 같은 코드로 누락된 데이터를 체크할 수 있습니다.

```python
dataframe.isnull()
dataframe.notnull()
```
