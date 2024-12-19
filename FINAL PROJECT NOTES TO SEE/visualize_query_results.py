import pandas as pd
import matplotlib.pyplot as plt

# === visualization: average ratings ===
avg_rating_data = pd.read_csv("avg_rating.csv", names=["company_name", "average_rating"])
plt.figure(figsize=(10, 6))
plt.barh(avg_rating_data["company_name"], avg_rating_data["average_rating"], color="skyblue")
plt.title("top 10 companies by average rating")
plt.xlabel("average rating")
plt.ylabel("company name")
plt.tight_layout()
plt.savefig("avg_rating_chart.png")
plt.show()

# === visualization: top reviews ===
top_reviews_data = pd.read_csv("top_reviews.csv", names=["company_name", "reviews"])
# convert 'reviews' to numeric (e.g., '9k' -> 9000)
top_reviews_data["reviews"] = top_reviews_data["reviews"].str.replace('k', '000').astype(int)
plt.figure(figsize=(10, 6))
plt.barh(top_reviews_data["company_name"], top_reviews_data["reviews"], color="orange")
plt.title("top 10 companies by reviews")
plt.xlabel("number of reviews")
plt.ylabel("company name")
plt.tight_layout()
plt.savefig("top_reviews_chart.png")
plt.show()


