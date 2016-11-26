class Exercise:

    def __init__(self, name, group, secondary_group, weights, stability_ball):
        self.name = name
        self.group = group
        self.secondary_group = secondary_group
        self.weights = False
        self.stability_ball = False
        self.count = '0'

        if(weights == 'y') or (weights == 'True') or (weights is True):
            self.weights = True
        if(stability_ball == 'y') or (stability_ball == 'True') or (stability_ball is True):
            self.stability_ball = True

    def __str__(self):
        string = '\n\n*'
        string += self.name + '*'
        string += '\nGroup: ' + self.group
        string += '\nSecondary Group: ' + (self.secondary_group or '-')
        string += '\nRequires Weights: ' + ('Yes' if (self.weights) else 'No')
        string += '\nRequires Stability Ball: ' + ('Yes' if (self.stability_ball) else 'No')
        return string
