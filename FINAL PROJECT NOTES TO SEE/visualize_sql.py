import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# connect to sqlite database
db_path = "/Users/saa/Documents/BRos_110-02 SJSU/HOMEWORK ASSIGNS/FINAL PROJECT NOTES TO SEE/database_name.db"
conn = sqlite3.connect(db_path)

# query: average salary by region
query_avg_salary = """
SELECT location, AVG(salary_in_usd) AS avg_salary
FROM enhanced_companies
GROUP BY location
ORDER BY avg_salary DESC;
"""
avg_salary_data = pd.read_sql_query(query_avg_salary, conn)

# bar chart: average salary by region
plt.figure(figsize=(12, 6))
sns.barplot(x='avg_salary', y='location', data=avg_salary_data, palette='viridis')
plt.title("average salary by region")
plt.xlabel("average salary (usd)")
plt.ylabel("region")
plt.tight_layout()
plt.savefig("avg_salary_by_region.png")
plt.show()

# query: it roles by region
query_it_roles = """
SELECT location, COUNT(*) AS it_roles
FROM enhanced_companies
WHERE is_it_role = 1
GROUP BY location
ORDER BY it_roles DESC;
"""
it_roles_data = pd.read_sql_query(query_it_roles, conn)

# bar chart: it roles by region
plt.figure(figsize=(12, 6))
sns.barplot(x='it_roles', y='location', data=it_roles_data, palette='coolwarm')
plt.title("it roles by region")
plt.xlabel("number of it roles")
plt.ylabel("region")
plt.tight_layout()
plt.savefig("it_roles_by_region.png")
plt.show()

# close the database connection
conn.close()
