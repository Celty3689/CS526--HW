def read_input(filename):
    """Read input from file"""
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])
    men_preferences = {}
    women_preferences = {}

    # Read men preferences (first n lines after count)
    for i in range(1, n + 1):
        parts = lines[i].split()
        man = parts[0]
        preferences = parts[1:]
        men_preferences[man] = preferences

    # Read women preferences (next n lines)
    for i in range(n + 1, 2 * n + 1):
        parts = lines[i].split()
        woman = parts[0]
        preferences = parts[1:]
        women_preferences[woman] = preferences

    return n, men_preferences, women_preferences


def gale_shapley(men_preferences, women_preferences):
    """Implement Gale-Shapley algorithm for stable matching"""
    # Initialize all men as free
    free_men = list(men_preferences.keys())
    women_engaged = {}  # woman: man
    men_next_proposal_index = {man: 0 for man in men_preferences}

    while free_men:
        man = free_men[0]
        woman = men_preferences[man][men_next_proposal_index[man]]

        if woman not in women_engaged:
            # Woman is free, accept proposal
            women_engaged[woman] = man
            free_men.remove(man)
        else:
            # Woman is engaged, check if she prefers new man
            current_man = women_engaged[woman]
            woman_prefs = women_preferences[woman]

            if woman_prefs.index(man) < woman_prefs.index(current_man):
                # Woman prefers new man
                women_engaged[woman] = man
                free_men.remove(man)
                free_men.append(current_man)

        men_next_proposal_index[man] += 1

    return women_engaged


def process_file(input_filename, output_filename):
    """Process a single input file and write output"""
    n, men_preferences, women_preferences = read_input(input_filename)

    # Run Gale-Shapley algorithm
    matches = gale_shapley(men_preferences, women_preferences)

    # Write output file (only final matches)
    with open(output_filename, 'w') as f:
        # Get the original order of men from input file
        men_order = list(men_preferences.keys())

        # Create a reverse mapping: man -> woman
        man_to_woman = {}
        for woman, man in matches.items():
            man_to_woman[man] = woman

        # Write matches in the order of men from input file
        for man in men_order:
            woman = man_to_woman[man]
            f.write(f"{man} - {woman}\n")

    print(f"Output written to: {output_filename}")


def main():
    """Main function to process all input files"""
    input_files = ['marraige_ten.txt', 'marriage_hundred.txt','marraige_thousand.txt']

    for input_file in input_files:
        output_file = input_file.replace('.txt', '_output.txt')
        process_file(input_file, output_file)


if __name__ == "__main__":
    main()