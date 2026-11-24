import os
import unittest


def run_test_summary(test_dir="tests"):
    loader = unittest.TestLoader()

    test_files = sorted(
        f for f in os.listdir(test_dir) if f.startswith("test_") and f.endswith(".py")
    )

    count_passed = 0
    count_total = 0
    for filename in test_files:
        module_name = filename[:-3]
        suite = loader.discover(start_dir=test_dir, pattern=filename)

        result = unittest.TestResult()
        suite.run(result)

        total = result.testsRun
        failed = len(result.failures) + len(result.errors)
        passed = total - failed


        count_passed += passed
        count_total += total

        print(f"{module_name} - {passed}/{total}")
        for i in result.failures:
            print(i[0])
            print(i[1])
        for i in result.errors:
            print(i[0])
            print(i[1])
        print('\n\n\n')

    print(f"All tests - {count_passed}/{count_total}")


if __name__ == "__main__":
    run_test_summary()