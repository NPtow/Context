#!/usr/bin/env python3
import argparse
import json
import mimetypes
import os
from pathlib import Path
from typing import Optional
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API_URL = "https://api.deepgram.com/v1/listen"
DEFAULT_QUERY = {
    "model": "nova-3",
    "language": "multi",
    "smart_format": "true",
    "diarize": "true",
    "utterances": "true",
    "paragraphs": "true",
    "punctuate": "true",
}


def load_api_key() -> str:
    env_key = os.getenv("DEEPGRAM_API_KEY")
    if env_key:
        return env_key.strip()

    secret_path = Path("/Users/NIKITA/.codex/skills/meeting-transcriber/.secrets/deepgram.env")
    if secret_path.exists():
        for line in secret_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("DEEPGRAM_API_KEY="):
                return line.split("=", 1)[1].strip()

    raise SystemExit(
        "DEEPGRAM_API_KEY not found. Set env var or create "
        "/Users/NIKITA/.codex/skills/meeting-transcriber/.secrets/deepgram.env"
    )


def parse_args():
    parser = argparse.ArgumentParser(description="Transcribe a recording with Deepgram.")
    parser.add_argument("--input", required=True, help="Absolute path to audio/video file")
    parser.add_argument(
        "--output-dir",
        help="Directory for artifacts. Defaults to <source_dir>/.meeting-transcriber/<basename>/",
    )
    return parser.parse_args()


def build_output_dir(source: Path, explicit_output: Optional[str]) -> Path:
    if explicit_output:
        return Path(explicit_output).expanduser().resolve()
    return source.parent / ".meeting-transcriber" / source.stem


def extract_transcript(payload: dict) -> str:
    utterances = (
        payload.get("results", {})
        .get("utterances", [])
    )
    if utterances:
        lines = []
        for item in utterances:
            speaker = item.get("speaker", "?")
            start = item.get("start")
            end = item.get("end")
            transcript = (item.get("transcript") or "").strip()
            if not transcript:
                continue
            lines.append(f"[Speaker {speaker}] ({start:.2f}-{end:.2f}) {transcript}")
        return "\n".join(lines).strip()

    channels = (
        payload.get("results", {})
        .get("channels", [])
    )
    if channels:
        alts = channels[0].get("alternatives", [])
        if alts:
            return (alts[0].get("transcript") or "").strip()

    return ""


def main():
    args = parse_args()
    source = Path(args.input).expanduser().resolve()
    if not source.exists():
        raise SystemExit(f"Input file does not exist: {source}")

    out_dir = build_output_dir(source, args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    api_key = load_api_key()
    query = urlencode(DEFAULT_QUERY)
    mime_type = mimetypes.guess_type(str(source))[0] or "application/octet-stream"
    data = source.read_bytes()

    req = Request(
        f"{API_URL}?{query}",
        data=data,
        headers={
            "Authorization": f"Token {api_key}",
            "Content-Type": mime_type,
        },
        method="POST",
    )

    with urlopen(req) as response:
        payload = json.loads(response.read().decode("utf-8"))

    raw_path = out_dir / "raw.json"
    utterances_path = out_dir / "utterances.json"
    transcript_path = out_dir / "transcript.txt"

    raw_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    utterances = payload.get("results", {}).get("utterances", [])
    utterances_path.write_text(json.dumps(utterances, ensure_ascii=False, indent=2), encoding="utf-8")

    transcript = extract_transcript(payload)
    transcript_path.write_text(transcript, encoding="utf-8")

    print(json.dumps({
        "source_file": str(source),
        "output_dir": str(out_dir),
        "transcript": str(transcript_path),
        "utterances": str(utterances_path),
        "raw_json": str(raw_path),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
