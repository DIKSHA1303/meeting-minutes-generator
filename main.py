
import re
import argparse
from pathlib import Path


def read_transcript(file_path):
    """Read the meeting transcript from a text file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Transcript not found: {file_path}")

    return path.read_text(encoding="utf-8")


def extract_speaker_statements(transcript):
    """Extract statements written in Speaker: message format."""
    statements = []

    for line in transcript.splitlines():
        match = re.match(r"^\s*([^:]+):\s*(.+)$", line)

        if match:
            speaker = match.group(1).strip()
            message = match.group(2).strip()
            statements.append((speaker, message))

    return statements


def generate_summary(statements):
    """Create a simple summary from the transcript."""
    if not statements:
        return ["No speaker statements were identified."]

    summary = []

    for speaker, message in statements[:5]:
        summary.append(f"- {speaker} discussed: {message}")

    return summary


def extract_decisions(statements):
    """Identify statements containing decision-related keywords."""
    keywords = [
        "decided", "agreed", "approved",
        "confirmed", "finalized", "selected"
    ]

    decisions = []

    for speaker, message in statements:
        if any(word in message.lower() for word in keywords):
            decisions.append(f"- {speaker}: {message}")

    return decisions


def extract_action_items(statements):
    """Identify possible action items and their owners."""
    action_keywords = [
        "will", "must", "need to", "should",
        "responsible for", "has to"
    ]

    action_items = []

    for speaker, message in statements:
        lower_message = message.lower()

        if any(keyword in lower_message for keyword in action_keywords):
            action_items.append(
                f"- **{speaker}**: {message}"
            )

    return action_items


def generate_minutes(transcript):
    """Generate structured meeting minutes."""
    statements = extract_speaker_statements(transcript)

    summary = generate_summary(statements)
    decisions = extract_decisions(statements)
    actions = extract_action_items(statements)

    content = [
        "# Meeting Minutes",
        "",
        "## 1. Summary",
        *summary,
        "",
        "## 2. Decisions",
    ]

    content.extend(
        decisions if decisions else ["- No decisions detected."]
    )

    content.extend([
        "",
        "## 3. Action Items",
    ])

    content.extend(
        actions if actions else ["- No possible action items detected."]
    )

    content.extend([
        "",
        "## 4. Review Notes",
        "- This version uses rule-based extraction.",
        "- Decisions and action items must be verified against the original transcript.",
        "- Detected action items are suggestions, not confirmed assignments.",
        "- Deadlines and speaker identities are not independently verified.",
        "",
        "---",
        "*Generated using the Meeting Minutes Generator.*"
    ])

    return "\n".join(content)


def main():
    parser = argparse.ArgumentParser(
        description="Generate structured meeting minutes from a text transcript."
    )

    parser.add_argument(
        "input",
        help="Path to the meeting transcript (.txt)"
    )

    parser.add_argument(
        "-o", "--output",
        default="meeting_minutes.md",
        help="Output Markdown file"
    )

    args = parser.parse_args()

    try:
        transcript = read_transcript(args.input)

        minutes = generate_minutes(transcript)

        Path(args.output).write_text(
            minutes,
            encoding="utf-8"
        )

        print("Meeting minutes generated successfully!")
        print(f"Output saved to: {args.output}")

    except (FileNotFoundError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
