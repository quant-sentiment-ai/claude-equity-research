"""Offline contract checks for the optional Adanos research input."""

import importlib.util
import io
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlparse

SCRIPT = (
    Path(__file__).resolve().parents[1] / "commands/trading-ideas/scripts/adanos.py"
)
spec = importlib.util.spec_from_file_location("adanos", SCRIPT)
adanos = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adanos)


class AdanosTests(unittest.TestCase):
    def test_all_sources_use_header_and_explicit_dates(self):
        requests = []

        def respond(request, timeout):
            requests.append(request)
            self.assertEqual(timeout, 10)
            return io.BytesIO(b'{"found": true, "sentiment_score": 0.2, "mentions": 4}')

        with patch.object(adanos, "urlopen", side_effect=respond):
            results = {
                source: adanos.fetch(
                    "AAPL", "test-key", "2026-09-01", "2026-09-07", source
                )
                for source in adanos.SOURCES
            }
        self.assertEqual(len(results), 4)
        for source, request in zip(adanos.SOURCES, requests):
            self.assertEqual(
                urlparse(request.full_url).path, f"/{source}/stocks/v1/stock/AAPL"
            )
            self.assertEqual(
                parse_qs(urlparse(request.full_url).query),
                {"from": ["2026-09-01"], "to": ["2026-09-07"]},
            )
            self.assertEqual(request.get_header("X-api-key"), "test-key")
        self.assertNotIn("mentions", results["polymarket"])

    def test_no_data_and_http_error_are_distinct(self):
        with patch.object(
            adanos, "urlopen", return_value=io.BytesIO(b'{"found": false}')
        ):
            self.assertEqual(
                adanos.fetch("AAPL", "key", "2026-09-01", "2026-09-07", "news"),
                {"status": "no data"},
            )
        with patch.object(
            adanos, "urlopen", side_effect=HTTPError("url", 403, "Forbidden", {}, None)
        ):
            self.assertEqual(
                adanos.fetch("AAPL", "key", "2026-09-01", "2026-09-07", "news"),
                {"status": "HTTP 403"},
            )

    def test_main_rejects_invalid_ticker_before_network(self):
        with (
            patch.object(sys, "argv", ["adanos.py", "AAPL;echo key"]),
            patch.dict(adanos.os.environ, {"ADANOS_API_KEY": "test-key"}),
            self.assertRaises(SystemExit),
        ):
            adanos.main()


if __name__ == "__main__":
    unittest.main()
