import os
import openai
from github import Github
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GitHubIntegration:
    def __init__(self, token):
        self.github = Github(token)

    def get_pull_request(self, repo_name, pr_number):
        repo = self.github.get_repo(repo_name)
        return repo.get_pull(pr_number)

    def get_pr_diff(self, pull_request):
        return list(pull_request.get_files())

    def post_review(self, pull_request, review_body):
        pull_request.create_review(body=review_body)

class AIIntegration:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.model = "gpt-3.5-turbo"

    def get_ai_review(self, code_diff):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a code reviewer. Analyze the following code diff and provide constructive feedback."},
                {"role": "user", "content": code_diff}
            ]
        )
        return response.choices[0].message['content']

class CodeAnalyzer:
    def analyze_diff(self, diff):
        # This is a simple example. You might want to expand this method
        # to provide more detailed analysis.
        lines_changed = len(diff.split('\n'))
        return f"Analysis of diff: {lines_changed} lines changed"

def main():
    # Load environment variables
    github_token = os.getenv('GITHUB_TOKEN')
    openai_api_key = os.getenv('OPENAI_API_KEY')
    repo_name = os.getenv('REPO_NAME')
    pr_number = int(os.getenv('PR_NUMBER'))

    # Initialize integrations
    github_integration = GitHubIntegration(github_token)
    ai_integration = AIIntegration(openai_api_key)
    code_analyzer = CodeAnalyzer()

    # Get pull request
    pr = github_integration.get_pull_request(repo_name, pr_number)

    # Get PR diff
    pr_files = github_integration.get_pr_diff(pr)

    # Analyze diff and get AI review
    full_diff = "\n".join([f.patch for f in pr_files if f.patch])
    analysis = code_analyzer.analyze_diff(full_diff)
    ai_review = ai_integration.get_ai_review(full_diff)

    # Combine analysis and AI review
    full_review = f"{analysis}\n\nAI Review:\n{ai_review}"

    # Post review
    github_integration.post_review(pr, full_review)

    print("Review posted successfully!")

if __name__ == "__main__":
    main()