import graduates
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

list_of_grad_major = graduates.get_majors()
# 4
employed = list_of_grad_major[4]["Employment"]["Status"]["Employed"]
unemployed = list_of_grad_major[4]["Employment"]["Status"]["Unemployed"]
wf = list_of_grad_major[4]["Employment"]["Status"]["Not in Labor Force"]

objects = ('Employed', 'Unemployed', 'Not in the Work Force')
y_pos = np.arange(len(objects))
performance = [employed, unemployed, wf]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Graduates with Computer Science Degree')
plt.title('Employment')

plt.show()

mean = list_of_grad_major[4]["Salaries"]["Mean"]
highest = list_of_grad_major[4]["Salaries"]["Highest"]
lowest = list_of_grad_major[4]["Salaries"]["Lowest"]

objects = ('Highest', 'Average', 'Lowest')
y_pos = np.arange(len(objects))
performance2 = [highest, mean, lowest]

plt.bar(y_pos, performance2, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Dollar Amount')
plt.title('Salaries of Graduates with Computer Science Degree')

plt.show()
