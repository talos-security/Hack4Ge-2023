from flask import Flask
from rich import print

from db import get_challenges_for_candidate, get_challenges_for_candidate_2, get_challenges_for_candidate_3, get_challenges_for_candidate_4

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "Hi 👋 head out to "
        '<a href="/challenges/111.111.111-11">this link (chall 1)</a> to get started.<br>'
        '<a href="/challenges2/111.111.111-11">this link (chall 2)</a> to get started.<br>'
        '<a href="/challenges3/111.111.111-11">this link (chall 3) </a> to get started.<br>'
        '<a href="/challenge4/111.111.111-11">this link (chall 4)</a> to get started.<br>'

    )




@app.route("/challenges4/<cpf>")
def get_challenges_4(cpf: str):
    print(f"[bold]{'-' * 50}[/bold]")
    print(f"[bold]Passing input:[/bold] [yellow]{cpf}[/yellow]")

    challenges = get_challenges_for_candidate_4(cpf)
    output = [f"<li>{title}: scored {score}</li>" for title, score in challenges]

    disclaimer = f"""
        <p>Here are the challenges I got for candidate:
            <pre><blockquote>{cpf}</blockquote></pre>
        </p>
    """
    return f"{disclaimer}<br/><h3>Results</h3><ol>{''.join(output)}</ol>"



@app.route("/challenges3/<cpf>")
def get_challenges_3(cpf: str):
    print(f"[bold]{'-' * 50}[/bold]")
    print(f"[bold]Passing input:[/bold] [yellow]{cpf}[/yellow]")

    challenges = get_challenges_for_candidate_3(cpf)
    output = [f"<li>{title}: scored {score}</li>" for title, score in challenges]

    disclaimer = f"""
        <p>Here are the challenges I got for candidate:
            <pre><blockquote>{cpf}</blockquote></pre>
        </p>
    """
    return f"{disclaimer}<br/><h3>Results</h3><ol>{''.join(output)}</ol>"




@app.route("/challenges2/<cpf>")
def get_challenges_2(cpf: str):
    print(f"[bold]{'-' * 50}[/bold]")
    print(f"[bold]Passing input:[/bold] [yellow]{cpf}[/yellow]")

    challenges = get_challenges_for_candidate_2(cpf)
    output = [f"<li>{title}: scored {score}</li>" for title, score in challenges]

    disclaimer = f"""
        <p>Here are the challenges I got for candidate:
            <pre><blockquote>{cpf}</blockquote></pre>
        </p>
    """
    return f"{disclaimer}<br/><h3>Results</h3><ol>{''.join(output)}</ol>"


@app.route("/challenges/<cpf>")
def get_challenges(cpf: str):
    print(f"[bold]{'-' * 50}[/bold]")
    print(f"[bold]Passing input:[/bold] [yellow]{cpf}[/yellow]")

    challenges = get_challenges_for_candidate(cpf)
    output = [f"<li>{title}: scored {score}</li>" for title, score in challenges]

    disclaimer = f"""
        <p>Here are the challenges I got for candidate:
            <pre><blockquote>{cpf}</blockquote></pre>
        </p>
    """
    return f"{disclaimer}<br/><h3>Results</h3><ol>{''.join(output)}</ol>"
