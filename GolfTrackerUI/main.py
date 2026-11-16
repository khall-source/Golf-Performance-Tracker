
from datetime import datetime
from RoundService.golf_round import GolfRound
from GolfDataRepository.golf_repository import GolfDataRepository


def recordRound(repository):
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

        try:
            if repository.saveRound(golf_round):
                print("\nGolf round saved successfully!")
            else:
                print("\nError: Could not save round.")
        except (OSError, ValueError) as error:
            print(f"\nError saving round: {error}")
    else:
        print("\nError: Invalid golf round.")


def viewRoundHistory(repository):
    try:
        rounds = repository.getRounds()
    except (OSError, ValueError) as error:
        print(f"\nError loading rounds: {error}")
        return

    if not rounds:
        print("\nNo saved golf rounds found.")
        return

    print("\nGolf Round History")
    print("----------------------------")

    for number, round_data in enumerate(rounds, 1):
        print(f"\nRound {number}")
        print(f"Date: {round_data['date']}")
        print(f"Course: {round_data['courseName']}")
        print(f"Total Score: {round_data['totalScore']}")


def main():
    repository = GolfDataRepository()

    while True:
        print("\n================================")
        print("  Golf Performance Tracker")
        print("================================")
        print("1. Record Golf Round")
        print("2. View Round History")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ")

        if choice == "1":
            recordRound(repository)
        elif choice == "2":
            viewRoundHistory(repository)
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("\nError: Invalid menu option.")


if __name__ == "__main__":
    main()
