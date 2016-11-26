class Exercise:

    def __init__(self, name, group, secondary_group, weights, stability_ball, machine):
        self.name = name
        self.group = group
        self.secondary_group = secondary_group
        self.requires_weights = False
        self.requires_stability_ball = False
        self.requires_machine = False
        self.count = '0'

        if(weights == 'y') or (weights == 'True') or (weights is True):
            self.requires_weights = True
        if(stability_ball == 'y') or (stability_ball == 'True') or (stability_ball is True):
            self.requires_stability_ball = True
        if(machine == 'y') or (machine == 'True') or (machine is True):
            self.requires_machine = True

    def __str__(self):
        string = '\n\n*'
        string += self.name + '*'
        string += '\nGroup: ' + self.group
        string += '\nSecondary Group: ' + (self.secondary_group or '-')
        string += '\nRequires Weights: ' + ('Yes' if (self.requires_weights is True) else 'No')
        string += '\nRequires a Stability Ball: ' + ('Yes' if (self.requires_stability_ball is True) else 'No')
        string += '\nRequires a Machine: ' + ('Yes' if (self.requires_machine is True) else 'No')
        return string
