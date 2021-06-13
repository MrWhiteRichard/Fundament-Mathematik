class StepSize:

    def __init__(self, function):

        if type(function) in [int, float]:
            self.function = lambda a, n: function
        
        else:
            self.funtion = function

    def __call__(self, a, n):
        self.function(a, n)