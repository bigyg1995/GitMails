import requests
import re

GITHUB_TOKEN = ""
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"Error getting repos: {response.status_code} {response.text}")
    repos = response.json()
    if not repos:
        raise Exception("No repositories found for user.")
    return repos

def get_commits(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits?per_page=100"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"Error getting commits: {response.status_code} {response.text}")
    commits = response.json()
    if not commits:
        raise Exception("No commits found in the selected repository.")
    return commits

def extract_email(from_line):
    match = re.search(r"<([^>]+)>", from_line)
    if match:
        return match.group(1)
    return None

def get_from_author_line(username, repo_name, sha):
    patch_url = f"https://github.com/{username}/{repo_name}/commit/{sha}.patch"
    patch_response = requests.get(patch_url)
    if patch_response.status_code != 200:
        return None
    patch_text = patch_response.text
    for line in patch_text.splitlines():
        if line.startswith("From:"):
            return line
    return None

def main():
    username = input("Enter GitHub username: ").strip()
    repos = get_user_repos(username)
    print("\nAvailable repositories:")
    for idx, repo in enumerate(repos):
        print(f"{idx}: {repo['name']}")
    
    repo_choice = input("\nEnter the number of the repository you want to inspect: ").strip()
    if not repo_choice.isdigit() or int(repo_choice) < 0 or int(repo_choice) >= len(repos):
        raise Exception("Invalid repository number selected.")
    repo_choice = int(repo_choice)
    repo_name = repos[repo_choice]['name']
    print(f"\nSelected repository: {repo_name}")

    commits = get_commits(username, repo_name)
    unique_emails = set()
    for commit in commits:
        sha = commit['sha']
        from_author_line = get_from_author_line(username, repo_name, sha)
        if from_author_line:
            email = extract_email(from_author_line)
            if email:
                unique_emails.add(email)

    print("\nEmails found:")
    for email in unique_emails:
        print(email)

if __name__ == "__main__":
    main()
