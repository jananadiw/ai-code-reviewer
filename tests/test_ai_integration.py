import pytest
from unittest.mock import patch
from src.ai_integration import AIIntegration

@pytest.fixture
def ai_integration():
    return AIIntegration("dummy_api_key")

def test_get_ai_review(ai_integration):
    with patch('src.ai_integration.openai.ChatCompletion.create') as mock_create:
        mock_create.return_value.choices[0].message = {'content': 'AI review content'}
        code_diff = "Sample code diff"

        review = ai_integration.get_ai_review(code_diff)

        assert review == 'AI review content'
        mock_create.assert_called_once_with(
            model=ai_integration.model,
            messages=[
                {"role": "system", "content": "You are a code reviewer. Analyze the following code diff and provide constructive feedback."},
                {"role": "user", "content": code_diff}
            ]
        )