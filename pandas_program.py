import pandas as pd

df = pd.read_csv("C:\\Users\\MTS\\Downloads\\employees.csv")
# print(df)
# high_salary = df[df["Salary"] > 80000]
# print(high_salary)
# join_dt = df[df["JoiningDate"]>"2023-01-01"]
# df["JoiningYear"] = df["JoiningDate"].dt.year
#
# print(join_dt)

# print(df["JoiningDate"].dtype)
#
# df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])
#
# # Extract year
# df["JoiningYear"] = df["JoiningDate"].dt.year
#
# # Filter employees who joined after 2023-01-01
# join_dt = df[df["JoiningDate"] > "2023-01-01"]
#
# print(join_dt)
# print(df.isnull())
print(df.isnull().sum())
# print(df.sum(numeric_only=True))
# print(df.sum())
