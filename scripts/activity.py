from datetime import datetime

with open("logs/activity.md","a",encoding="utf-8") as f:
    f.write(
        f"\n## Automated activity\n"
        f"Time: {datetime.now()}\n"
        f"Status: GitHub Actions running\n"
    )
