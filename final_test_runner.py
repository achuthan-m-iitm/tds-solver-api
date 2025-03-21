
import requests
import json

API_URL = "http://127.0.0.1:8000/api/solve-question"

with open("tds_test_cases.json", "r") as f:
    test_cases = json.load(f)

passed = 0
failed = 0

print("🔍 Running TDS Solver Tests...\n")

for i, case in enumerate(test_cases, 1):
    files = {}
    data = {"question": case["question"]}

    if case["file"]:
        try:
            files["file"] = open(case["file"], "rb")
        except FileNotFoundError:
            print(f"[{i}] ❌ File not found: {case['file']}")
            failed += 1
            continue

    try:
        response = requests.post(API_URL, data=data, files=files)
        result = response.json().get("answer", "")
    except Exception as e:
        print(f"[{i}] ❌ Error during request: {str(e)}")
        failed += 1
        continue

    match = case["expected_contains"].lower() in result.lower()
    status = "✅" if match else "❌"

    print(f"[{i}] {status} Q: {case['question'][:60]}...")
    if not match:
        print(f"    ↪ Expected to contain: {case['expected_contains']}")
        print(f"    ↪ Got: {result[:200]}")

    if match:
        passed += 1
    else:
        failed += 1

print("\n🎯 Test Summary:")
print(f"   ✅ Passed: {passed}")
print(f"   ❌ Failed: {failed}")
print(f"   📦 Total: {len(test_cases)}")
