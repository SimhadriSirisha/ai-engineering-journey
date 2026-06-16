import numpy as np

# sigmoid func
def sigmoid(W, X, b):
    return 1/(1 + np.exp(-(np.dot(W, X) + b)))

def cost(m, n, W, b, x_train, y_train, withReg, l):
    loss = 0
    for i in range(m):
        sigmoidVal = sigmoid(W, x_train[i], b)
        loss = loss + (-(y_train[i]*np.log(sigmoidVal)) - (1-y_train[i])*(np.log(1-sigmoidVal)))
    
        bce = loss/m

    if withReg:
        coefficientCost = 0
        for j in range(n):
            coefficientCost = coefficientCost + W[j]**2
        return bce + (l * coefficientCost)/(2*m)
    return bce

def get_w_derivatives(m, W, b, j, x_train, y_train, withReg, l):
    total = 0
    for i in range(m):
        f_wb = sigmoid(W, x_train[i], b)
        error = f_wb - y_train[i]
        total = total + error*x_train[i,j]

    if withReg:
        return (total/m) + (l/m)*W[j]
    return total/m

def get_b_derivatives(m, W, b, x_train, y_train):
    total = 0
    for i in range(m):
        f_wb = sigmoid(W, x_train[i], b)
        error = f_wb - y_train[i]
        total = total + error
    return total/m

def gradient_descent(iterations, learning_rate, x_train, y_train, withReg, l = 0):
    m = len(x_train)
    n = len(x_train[0])
    W = np.zeros(n)
    dj_dw = np.zeros(n)
    b = 0
    costs = []

    for k in range(iterations):
        dj_db = get_b_derivatives(m, W, b, x_train, y_train)
        for j in range(n):
            dj_dw[j] = get_w_derivatives(m, W, b, j, x_train, y_train, withReg, l)
        for j in range(n):
            W[j] = W[j] - learning_rate * dj_dw[j]
        b = b - learning_rate * dj_db
        c = cost(m, n, W, b, x_train, y_train, withReg, l)
        costs.append(c)

        if k%1000 == 0:
            print(f"cost @ {k}th iteration: {c}")

    return W, b, costs
