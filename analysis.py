import pandas as pd

# Read CSV file
data = pd.read_csv("questions.csv")

# Count issues by keyword
refund = data["question"].str.contains("refund", case=False).sum()
return_p = data["question"].str.contains("return", case=False).sum()
order = data["question"].str.contains("order", case=False).sum()
cancel = data["question"].str.contains("cancel", case=False).sum()
delay = data["question"].str.contains("delay|late", case=False).sum()

print("Customer Issue Analysis Results")
print("--------------------------------")
print("Refund Issues:", refund)
print("Return Issues:", return_p)
print("Order Issues:", order)
print("Cancel Issues:", cancel)
print("Delay Issues:", delay)

# Conclusion
print("\nConclusion:")
if refund > return_p and refund > order:
    print("Most customers are facing refund issues.")
elif return_p > refund and return_p > order:
    print("Most customers are facing return issues.")
elif order > refund and order > return_p:
    print("Most customers are asking about order status.")
else:
    print("Customer issues are distributed across multiple categories.")