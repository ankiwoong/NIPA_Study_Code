Q>

다음 문제를 읽고 올바른 정답을 작성하세요.<br>
1부터 100까지의 숫자 중 랜덤하게 10개의 정수를 뽑아 1행 10열의 Array를 생성하고 A라고 저장하고<br> 10행1열의 Array를 생성하여 B라고 저장했다고 합니다.<br>

```python
A = np.random.randint(0,100,[1,10])
B = np.random.randint(0,100,[10,1])
```

A와 B의 합을 계산하면 몇행 몇열의 Array가 생성될지 예상해보자.<br>
Shape이 다른 Array끼리의 연산을 무엇이라 부르는가?<br>
<br>
답안 예시><br>
만약 생성된 Array의 예상한 크기가 5행 5열이고, Shape이 다른 Array끼리의 연산을 연산방법이라고 부른다면<br>
5행 5열, 연산방법 이라고 입력합니다.

A>
10행 10열, 연산방법

해설>

```shell
array([[118, 111, 131, 145,  46, 108,  93,  88, 111, 106],
       [170, 163, 183, 197,  98, 160, 145, 140, 163, 158],
       [138, 131, 151, 165,  66, 128, 113, 108, 131, 126],
       [109, 102, 122, 136,  37,  99,  84,  79, 102,  97],
       [109, 102, 122, 136,  37,  99,  84,  79, 102,  97],
       [137, 130, 150, 164,  65, 127, 112, 107, 130, 125],
       [106,  99, 119, 133,  34,  96,  81,  76,  99,  94],
       [149, 142, 162, 176,  77, 139, 124, 119, 142, 137],
       [133, 126, 146, 160,  61, 123, 108, 103, 126, 121],
       [143, 136, 156, 170,  71, 133, 118, 113, 136, 131]])
```
