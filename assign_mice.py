def assign_mice_to_holes(mice, holes):
    """
    Assign mice to holes using a greedy strategy.
    Returns the minimum possible maximum time.
    """

    mice.sort()
    holes.sort()

    maximum_time = 0

    print("Assignments:")

    for mouse, hole in zip(mice, holes):
        time = abs(mouse - hole)

        print(f"Mouse at {mouse} -> Hole at {hole} : {time}")

        if time > maximum_time:
            maximum_time = time

    return maximum_time


if __name__ == "__main__":

    mice = [4, -4, 2]
    holes = [4, 0, 5]

    result = assign_mice_to_holes(mice, holes)

    print("\nMinimum maximum time =", result)