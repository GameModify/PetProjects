class StaticClass:


    @staticmethod
    def update1(data):
        return data

    @staticmethod
    def update2(data):
        return StaticClass.__convert(data)

    @staticmethod
    def __convert(data):
        return data



class SomeClass:
    def update1(self, data):
        self.data = data
        return data

    def update2(self, data):
        return self.__convert(data)

    def __convert(self, data):
        return data

result = StaticClass.update1(123123)

test = SomeClass()

result = test.update1(34234)