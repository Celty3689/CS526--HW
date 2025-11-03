def check_snowfall():
    """Process all snowfall_input files."""
    for i in range(1, 6):
        filename = f"snowfall_input{i}.txt"
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                n = int(lines[0].strip())
                cumulative_snowfall = list(map(int, lines[1].strip().split()))

                # Calculate the daily snowfall.
                daily_snowfall = [cumulative_snowfall[0]]
                for j in range(1, n):
                    daily_snowfall.append(cumulative_snowfall[j] - cumulative_snowfall[j-1])

                # Calculate the total snowfall.
                total_snowfall = cumulative_snowfall[-1]

                # Check all three-day consecutive windows.
                result = "NO"
                for k in range(n - 2):
                    three_day_total = daily_snowfall[k] + daily_snowfall[k+1] + daily_snowfall[k+2]
                    if three_day_total > total_snowfall / 2:
                        result = "YES"
                        break

                # Print out the result
                print(f"{filename}: {result}")

        except FileNotFoundError:
            print(f"{filename}: File not found")
        except Exception as e:
            print(f"{filename}: Error processing file")

if __name__ == "__main__":
    check_snowfall()