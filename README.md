# AI-Powered Code Reviewer

This project is an automated code review tool that leverages AI to provide insightful feedback on GitHub pull requests. It combines GitHub integration, AI-powered analysis, and basic code metrics to offer comprehensive code reviews.

## Features

- Automatic pull request analysis
- AI-generated code review comments
- Basic code metrics
- Configurable settings via YAML file
- Environment variable support for sensitive data

## Prerequisites

- Python 3.7 or higher
- GitHub account and personal access token
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-powered-code-reviewer.git
   cd ai-powered-code-reviewer
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   Create a `.env` file in the project root and add your GitHub and OpenAI API keys:
   ```
   GITHUB_TOKEN=your_github_token
   OPENAI_API_KEY=your_open
  
## Configuration
The project uses a YAML configuration file located at config/config.yaml. You can customize various settings here, including:
```yaml
github:
  token: ${GITHUB_TOKEN}

openai:
  api_key: ${OPENAI_API_KEY}

review:
  max_files: 5
  file_extensions:
    - .py
    - .js
    - .ts

ai:
  model: gpt-3.5-turbo
  temperature: 0.7
  max_tokens: 500

prompts:
  code_review: |
    You are a code reviewer. Analyze the following code diff and provide constructive feedback:
    
    {code_diff}
    
    Focus on:
      1. Code quality
      2. Potential bugs
      3. Performance issues
      4. Best practices
```

## Usage
Run the code reviewer with the following command:
```
python src/main.py --repo username/repository --pr pull_request_number
```

Optional arguments:
- --config: Specify a custom configuration file path (default: `config/config.yaml`)

## Project Structure
- `src/`: Contains the main source code
  - `main.py`: Entry point of the application
  - `github_integration.py`: Handles GitHub API interactions
  - `ai_integration.py`: Manages AI-powered code review
  - `code_analysis.py`: Performs basic code analysis
- `tests/`: Contains unit tests
- `config/`: Holds configuration files

## Testing

To run the tests, use the following command:
```
pytest tests/
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
