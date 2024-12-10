import numpy as np

class Perceptron:
    def __init__(
            self, 
            input_num:int=None,
            lr:float=0.01
        ):
        self.input_num:int = input_num
        self.learning_rate:float = lr
        self.weight:np.ndarray = None

        if input_num != None:
            self.weight:np.ndarray = np.random.uniform(-1, 1, size=self.input_num+1)

    def Input(self, input_num:int=None):
        if self.input_num == None:
            self.input_num = input_num
        
        self.weight = np.random.uniform(-1, 1, size=self.input_num+1)
        
    def Activation(self, X):
        # step function
        return np.where(X > 0, 1, 0)

    def Forward(self, x):
        X = np.dot(x, self.weight[1:]) + self.weight[0]
        y = self.Activation(X)
        return y
    
    def Back(self, update, x):
        self.weight[1:] += update * x
        self.weight[0] += update
    
    def Train(self, 
            X:np.ndarray, 
            y:np.ndarray,
            epochs:int
        ):
        if X.shape != self.weight.shape: return False

        for epoch in range(epochs):
            for x_i, y_i in zip(X,y):
                predict_y = self.Forward(x_i)
                update = self.learning_rate * (y_i - predict_y)
                self.Back(update, x_i)
        return True
    
    def Predict(self, X):
        return self.Forward(X)
    
if __name__ == "__main__":
    X = np.array([
        [0,0], [0,1], [1,0], [1,1],
    ])
    y = np.array([0,0,0,1])

    p = Perceptron()
    p.Input(2)
    p.Train(X, y, epochs=100)
    print(p.Predict([1,1]))