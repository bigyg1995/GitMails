# GitMails
GitHub Commit Email Extractor



GitHub Commit Email Extractor
This Python script retrieves all unique author emails from the commit history of a selected GitHub repository for a specified user. It uses the GitHub API to list repositories and commits, and then fetches patch data for each commit to extract the "From:" email address.

Features
Lists all repositories for a given GitHub username.

Extracts all unique author emails from commit histories.

Avoids duplicate emails.

Simple interactive CLI for selection.

Prerequisites
Python 3.x

requests library

Install dependencies (if needed):

bash
Copy
Edit
pip install requests
Setup
GitHub Token:
The script requires a GitHub Personal Access Token with at least public repo access.
Replace the GITHUB_TOKEN value in the script with your token.

Clone or Download the Script:
Save the provided script as github_email_extractor.py.

Usage
Run the script:

bash
Copy
Edit
python github_email_extractor.py
Enter the target GitHub username when prompted.

Select the desired repository by entering its number.

The script will print a list of unique commit author emails found in that repository.

Example Output
yaml
Copy
Edit
Enter GitHub username: exampleuser

Available repositories:
0: repo-one
1: repo-two
...

Enter the number of the repository you want to inspect: 0

Selected repository: repo-one

Emails found:
alice@example.com
bob@example.com
Notes
The script checks up to 100 most recent repositories and 100 most recent commits per repository due to GitHub API pagination limits.

For private repositories, the token must have the required permissions.

Excessive API calls may result in rate limiting by GitHub.

License
This project is provided for educational and research purposes.

Let me know if you want to add badges, usage examples, or further customizations.








