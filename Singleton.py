class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_)
        return class_._instance
    
    def __init__(self, *args, **kwargs):
        if not hasattr(self.__class__, '_acess_attrs'):
            self.__class__.init(self, *args, **kwargs)
            setattr(self.__class__, '_acess_attrs', False)