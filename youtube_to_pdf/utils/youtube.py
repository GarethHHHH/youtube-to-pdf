import re
from urllib.parse import unquote

import requests


_VIDEO_ID_RE = re.compile(r"(?:v=|/)([0-9A-Za-z_-]{11})")


def clean_url(value: str) -> str:
    """Return a normalized long-form YouTube watch URL."""
    value = unquote(value)
    match = _VIDEO_ID_RE.search(value)
    if not match:
        raise ValueError("Invalid YouTube URL")
    video_id = match.group(1)
    return f"https://www.youtube.com/watch?v={video_id}"


def validate(value: str) -> str:
    """Validate the URL and return a cleaned version."""
    cleaned = clean_url(value)
    try:
        response = requests.head(cleaned, timeout=2)
        if response.status_code != 405:
            response.raise_for_status()
    except requests.exceptions.ConnectionError as exc:
        raise ValueError("Provided value is not an URL or connection error") from exc
    except requests.RequestException as exc:
        raise ValueError("Could not perform a successful request with the provided URL") from exc
    return cleaned
