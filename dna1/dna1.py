import csv
import sys


def main():  # main function checking which person the dna belongs to
    subsequences = ['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
    db_list = db()
    shortened_list = []
    subsequence_match = subsequence_matches()
    names_main = names()
    if 'Alice' in names_main or 'Bob' in names_main or 'Charlie' in names_main:  # differentiation between small and large dbs
        for row in db_list:
            if row['AGATC'] == subsequence_match['AGATC'] and row['AATG'] == subsequence_match['AATG'] and row['TATC'] == subsequence_match['TATC']:
                print(row['name'])
                return
            else:
                continue
        else:
            print('No match')

    elif 'Alice' not in names_main or 'Bob' not in names_main or 'Charlie' not in names_main:
        for row in modify_db():
            shortened = {}
            for subsequence in subsequences:
                if subsequence in row.keys():
                    shortened[subsequence] = row[subsequence]
                else:
                    continue
            shortened_list.append(shortened)
        for row in shortened_list:
            if row != subsequence_match:
                continue
            elif row == subsequence_match:
                print(modify_db()[shortened_list.index(row)]['name'])
                return
            else:
                continue
        else:
            print('No match')
    # else:
        # print('No match')


def arg_check():  # arg_check to be used in main
    if len(sys.argv) != 3:
        print("Missing command-line argument")
        exit(1)


def db():  # extracting db
    with open(sys.argv[1]) as database:
        reader = csv.DictReader(database)
    rows = []
    with open(sys.argv[1]) as database:
        reader = csv.DictReader(database)
        for row in reader:
            rows.append(row)
    return rows


def modify_db():
    sequences = ['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
    db_rows = db()
    for row in db_rows:
        for sequence in sequences:
            row[sequence] = row.get(sequence, '0')
    # print(db_rows)
    return db_rows


def names():
    names = []
    for row in db():
        names.append(row['name'])
    return names


def seq():  # extracting sequence file
    with open(sys.argv[2], encoding="utf-8") as sequence_file:
        sequence = sequence_file.read()
        return sequence

    with open(sys.argv[2], encoding="utf-8") as sequence_file:
        sequence = sequence_file.read()


def subsequence_matches():
    matches = {}
    db_rows = db()
    subsequences = ['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
    for subsequence in subsequences:
        if longest_match(seq(), subsequence) != 0:
            matches[subsequence] = str(longest_match(seq(), subsequence))
        elif longest_match(seq(), subsequence) == 0:
            matches[subsequence] = '0'
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
