import pandas as pd
import numpy as np

hours = np.arange(1, 11)
marks = 30 + hours*5 + np.random.randint(-3,3,size=10)

df = pd.DataFrame({"StudyHours":hours, "Marks":marks})
print(df)

print("\nFeature: StudyHours")
print("Label: Marks")
print("Observation: Positive correlation between hours and marks.")
