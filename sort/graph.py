import matplotlib.pyplot as plt

x_values = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
y_values = [
    0.010993719100952148,
    0.020018577575683594,
    0.032997846603393555,
    0.019037485122680664,
    0.023550033569335938,
    0.02600574493408203,
    0.031022071838378906,
    0.03447532653808594,
    0.04099726676940918,
    0.0455470085144043,
]

plt.plot(x_values, y_values, marker='o', linestyle='-', color='r')


plt.xlabel('Array Entries')
plt.ylabel('Time of execution (seconds)')
plt.title('Y Execution Time of X elements in Array')

plt.show()