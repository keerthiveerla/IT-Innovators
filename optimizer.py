def optimize_code(code: str):
    optimized = code

    optimized = optimized.replace("== None", "is None")

    # remove extra blank lines
    lines = optimized.splitlines()
    cleaned = [line.rstrip() for line in lines if line.strip() != ""]
    optimized = "\n".join(cleaned)

    return optimized