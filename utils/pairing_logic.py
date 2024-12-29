def calculate_compatibility(student1, student2, threshold=20):
    """
    Calculate a compatibility score between two students based on their attributes.
    Args:
        student1 (dict): A dictionary containing the attributes of the first student.
        student2 (dict): A dictionary containing the attributes of the second student.
        threshold (int): Minimum compatibility score for pairing (default is 20).
    Returns:
        int: A compatibility score (higher is better), or -1 if below the threshold or invalid pair.
    """
    # Gender constraint: Male and female cannot be paired
    if student1['Gender'] != student2['Gender']:
        print(f"\nCannot pair {student1['Student ID']} (Gender: {student1['Gender']}) "
              f"with {student2['Student ID']} (Gender: {student2['Gender']}) -> Gender mismatch.")
        return -1

    score = 0
    print(f"\nCalculating compatibility between {student1['Student ID']} and {student2['Student ID']}:")
    
    # Compare personality metrics
    personality1 = student1.get('Personality Metrics', {})
    personality2 = student2.get('Personality Metrics', {})
    for key in personality1.keys():
        if key in personality2:
            diff = abs(personality1[key] - personality2[key])
            increment = max(0, 10 - diff)
            score += increment
            print(f"    {key}: {personality1[key]} vs {personality2[key]} -> +{increment}")

    # Match based on religion
    if student1['Religion'] == student2['Religion']:
        score += 10
        print(f"    Religion Match -> +10")

    print(f"    Final Score: {score}")

    # Return -1 if score is below the threshold
    return score if score >= threshold else -1


def generate_pairings(students, threshold=20):
    """
    Generate the best roommate pairings for a list of students.
    Args:
        students (list): A list of dictionaries, where each dictionary represents a student.
        threshold (int): Minimum compatibility score for pairing (default is 20).
    Returns:
        list of tuples: A list of pairs, where each pair is a tuple of student IDs.
    """
    pairings = []
    unpaired_students = students[:]

    while len(unpaired_students) > 1:
        best_score = -1
        best_pair = None

        # Find the best pairing
        for i in range(len(unpaired_students)):
            for j in range(i + 1, len(unpaired_students)):
                student1 = unpaired_students[i]
                student2 = unpaired_students[j]
                score = calculate_compatibility(student1, student2, threshold)
                print(f"    Score between {student1['Student ID']} and {student2['Student ID']}: {score}")
                if score > best_score:
                    best_score = score
                    best_pair = (student1, student2)

        # Assign the best pair
        if best_pair and best_score >= threshold:
            pairings.append((best_pair[0]['Student ID'], best_pair[1]['Student ID']))
            print(f"Paired: {best_pair[0]['Student ID']} with {best_pair[1]['Student ID']}")
            unpaired_students.remove(best_pair[0])
            unpaired_students.remove(best_pair[1])
        else:
            print(f"No valid pair found with a score >= {threshold}.")
            break

    # Handle any leftover student (odd number of students)
    if len(unpaired_students) == 1:
        print(f"Unpaired: {unpaired_students[0]['Student ID']}")
        pairings.append((unpaired_students[0]['Student ID'], None))

    return pairings
