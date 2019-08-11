<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
# learn_algorithm_in_python
## 算法复杂度
* 例如计算以下时间复杂度

```python
def func():
	n = 10
	for i in range(n):
		for j in range(i,n):
			a = 1
```
计算次数：
 \\(n+(n-1)+...+1=n*\frac{n+1}{2}=\frac{1}{2}n^2+\frac{n}{2}\\)  
 时间复杂度：为O(\\(n^2\\))  
 系数，非最高此项均可视为常数项
## 数据结构
