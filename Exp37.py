import numpy as np
import matplotlib.pyplot as plt

study = np.array([1,2,3,4,5,6])
score = np.array([50,55,65,70,80,85])

corr = np.corrcoef(study, score)[0,1]
print("Correlation:", corr)

plt.scatter(study, score)
plt.xlabel("Study hours")
plt.ylabel("Score")
plt.title("Study vs Score")
plt.show()
