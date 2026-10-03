"""Fetch optional, dated Adanos context without exposing the API key."""

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

SOURCES = ("reddit", "x", "news", "polymarket")
BASE_URL = "https://api.adanos.org"


def fetch(ticker, key, start, end, source):
    path = f"/{source}/stocks/v1/stock/{ticker}"
    query = urlencode({"from": start, "to": end})
    request = Request(f"{BASE_URL}{path}?{query}", headers={"X-API-Key": key})
    try:
        with urlopen(request, timeout=10) as response:
            data = json.load(response)
    except HTTPError as error:
        return {"status": f"HTTP {error.code}"}
    except (URLError, TimeoutError, ValueError):
        return {"status": "unavailable"}

    if not isinstance(data, dict) or not isinstance(data.get("found"), bool):
        return {"status": "unexpected response"}
    if not data["found"]:
        return {"status": "no data"}
    count_field = "trade_count" if source == "polymarket" else "mentions"
    return {
        "status": "found",
        **{
            field: data[field]
            for field in (
                "sentiment_score",
                "buzz_score",
                count_field,
                "bullish_pct",
                "bearish_pct",
            )
            if data.get(field) is not None
        },
    }


def main():
    if len(sys.argv) != 2 or not re.fullmatch(
        r"[A-Za-z0-9][A-Za-z0-9.]{0,9}", sys.argv[1]
    ):
        raise SystemExit("Provide one US stock ticker, e.g. AAPL")
    key = os.environ.get("ADANOS_API_KEY", "").strip()
    if not key:
        raise SystemExit("ADANOS_API_KEY is not set")
    ticker = sys.argv[1].upper()
    end = datetime.now(timezone.utc).date()
    start = end - timedelta(days=6)
    print(
        json.dumps(
            {
                "ticker": ticker,
                "from": start.isoformat(),
                "to": end.isoformat(),
                "sources": {
                    source: fetch(
                        ticker, key, start.isoformat(), end.isoformat(), source
                    )
                    for source in SOURCES
                },
            }
        )
    )


if __name__ == "__main__":
    main()
