import csv
import os
import matplotlib.pyplot as plt

# Create graphs folder if it doesn't exist
os.makedirs("graphs", exist_ok=True)

# Store benchmark data
data = {}

with open("benchmark_results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        structure = row["Structure"]

        if structure not in data:
            data[structure] = {
                "dataset": [],
                "insert": [],
                "search": [],
                "delete": []
            }

        data[structure]["dataset"].append(int(row["Dataset"]))
        data[structure]["insert"].append(float(row["Insert(s)"]))

        # Heap doesn't have search
        if row["Search(s)"] == "-":
            data[structure]["search"].append(None)
        else:
            data[structure]["search"].append(float(row["Search(s)"]))

        data[structure]["delete"].append(float(row["Delete/Extract(s)"]))


# ---------- Insert Graph ----------
plt.figure(figsize=(8,5))

for structure in data:
    plt.plot(
        data[structure]["dataset"],
        data[structure]["insert"],
        marker="o",
        label=structure
    )

plt.title("Insertion Time Comparison")
plt.xlabel("Dataset Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.savefig("graphs/insert_time.png")
plt.close()


# ---------- Search Graph ----------
plt.figure(figsize=(8,5))

for structure in data:
    if structure != "Min Heap":
        plt.plot(
            data[structure]["dataset"],
            data[structure]["search"],
            marker="o",
            label=structure
        )

plt.title("Search Time Comparison")
plt.xlabel("Dataset Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.savefig("graphs/search_time.png")
plt.close()


# ---------- Delete / Extract Graph ----------
plt.figure(figsize=(8,5))

for structure in data:
    plt.plot(
        data[structure]["dataset"],
        data[structure]["delete"],
        marker="o",
        label=structure
    )

plt.title("Delete / Extract-Min Time Comparison")
plt.xlabel("Dataset Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.savefig("graphs/delete_time.png")
plt.close()

print("Graphs generated successfully!")