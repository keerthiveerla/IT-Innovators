from reviewer import review_code
from optimizer import optimize_code

code = input("Paste your code:\n")

issues = review_code(code)
optimized_code = optimize_code(code)

print("\nIssues Found:")
for issue in issues:
    print("-", issue)

print("\nOptimized Code:")
print(optimized_code)