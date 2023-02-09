from flask import Flask
from rich import print

from db import get_challenges_for_candidate

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "Hi 👋 head out to " '<a href="/test/999-99-9999">this link</a> to get started.'
    )


@app.route("/test/<ssn>")
def get_challenges(ssn: str):
    print(f"[bold]{'-' * 50}[/bold]")
    print(f"[bold]Passing input:[/bold] [yellow]{ssn}[/yellow]")

    challenges = get_challenges_for_candidate(ssn)
    output = [f"<li>{title}: scored {score}</li>" for title, score in challenges]

    disclaimer = f"""
        <p>Here are the challenges I got for candidate:
            <pre><blockquote>{ssn}</blockquote></pre>
        </p>
    """
    return f"{disclaimer}<br/><h3>Results</h3><ol>{''.join(output)}</ol>"
