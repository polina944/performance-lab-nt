import json
import sys

def fill_values(tests, values_map):
    for test in tests:
        if "id" in test and str(test["id"]) in values_map:
            test["value"] = values_map[str(test["id"])]
        if "values" in test:
            test["values"] = fill_values(test["values"], values_map)
    return tests

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python task3.py <values.json> <tests.json> <report.json>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        values_list = json.load(f)
        values_map = {str(v["id"]): v["value"] for v in values_list}

    with open(sys.argv[2]) as f:
        tests_json = json.load(f)

    tests_json["tests"] = fill_values(tests_json["tests"], values_map)

    with open(sys.argv[3], "w") as f:
        json.dump(tests_json, f, indent=4)
