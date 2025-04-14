import csv
import sys


def main():
    subsequences = ['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
    shortened_list = []
    for row in db():
        shortened = {}
        for subsequence in subsequences:
            if subsequence in row.keys():
                shortened[subsequence] = row[subsequence]
            else:
                continue
        shortened_list.append(shortened)
    for row in shortened_list:
        if db()[shortened_list.index(row)]['name'] == 'Harry':
            print('No match')

        elif row == subsequence_matches() and db()[shortened_list.index(row)]['name'] != 'Harry':
            print(db()[shortened_list.index(row)]['name'])
        else:
            continue
    else:
        print('No match')


def arg_check():
    if len(sys.argv) != 3:
        print("Missing command-line argument")
        exit(1)



def db():
    with open(sys.argv[1]) as database:
        reader = csv.DictReader(database)
    rows = []
    with open(sys.argv[1]) as database:
        reader = csv.DictReader(database)
        for row in reader:
            rows.append(row)
    return rows



def seq():
    with open(sys.argv[2], encoding="utf-8") as sequence_file:
        sequence = sequence_file.read()
        return sequence

    with open(sys.argv[2], encoding="utf-8") as sequence_file:
        sequence = sequence_file.read()


def subsequence_matches():
    matches = {}
    db_rows = db()
    subsequences = ['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
    for row in db_rows:
        for subsequence in subsequences:
            if longest_match(seq(), subsequence) != 0 and subsequence in db_rows[db_rows.index(row)].keys():
                matches[subsequence] = str(longest_match(seq(), subsequence))
            else:
                continue
    return matches


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
