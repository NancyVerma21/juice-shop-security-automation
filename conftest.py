from pathlib import Path
import os

import pytest
from dotenv import load_dotenv


load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")

SCREENSHOTS_DIR = Path("screenshots")
TRACES_DIR = Path("traces")

SCREENSHOTS_DIR.mkdir(exist_ok=True)
TRACES_DIR.mkdir(exist_ok=True)


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(autouse=True)
def capture_failure_artifacts(request):
    if request.node.get_closest_marker("ui") is None:
        yield
        return

    page = request.getfixturevalue("page")

    page.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    yield

    report = getattr(request.node, "rep_call", None)

    if report and report.failed:
        test_name = request.node.name

        screenshot_path = SCREENSHOTS_DIR / f"{test_name}.png"
        trace_path = TRACES_DIR / f"{test_name}.zip"

        page.screenshot(
            path=str(screenshot_path),
            full_page=True,
        )

        page.context.tracing.stop(path=str(trace_path))
    else:
        page.context.tracing.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)
