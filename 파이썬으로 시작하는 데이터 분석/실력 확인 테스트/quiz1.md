Q>
다음 조건을 만족하는 코드를 고르세요.

```python
import numpy as np

array = np.arange(8)
```

위와 같이 array라는 이름의 numpy 배열이 있다.

코드를 실행하면 array에는 아래와 같은 값이 저장된다.

```
[0 1 2 3 4 5 6 7]
```

이 array를 아래와 같은 크기로 변경하여 matrix 변수에 저장하려고 한다.

```shell
[[0 1 2 3]

[4 5 6 7]]
```

어떤 코드를 작성해야 할까?

1. `matrix = array.reshape((2,4))`
2. `matrix = array.resize((2,4))`
3. `matrix = array.reshape((4,2))`
4. `matrix = array.resize((4,2))`

A>
1

해설>

```shell
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
```
