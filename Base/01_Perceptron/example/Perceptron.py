import numpy as np

class Perceptron:
    def __init__(
            self, 
            units:int=None,
            lr:float=0.01
        ):
        '''Perceptron
        parameters
        - units : number of inputs(int)
        - lr : learning_rate(float)
        ''' 
        self.units:int = units
        self.learning_rate:float = lr
        self.weight:np.ndarray = None
        self.bias:np.ndarray = np.random.uniform(-1, 1, size=1)

        if units != None:
            self.weight:np.ndarray = np.random.uniform(-1, 1, size=self.units)

    def Input(self, units:int=None):
        if self.units == None:
            self.units = units
        
        self.weight = np.random.uniform(-1, 1, size=self.units)
        
    def Activation(self, X):
        # step function
        return np.where(X > 0, 1, 0)

    def Forward(self, x):
        X = np.dot(x, self.weight) + self.bias
        y = self.Activation(X)
        return y
    
    def Back(self, update, x):
        self.weight += update * x
        self.bias += update
    
    def Train(self, 
            X:np.ndarray, 
            y:np.ndarray,
            epochs:int
        ):
        for epoch in range(epochs):
            for x_i, y_i in zip(X,y):
                predict_y = self.Forward(x_i)
                update = self.learning_rate * (y_i - predict_y)
                self.Back(update, x_i)
    
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