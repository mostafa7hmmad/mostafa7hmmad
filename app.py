import requests
import plotly.graph_objects as go

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

# Prepare data
labels = ["Followers", "Stars"]
values = [followers_count, stars_count]

# Create interactive chart
fig = go.Figure(data=[go.Bar(x=labels, y=values, marker=dict(color=['blue', 'gold']))])
fig.update_layout(
    title=f"GitHub Stats for {username}",
    xaxis_title="Category",
    yaxis_title="Count",
    template="plotly_dark",
)

# Save as an HTML file
fig.write_html("github_stats.html")
print("Interactive chart saved as github_stats.html")
