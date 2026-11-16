from RoundService.hole_stats import HoleStats

class GolfRound:
    def __init__(self, date, courseName):
        self.date = date
        self.courseName = courseName
        self.holeStats = []

    def addHoleStats(self, holeNumber, par, strokes,
                     greenHit=False, fairwayHit=None, putts=0):
        hole = HoleStats(
            holeNumber, par, strokes,
            greenHit, fairwayHit, putts
        )
        self.holeStats.append(hole)

    def validateRound(self):
        if not self.date or not self.courseName.strip():
            return False

        if len(self.holeStats) != 18:
            return False

        hole_numbers = set()

        for hole in self.holeStats:
            if not hole.validateStats():
                return False

            if hole.holeNumber in hole_numbers:
                return False

            hole_numbers.add(hole.holeNumber)

        return True

    def calculateTotalScore(self):
        return sum(hole.strokes for hole in self.holeStats)

    def calculateCoursePar(self):
        return sum(hole.par for hole in self.holeStats)

    def calculateScoreToPar(self):
        return self.calculateTotalScore() - self.calculateCoursePar()

    def formatScore(self):
        score = self.calculateTotalScore()
        difference = self.calculateScoreToPar()

        if difference == 0:
            return f"{score} (E)"
        elif difference > 0:
            return f"{score} (+{difference})"
        else:
            return f"{score} ({difference})"

    def calculateTotalPutts(self):
        return sum(hole.putts for hole in self.holeStats)

    def calculateGIR(self):
        return sum(1 for hole in self.holeStats if hole.greenHit)

    def calculateFairwaysHit(self):
        return sum(
            1 for hole in self.holeStats
            if hole.fairwayHit is True
        )

    def calculateFairwayOpportunities(self):
        return sum(
            1 for hole in self.holeStats
            if hole.par in (4, 5)
        )