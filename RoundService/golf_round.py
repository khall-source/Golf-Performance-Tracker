
from RoundService.hole_stats import HoleStats


class GolfRound:
    def __init__(self, date, courseName):
        self.date = date
        self.courseName = courseName
        self.holeStats = []

    def addHoleStats(self, hole_number, par, strokes):
        stats = HoleStats(hole_number, par, strokes)
        self.holeStats.append(stats)

    def validateRound(self):
        if not self.date or not self.courseName.strip():
            return False

        if len(self.holeStats) != 18:
            return False

        hole_numbers = []

        for stats in self.holeStats:
            if not stats.validateStats():
                return False

            hole_numbers.append(stats.hole_number)

        if sorted(hole_numbers) != list(range(1, 19)):
            return False

        return True

    def calculateTotalScore(self):
        total = 0

        for stats in self.holeStats:
            total += stats.strokes

        return total
