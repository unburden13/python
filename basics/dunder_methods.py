# Dunder methods are special methods with default functionality for objects
# They can be overwritten in order to take advantage of the syntax
# Some examples:

class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'option1': 'yoyo',
            'option2': 'ball'
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return 'called!'

    def __getitem__(self, index):
        return self.my_dict[index]

    def __del__(self):
        print('deleted!')


action_figure = Toy('red',10)
print(action_figure.__str__())
print(len(action_figure))
print(action_figure())
print(action_figure['option2'])
del action_figure

