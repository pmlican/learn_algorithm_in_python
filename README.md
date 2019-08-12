## 算法复杂度
* 例如计算以下时间复杂度

```python
def func():
    a = 1
```
时间复杂度：
O(1)

```
def func():
    n = 10
    for i in range(n):
        a = 1
```
时间复杂度 O(n)

```python
def func():
	n = 10
	for i in range(n):
		for j in range(i,n):
			a = 1
```
计算次数：
<img src="https://latex.codecogs.com/svg.latex?\Large&space;n+(n-1)+...+1=n*\frac{n+1}{2}=\frac{1}{2}n^2+\frac{n}{2}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />
 时间复杂度：为O(n^2)  
 系数，非最高此项均可视为常数项

```python
def func(n):
    if n <= 1: return n
    return func(n - 1) + func(n - 1)
```
时间复杂度为O(2^n)  
f(5)->f(4)+f(4)->f(3)+f(3)+f(3)+f(3)->f(2)+f(2)+f(2)+f(2)+f(2)+f(2)+f(2)+f(2)

```python
def func(n):
    if n <= 1: return n
    return func(n//2)+1
```
时间复杂度为O(log(N))

```python
def func(n):
    if n <= 1: return
    mid = n // 2
    for i in range(mid+1,n):
        a = 1
    func(mid)
```
渐进复杂度O(N)  
f(n) = f(n/2) + n/2 = f(n/4) + n/2 + n/4 = n/2 + n/4 + n/8 + ... <= n

```python
a = []
def func(x):
    if x == 0:
        a.push(x)
    else:
        while a.size() > 0:
            a.pop()  
```
均摊复杂度O(N)  
分析：
x=0,单次时间复杂度为O(1)
x!=0,单次时间复杂度为O(N)
总的pop次数不会超过全部x=0的次数，所以总体复杂度为O(N)

## 数据结构
![equation](http://www.sciweavers.org/tex2img.php?eq=1%2Bsin%28mc%5E2%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)

