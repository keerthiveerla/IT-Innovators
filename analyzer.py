def analyze_code(code: str):
    lines = code.splitlines()
    score = 100

    if "print(" in code:
        score -= 10
    if "== None" in code:
        score -= 10
    if len(lines) > 50:
        score -= 10

    return {
        "lines": len(lines),
        "score": max(score, 0)
    }