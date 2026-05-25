import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    stock_score: list[int] = []
    args = sys.argv[1:]
    for arg in args:
        try:
            score = int(arg)
            stock_score.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not stock_score:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")

    else:
        total = len(stock_score)
        total_score = sum(stock_score)
        high = max(stock_score)
        low = min(stock_score)
        average = total_score / total
        range = high - low

        print(f"Scores processed: {stock_score}")
        print(f"Total players: {total}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average}")
        print(f"High score: {high}")
        print(f"Low score: {low}")
        print(f"Score range: {range}")
