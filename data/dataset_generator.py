import random
import csv

def generate_dataset(size, filename):
    """Generate a dataset of random cities and save it as a CSV file."""

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        # Header row
        writer.writerow(["Name", "X", "Y", "Population", "Distance"])

        for i in range(size):
            name = f"City{i+1}"
            x = round(random.uniform(-180, 180), 2)
            y = round(random.uniform(-90, 90), 2)
            population = random.randint(1000, 1000000)
            distance = round(random.uniform(1, 1000), 2)

            writer.writerow([name, x, y, population, distance])

    print(f"{filename} created with {size} cities.")


if __name__ == "__main__":
    generate_dataset(100, "cities_100.csv")
    generate_dataset(1000, "cities_1000.csv")
    generate_dataset(10000, "cities_10000.csv")