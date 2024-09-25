import argparse
import yaml
import os
from dotenv import load_dotenv

from github_integration import GitHubIntegration
from ai_integration import AIIntegration
from code_analysis import CodeAnalyzer

def load_config(config_path):
    load_dotenv()

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    def replace_env_vars(item):
        if isinstance(item, dict):
            return {k: replace_env_vars(v) for k, v in item.items()}
        elif isinstance(item, list):
            return [replace_env_vars(i) for i in item]
        elif isinstance(item, str) and item.startswith('${') and item.endswith('}'):
            env_var = item[2:-1]
            return os.getenv(env_var, item)
        else:
            return item

    return replace_env_vars(config)

def parse_arguments():
    parser = argparse.ArgumentParser(description='AI-Powered Code Reviewer')
    parser.add_argument('--repo', required=True, help='GitHub repository in format username/repo')
    parser.add_argument('--pr', type=int, required=True, help='Pull request number')
    parser.add_argument('--config', default='config/config.yaml', help='Path to configuration file')
    return parser.parse_args()

def main():
    args = parse_arguments()
    config = load_config(args.config)

    github_integration = GitHubIntegration(config['github']['token'])
    ai_integration = AIIntegration(config['openai']['api_key'])
    code_analyzer = CodeAnalyzer()

    pr = github_integration.get_pull_request(args.repo, args.pr)
    files = github_integration.get_pr_diff(pr)

    full_review = []
    for file in files:
        analysis = code_analyzer.analyze_diff(file.patch)
        ai_review = ai_integration.get_ai_review(file.patch)
        full_review.append(f"File: {file.filename}\nAnalysis: {analysis}\nAI Review: {ai_review}")

    full_review_text = "\n\n".join(full_review)
    github_integration.post_review(pr, full_review_text)

    print("Review completed and posted.")

if __name__ == '__main__':
    main()