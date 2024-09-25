from src.code_analysis import CodeAnalyzer

def test_analyze_diff():
    analyzer = CodeAnalyzer()
    diff = "Sample diff\nwith multiple\nlines"

    analysis = analyzer.analyze_diff(diff)

    assert analysis == "Analysis of diff: 3 lines changed"