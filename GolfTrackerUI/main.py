
from datetime import datetime
from RoundService.golf_round import GolfRound
from GolfDataRepository.golf_repository import GolfDataRepository


def main():
    print("================================")
    print("  Golf Performance Tracker")
    print("================================")

    repository = GolfDataRepository()

    print("\nRecord a New Golf Round")

    date = input("Enter date (YYYY-MM-DD): ")
    course = input("Enter golf course name: ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Error: Invalid date. Use YYYY-MM-DD.")
        return

    if not course.strip():
        print("Error: Course name cannot be empty.")
        return

    golf_round = GolfRound(date, course)

    for hole in range(1, 19):
        print(f"\nHole {hole}")

        try:
            par = int(input("Enter par (3-5): "))
            strokes = int(input("Enter strokes (1-20): "))
        except ValueError:
            print("Error: Please enter whole numbers.")
            return

        golf_round.addHoleStats(hole, par, strokes)

        if not golf_round.holeStats[-1].validateStats():
            print("Error: Invalid hole statistics.")
            return

    if golf_round.validateRound():
        total = golf_round.calculateTotalScore()

        print("\nRound Summary")
        print("----------------------------")
        print(f"Date: {date}")
        print(f"Course: {course}")
        print(f"Total Score: {total}")

        if repository.saveRound(golf_round):
            print("\nGolf round saved successfully!")
        else:
            print("\nError: Could not save round.")
    else:
        print("\nError: Invalid golf round.")


if __name__ == "__main__":
    main()
