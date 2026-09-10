import sys


def get_scores() -> list[int]:
    scores = []
    index = 1

    while index < len(sys.argv):
        try:
            score = int(sys.argv[index])
            scores.append(score)
        except ValueError:
            print("Invalid parameter: '" + sys.argv[index] + "'")
        index = index + 1

    return scores


def show_usage() -> None:
    print("No scores provided. Usage:", end=" ")
    print("python3 ft_score_analytics.py <score1> <score2> ...")


def show_stats(scores: list[int]) -> None:
    total = sum(scores)
    average = total / len(scores)
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Total score:", total)
    print("Average score:", average)
    print("High score:", high_score)
    print("Low score:", low_score)
    print("Score range:", score_range)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    scores = get_scores()
    if len(scores) == 0:
        show_usage()
    else:
        show_stats(scores)
