import openai

class AIIntegration:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        openai.api_key = api_key
        self.model = model

    def get_ai_review(self, code_diff):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a code reviewer. Analyze the following code diff and provide constructive feedback."},
                {"role": "user", "content": code_diff}
            ]
        )
        return response.choices[0].message['content']