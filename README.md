# GitMails
**GitHub Commit Email Extractor**


This Python script retrieves all unique author emails from the commit history of a selected GitHub repository for a specified user.
It uses the GitHub API to list repositories and commits, and then fetches patch data for each commit to extract the "From:" email address.

#**Features**

Lists all repositories for a given GitHub username.

Extracts all unique author emails from commit histories.

Avoids duplicate emails.

#**Requirements**

**GitHub Token**:The script requires a GitHub Personal Access Token with at least public repo access.

Replace the GITHUB_TOKEN value in the script with your token.
