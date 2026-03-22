from main import analyze

def test_successrate():

    success, fail = analyze("data1.csv")
    total = success + fail
    rate = success / total if total > 0 else 0

    assert rate >= 0.8