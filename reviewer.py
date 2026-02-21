def review_code(code: str):
    issues = []

    if "print(" in code:
        issues.append("Debug print statements detected")

    if "== None" in code:
        issues.append("Use 'is None' instead of '== None'")

    if "\t" in code:
        issues.append("Avoid tabs, use 4 spaces for indentation")

    if len(code.splitlines()) > 50:
        issues.append("File is too long, consider breaking into functions")

    return issues