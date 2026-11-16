
import json
from pathlib import Path


class GolfDataRepository:
    def __init__(self):
        self.filePath = Path(__file__).resolve().parent / "rounds.json"

    def getRounds(self):
        if not self.filePath.exists():
            return []

        with open(self.filePath, "r") as file:
            return json.load(file)

    def saveRound(self, golfRound):
        rounds = self.getRounds()

        roundData = {
            "date": golfRound.date,
            "courseName": golfRound.courseName,
            "totalScore": golfRound.calculateTotalScore(),
            "coursePar": golfRound.calculateCoursePar(),
            "scoreToPar": golfRound.calculateScoreToPar(),
            "totalPutts": golfRound.calculateTotalPutts(),
            "greensInRegulation": golfRound.calculateGIR(),
            "fairwaysHit": golfRound.calculateFairwaysHit(),
            "fairwayOpportunities": golfRound.calculateFairwayOpportunities(),
            "holes": []
        }

        for hole in golfRound.holeStats:
            roundData["holes"].append({
                "holeNumber": hole.holeNumber,
                "par": hole.par,
                "strokes": hole.strokes,
                "greenHit": hole.greenHit,
                "fairwayHit": hole.fairwayHit,
                "putts": hole.putts
            })

        rounds.append(roundData)

        with open(self.filePath, "w") as file:
            json.dump(rounds, file, indent=4)

        return True
