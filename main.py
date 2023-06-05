from github import Github

# First create a Github instance:

# using an access token
g = Github("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")

# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="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")

repoName = "pytest"
source_branch = 'main'
target_branch = 'nuevoparatest'

repo = g.get_user().get_repo(repoName)
sb = repo.get_branch(source_branch)
repo.create_git_ref(ref='refs/heads/' + target_branch, sha=sb.commit.sha)
