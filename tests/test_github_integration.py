import pytest
from unittest.mock import Mock, patch
from src.github_integration import GitHubIntegration

@pytest.fixture
def github_integration():
    return GitHubIntegration("dummy_token")

def test_get_pull_request(github_integration):
    with patch('src.github_integration.Github') as mock_github:
        mock_repo = Mock()
        mock_github.return_value.get_repo.return_value = mock_repo
        mock_pr = Mock()
        mock_repo.get_pull.return_value = mock_pr

        pr = github_integration.get_pull_request("test/repo", 1)

        assert pr == mock_pr
        mock_github.return_value.get_repo.assert_called_once_with("test/repo")
        mock_repo.get_pull.assert_called_once_with(1)

def test_get_pr_diff(github_integration):
    mock_pr = Mock()
    mock_files = [Mock(), Mock()]
    mock_pr.get_files.return_value = mock_files

    files = github_integration.get_pr_diff(mock_pr)

    assert files == mock_files
    mock_pr.get_files.assert_called_once()

def test_post_review(github_integration):
    mock_pr = Mock()
    review_body = "Test review"

    github_integration.post_review(mock_pr, review_body)

    mock_pr.create_review.assert_called_once_with(body=review_body)
