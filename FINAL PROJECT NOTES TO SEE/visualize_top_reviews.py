import pandas as pd
import matplotlib.pyplot as plt
import os

# ensure the output directory exists
output_dir = "visualizations"
os.makedirs(output_dir, exist_ok=True)

# load the enhanced dataset
file_path = "enhanced_companies.csv"
data = pd.read_csv(file_path)

# convert reviews from string format (e.g., '9k') to integer values
data['reviews'] = (
    data['reviews']
    .str.replace('k', '000')  # replace 'k' with '000' to convert to thousands
    .str.replace(r'\.', '', regex=True)  # remove any dots
    .astype(int)
)

# extract top 10 companies by reviews
top_reviews_data = data[['company_name', 'reviews']].sort_values(by='reviews', ascending=False).head(10)

# plot the top 10 companies by reviews
plt.figure(figsize=(10, 6))
plt.barh(top_reviews_data['company_name'], top_reviews_data['reviews'], color="orange")
plt.xlabel("number of reviews")
plt.ylabel("company name")
plt.title("top 10 companies by reviews")
plt.tight_layout()

# save the figure as an image
output_file = os.path.join(output_dir, "top_reviews_chart.png")
plt.savefig(output_file)
plt.show()

print(f"top reviews chart saved as {output_file}")
