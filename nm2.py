import numpy as np

a = np.ones(5)
b = np.zeros(3)
c = np.empty(2)
print(a)
print(b)
print(c)

t = np.arange(5)
print(t)

t = np.arange(2, 10, 2)
print(t)

# you say you want 5 number between 0 and 10
s = np.linspace(0, 10, num=5)
print(s)


# matrix 2 spaces 
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print("a -----------")
print(a.ndim)
print(a.size)
print(a.shape)

# tensor spaec more than 2 
b = np.array([
    [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ],
    [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ]
])
print("b -----------")
print(b.ndim)
print(b.shape)
print(b.size)


# work math with numpy
a = [1, 2, 5, 7]
print(np.prod(a)) # برای ضرب 

b = np.power([2, 3.5], 3) # اعداد داخل لیست به توان 3 میرسه که بیرونش نوشتیم
print(b)

c = np.linspace(-np.pi/2, np.pi/2, 100)
print(np.sin(c)) # برای گرفتن سینوس

e = 4
print(np.sqrt(e)) # برای گرفتن جذر یک عدد
print(np.emath.sqrt(-4)) # emath در فضاهای مختلف انجام میده // یا میشه گفت خارج از اعداد حقیقی رو حساب میکنه


# shapre and reshape / میتونید از 1 در 1 تبدیل کنید به 3 در 4 یا ...
a = np.arange(12)
print(a)
b = a.reshape(3, 4)
print(b)
    # -1 convert it to flat again / یا همون 1 در 1 قبل
c = b.reshape(-1)
print(c)
    # همون کاره -1 رو میکنه  
c = b.ravel()
print(c)
    # flatten هم همون کاره -1 رو میکنه ravel  
        # با این تفاوت که یه copy میسازه   
c = b.flatten()
print(c)

