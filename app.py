import requests
import matplotlib.pyplot as plt

# Replace with your GitHub username
username = "mostafa7hmmad"

# API endpoints
followers_url = f"https://api.github.com/users/{username}"
repos_url = f"https://api.github.com/users/{username}/repos"

# Fetch followers count
response = requests.get(followers_url)
followers_count = response.json().get("followers", 0)

# Fetch stars count
response = requests.get(repos_url)
stars_count = sum(repo.get("stargazers_count", 0) for repo in response.json())

# Print counts for verification
print(f"Followers: {followers_count}")
print(f"Stars: {stars_count}")

# Create a bar chart
labels = ["Followers", "Stars"]
values = [followers_count, stars_count]

plt.bar(labels, values, color=["blue", "gold"])
plt.title(f"GitHub Stats for {username}")
plt.ylabel("Count")
plt.savefig("github_stats.png")  # Save the chart as an image
plt.show()
