import requests
import os

# GitHub username
username = "JuanJoseLobatonMateos"

# GitHub API URL for user repos
url = f"https://api.github.com/users/{username}/repos"

# Send GET request
response = requests.get(url)
repos = response.json()

# Generate markdown for repositories
markdown = ""
for repo in repos:
    if repo['description']:
        description = repo['description']
    else:
        description = "Descripción no disponible"
    markdown += f"- [**{repo['name']}**]({repo['html_url']}): {description}\n"

# Read the current README.md content
readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as file:
    readme_content = file.read()

# Split the content to insert the new markdown
start_marker = "<!--START_SECTION:projects-->"
end_marker = "<!--END_SECTION:projects-->"
before, after = readme_content.split(start_marker)
_, after = after.split(end_marker)

# Combine the content with the new markdown
new_readme_content = f"{before}{start_marker}\n{markdown}{end_marker}{after}"

# Write the updated content back to README.md
with open(readme_path, "w", encoding="utf-8") as file:
    file.write(new_readme_content)
