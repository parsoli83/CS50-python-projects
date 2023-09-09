class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self.cookies=0
    def __str__(self):
        if self.cookies==0:
            return ""
        return "🍪"*self.cookies

    def deposit(self, n):
        if self.cookies+n<=self.capacity:
            self.cookies=self.cookies+n
        else:
            raise ValueError

    def withdraw(self, n):
        if self.cookies-n>=0:
            self.cookies=self.cookies-n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self,capacity):
        try:
            if type(capacity)==int:
                if capacity>=0:
                    self._capacity=capacity
                else:
                    raise ValueError
            else:
                raise ValueError
        except:
            raise ValueError

    @property
    def size(self):
        return self.cookies
