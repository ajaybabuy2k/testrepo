import requests

def fetch_commit_details(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        print(f"Error: {response.status_code}")
        return []

def fetch_file_content(file_url):
    response = requests.get(file_url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch file content: {response.status_code}")
        return None