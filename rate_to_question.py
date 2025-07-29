def rate_to_question(question: str, answer: str, prompt: str, client) -> str:
    """
    Use OpenAI chat completion to rate the answer to a question.

    Parameters:
        question (str): The question text.
        answer (str): The answer text.
        prompt (str): The prompt text to guide the model.
        client: The OpenAI client instance.

    Returns:
        str: The model's response.
    """
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"{prompt} {question} {answer}"}],
            temperature=0.2
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return ""

