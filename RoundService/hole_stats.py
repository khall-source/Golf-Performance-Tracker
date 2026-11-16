
class HoleStats:
    def __init__(self, hole_number, par, strokes,
                 green_hit=False, fairway_hit=None, putts=0):
        self.holeNumber = hole_number
        self.par = par
        self.strokes = strokes
        self.greenHit = green_hit
        self.fairwayHit = fairway_hit
        self.putts = putts

    def validateStats(self):
        if not 1 <= self.holeNumber <= 18:
            return False

        if not 3 <= self.par <= 5:
            return False

        if not 1 <= self.strokes <= 20:
            return False

        if not isinstance(self.greenHit, bool):
            return False

        if self.par == 3:
            if self.fairwayHit is not None:
                return False
        elif not isinstance(self.fairwayHit, bool):
            return False

        if not isinstance(self.putts, int) or isinstance(self.putts, bool):
            return False

        if not 0 <= self.putts <= self.strokes:
            return False

        return True
