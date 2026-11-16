
import json
from pathlib import Path


class GolfDataRepository:
    def __init__(self):
        self.filename = (
            Path(__file__).resolve().parent / "rounds.json"
        )

    def saveRound(self, golfRound):
        if not golfRound.validateRound():
            return False

        round_data = {
            "date": golfRound.date,
            "courseName": golfRound.courseName,
            "totalScore": golfRound.calculateTotalScore(),
            "holes": []
        }

        for stats in golfRound.holeStats:
            round_data["holes"].append({
                "holeNumber": stats.hole_number,
                "par": stats.par,
                "strokes": stats.strokes
            })

        rounds = self.getRounds()
        rounds.append(round_data)

        with open(self.filename, "w") as file:
            json.dump(rounds, file, indent=4)

        return True

    def getRounds(self):
        if not self.filename.exists():
            return []

        with open(self.filename, "r") as file:
            return json.load(file)
