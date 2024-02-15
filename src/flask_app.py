from flask import Flask
from rich import print

from db import get_challenges_for_candidate

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "Hi 👋 head out to " '<a href="/contest/bob@example.com">this link</a> to get started.'
    )


@app.route("/contest/<email>")
def get_challenges(email: str):
    print(f"[bold]{'-' * 50}[/bold]")
    print(f"[bold]Passing input:[/bold] [yellow]{email}[/yellow]")

    challenges = get_challenges_for_candidate(email)
    output = [f"<li>{title}: scored {score}</li>" for title, score in challenges]

    disclaimer = f"""
        <p>Here are the contest results I got for this person:
            <pre><blockquote>{email}</blockquote></pre>
        </p>
    """
    return f"{disclaimer}<br/><h3>Results</h3><ol>{''.join(output)}</ol>"
