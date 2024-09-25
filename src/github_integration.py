from github import Github

class GitHubIntegration:
    def __init__(self, token):
        self.github = Github(token)

    def get_pull_request(self, repo_name, pr_number):
        repo = self.github.get_repo(repo_name)
        return repo.get_pull(pr_number)

    def get_pr_diff(self, pr):
        return pr.get_files()

    def post_review(self, pr, review_body):
        pr.create_review(body=review_body)