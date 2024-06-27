class Subject:
    def __init__(self, name):
        self.name = name
        self._observers = []
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    
    def notify(self, value):
        for observer in self._observers:
            observer.update(self, value)
    
class Observer:
    def __init__(self, subject):
        subject.attach(self)
        self.subject = subject

    def update(self, subject, value):
        self.subject = value

