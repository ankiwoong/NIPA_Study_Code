Q>

다음의 그래프를 그리려면 어떤 코드를 사용해야 할까요?
<img src="https://kasausyrzlhe1066469.cdn.ntruss.com/global/file/p/5d3e56a1dce9bd1b7ef69db6/image.png">

1. ```python
   plt.set_xlabel("number")
   plt.set_ylabel("value")
   plt.bar(data, bins=50)
   plt.legend(loc='upper left', label = 'value')
   ```

2. ```python
   plt.set_xlabel("number")
   plt.set_ylabel("value")
   plt.hist(data, bins=50, label = 'value')
   plt.legend(loc='upper left')
   ```

3. ```python
   plt.set_xlabel("value")
   plt.set_ylabel("number")
   plt.hist(data, bins=50)
   plt.legend(loc='upper left', label = 'value')
   ```

4. ```python
   plt.set_xlabel("value")
   plt.set_ylabel("number")
   plt.bar(data, bins=50, label = 'value')
   plt.legend(loc='upper left')
   ```

A>
3

해설>

hist = 히스토그램 그래프<br>
loc = 범례위치<br>
lable = 범례명
