#!/usr/bin/env python3
import sys
import urllib.request
from pathlib import Path

SOURCE_URL = (
    "https://raw.githubusercontent.com/gdydg/cfipcaiji/refs/heads/main/ip.txt"
)


def fetch_ip_lines(url: str, timeout_seconds: int = 30) -> list[str]:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status} when fetching {url}")
        raw_text = response.read().decode("utf-8", errors="ignore")

    # Normalize lines: strip, drop comments and blanks
    lines = [line.strip() for line in raw_text.splitlines()]
    return [line for line in lines if line and not line.startswith("#")]


def take_first_five(items: list[str]) -> list[str]:
    return items[:5]


def take_middle_five(items: list[str]) -> list[str]:
    if len(items) <= 5:
        return items.copy()
    start_index = (len(items) - 5) // 2  # left-biased center for even lengths
    end_index = start_index + 5
    return items[start_index:end_index]


def take_last_five(items: list[str]) -> list[str]:
    if len(items) <= 5:
        return items.copy()
    return items[-5:]


def write_lines(filepath: Path, lines: list[str]) -> None:
    # Always end file with newline for POSIX friendliness
    text = ("\n".join(lines) + "\n") if lines else ""
    filepath.write_text(text, encoding="utf-8")


def main() -> int:
    try:
        ips = fetch_ip_lines(SOURCE_URL)
    except Exception as exc:
        print(f"Failed to fetch ip.txt: {exc}", file=sys.stderr)
        return 1

    project_root = Path(__file__).resolve().parent

    mobile = take_first_five(ips)
    unicom = take_middle_five(ips)
    telecom = take_last_five(ips)

    write_lines(project_root / "移动.txt", mobile)
    write_lines(project_root / "联通.txt", unicom)
    write_lines(project_root / "电信.txt", telecom)

    print(
        f"Total: {len(ips)} | 移动: {len(mobile)} | 联通: {len(unicom)} | 电信: {len(telecom)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())