import graduates
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
lowest = input("First Major: ")
highest = input("Last Major: ")
list_of_grad_major = graduates.get_majors()
unemployed = []
name = []
for d in list_of_grad_major[4: 12]:
    unemployed.append(d["Employment"]["Status"]["Unemployed"])

for d in list_of_grad_major[4 : 12]:
    name.append(d["Education"]["Major"])


y_pos = np.arange(len(unemployed))

plt.bar(y_pos, unemployed, align='center', alpha=0.5)
plt.xticks(y_pos, name)
plt.ylabel('Graduates')
plt.title('Unemployment of Computer Science Majors Vs 5 Other Majors')

plt.show()
