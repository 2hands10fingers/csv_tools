class _(str):
    """ Turns any string into object type """

    def set(self):
        return set(list(self))
    
    def dict(self):
        return {k:None for k in self}
    
    def list(self):
        return list(self)
              
    def tuple(self):
        return tuple([i for i in self])
    
    def lprint(self):
        for i in self: print(i)
    
    def sort(self):
        return sorted(self)
