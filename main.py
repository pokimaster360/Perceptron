import numpy as np

X = np.array(
    [   
        [3, 11],  #True
        [4,10],  #True
        [5,8],  #True
        [3,5], # False  
        [5,6], # False  
        [1,3], # False      # Study Hours - Sleep Hours
    ],
    dtype= float
)

Y = np.array(
    [
        1,    #1
        1,    #2
        1,    #3
        0,    #4
        0,    #5
        0,    #6
    ],
    dtype= float
)



np.random.seed(4)
W = np.random.randn(2)

b = np.random.randn()


lr = 0.01



def forward(W, b):
    global loss
    
    Y_pred = X @ W + b          # (12,)
    L = Y_pred - Y              # (12,)
    
    loss = np.mean(L**2)
    gradient = (2 / len(X)) * (X.T @ L)   # (2,)
    
    W -= lr * gradient
    b -= lr * (2 / len(X)) * np.sum(L)

def predict():
    Y_pred = X @ W + b

    return Y_pred

def Answer():
    ans = []
    for x in predict():
        x = round(x)

        if x > 0:
            ans.append('Aprobado')
        else:
            ans.append('Reprobado')

    return ans


print(Answer())


for epoch in range(50000):
    forward(W,b)

    if epoch % 10000 == 0:
        print('-' * 80)
        print(f' Epoch: {epoch}')
        print(f' W: {W} | Loss: {loss}')
    
print("W:", W, "b:", b, "loss:", loss)


print(Answer())