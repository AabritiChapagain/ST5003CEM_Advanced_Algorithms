import csv
import matplotlib.pyplot as plt

threads = []
speedups = []

with open("task5/thread_benchmark.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        threads.append(int(row["Threads"]))
        speedups.append(float(row["Speedup"]))

plt.figure(figsize=(7, 5))

plt.plot(
    threads,
    speedups,
    marker="o",
    linewidth=2
)

plt.title("Speedup vs Thread Count")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.grid(True)

plt.savefig("graphs/thread_speedup.png")

print("Speedup graph saved to graphs/thread_speedup.png")

plt.show()