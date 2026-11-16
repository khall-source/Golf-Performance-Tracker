
from datetime import datetime
from RoundService.golf_round import GolfRound
from GolfDataRepository.golf_repository import GolfDataRepository


def askYesNo(question):
    while True:
        answer = input(question).strip().lower()

        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False

        print("Error: Please enter y or n.")


def formatScore(score, difference):
    if difference == 0:
        return f"{score} (E)"
    elif difference > 0:
        return f"{score} (+{difference})"
    else:
        return f"{score} ({difference})"


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

        if not (3 <= par <= 5 and 1 <= strokes <= 20):
            print("Error: Invalid par or strokes.")
            return

        green_hit = askYesNo("Green in regulation? (y/n): ")

        if par in (4, 5):
            fairway_hit = askYesNo("Fairway hit? (y/n): ")
        else:
            fairway_hit = None

        try:
            putts = int(input("Number of putts: "))
        except ValueError:
            print("Error: Putts must be a whole number.")
            return

        golf_round.addHoleStats(
            hole, par, strokes,
            green_hit, fairway_hit, putts
        )

        if not golf_round.holeStats[-1].validateStats():
            print("Error: Invalid hole statistics.")
            return

    if not golf_round.validateRound():
        print("Error: Invalid golf round.")
        return

    print("\nRound Summary")
    print("----------------------------")
    print(f"Date: {date}")
    print(f"Course: {course}")
    print(f"Course Par: {golf_round.calculateCoursePar()}")
    print(f"Score: {golf_round.formatScore()}")
    print(f"Greens in Regulation: {golf_round.calculateGIR()}/18")
    print(
        f"Fairways Hit: {golf_round.calculateFairwaysHit()}/"
        f"{golf_round.calculateFairwayOpportunities()}"
    )
    print(f"Total Putts: {golf_round.calculateTotalPutts()}")

    try:
        if repository.saveRound(golf_round):
            print("\nGolf round saved successfully!")
        else:
            print("\nError: Could not save round.")
    except (OSError, ValueError) as error:
        print(f"\nError saving round: {error}")


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
        score = round_data["totalScore"]

        # Older rounds may not have coursePar saved.
        course_par = round_data.get("coursePar")

        if course_par is None:
            holes = round_data.get("holes", [])
            if holes:
                course_par = sum(hole["par"] for hole in holes)

        print(f"\nRound {number}")
        print(f"Date: {round_data['date']}")
        print(f"Course: {round_data['courseName']}")

        if course_par is not None:
            print(f"Score: {formatScore(score, score - course_par)}")
        else:
            print(f"Score: {score}")

        if "greensInRegulation" in round_data:
            print(
                f"Greens in Regulation: "
                f"{round_data['greensInRegulation']}/18"
            )

        if "fairwaysHit" in round_data:
            print(
                f"Fairways Hit: {round_data['fairwaysHit']}/"
                f"{round_data['fairwayOpportunities']}"
            )

        if "totalPutts" in round_data:
            print(f"Total Putts: {round_data['totalPutts']}")


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

main()
