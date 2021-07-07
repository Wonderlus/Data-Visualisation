import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [i**2 for i in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)
# Назначение размера шрифта делений на осях
ax.tick_params(axis='both', which='major', labelsize=14)
# Назначение диапазона для каждой оси
ax.axis([0, 1100, 0, 1100000])
# plt.show()
# Сохранение диграммы
plt.savefig('squares_plot2.png')
