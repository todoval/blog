import sys
import numpy as np
import matplotlib.pyplot as plt

with open(sys.argv[1], "r") as f:
    rows = []
    for line in f:
        values = line.strip().split(",")

        if values[-1] == "":
            values = values[:-1]

        if "" in values:
            raise ValueError("Error! Corrupted file - null sample found.")

        rows.append([float(x) for x in values])

data = np.array(rows)

spectrum = data[0]

wavelengths = np.arange(380, 380 + len(spectrum))

plt.plot(wavelengths, spectrum)
plt.xlabel("Wavelength (nm)")
plt.ylabel("SPD")
plt.show()