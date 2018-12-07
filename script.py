class Greeting:

    @staticmethod
    def greet(name):
        if not isinstance(name, str):
            raise TypeError('Please provide a valid string argument')
        return('Hello, {}'.format(name))


