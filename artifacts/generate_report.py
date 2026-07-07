import json
from datetime import datetime

report = {
    "test_run": "unit-tests",
    "timestamp": datetime.utcnow().isoformat(),
    "total_tests": 12,
    "passed": 11,
    "failed": 1,
    "failed_test": "test_payment_gateway_timeout"
}

with open("artifacts/test-report.json", "w") as f:
    json.dump(report, f, indent=2)

with open("artifacts/build.log", "w") as f:
    f.write("Build started\nCompiling modules...\nBuild completed with 1 test failure\n")

print("Generated test-report.json and build.log")
