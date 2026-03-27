import pandas as pd

data = pd.read_csv("questions.csv")

refund = data["question"].str.contains("refund", case=False).sum()
return_p = data["question"].str.contains("return", case=False).sum()
order = data["question"].str.contains("order", case=False).sum()
cancel = data["question"].str.contains("cancel", case=False).sum()
delay = data["question"].str.contains("delay|late", case=False).sum()
payment = data["question"].str.contains("payment", case=False).sum()

print("Customer Issue Analysis Results")
print("--------------------------------")
print("Refund Issues:", refund)
print("Return Issues:", return_p)
print("Order Issues:", order)
print("Cancel Issues:", cancel)
print("Delay Issues:", delay)
print("Payment Issues:", payment)

print("\nConclusion:")
issues = {
    "Refund": refund,
    "Return": return_p,
    "Order": order,
    "Cancel": cancel,
    "Delay": delay,
    "Payment": payment
}

max_issue = max(issues, key=issues.get)
print("Most common customer issue is:", max_issue)
print("This issue should be prioritized for automation in chatbot system.")