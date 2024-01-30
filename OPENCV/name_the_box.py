
class box_namer:
    switcher = {

    }

    def naming(self,x_max):
        if (x_max-1000).is_around():
           return "Name Boc"

    def is_around(self,real, threshold=5):
        return real <= threshold