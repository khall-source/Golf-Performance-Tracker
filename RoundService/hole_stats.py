
class HoleStats:
    def __init__(self, hole_number, par, strokes):
        self.hole_number = hole_number
        self.par = par
        self.strokes = strokes

    def validateStats(self):
        if not 1 <= self.hole_number <= 18:
            return False

        if not 3 <= self.par <= 5:
            return False

        if not 1 <= self.strokes <= 20:
            return False

        return True
