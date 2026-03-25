import csv
import random

print("AI Customer Support Chatbot")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    # Save question to CSV
    with open("questions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user])

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I assist you today?")

    elif "order" in user:
        print("Bot: Please enter your order ID to check status.")
        order_id = input("Enter Order ID: ")
        print(f"Bot: Order {order_id} is on the way and will arrive soon.")
 
    elif "refund" in user:
        refund_id = random.randint(5000, 9000)
        print("Bot: Your refund request ID is", refund_id, ". Refund will be processed in 5-7 days.")

    elif "return" in user:
        print("Bot: Your return request has been created.")

    elif "cancel" in user:
        print("Bot: Your order has been cancelled.")

    elif "late" in user or "delay" in user:
        print("Bot: Sorry for the delay. Your order will arrive soon.")

    elif "payment" in user:
         print("Bot: Can you confirm if the payment was successful or failed?")

    elif "not received" in user:
         print("Bot: I'm sorry to hear that. Please provide your order ID so I can check.")

    elif "damaged" in user:
        print("Bot: Sorry for the inconvenience. You can request a replacement or return.")

    elif "exchange" in user:
        print("Bot: Exchange option is available under your order section.")

    elif "contact" in user:
         print("Bot: You can contact our support team at support@example.com.")

    elif "thank" in user:
        print("Bot: You're welcome! Is there anything else I can help you with?")

    elif "ok" in user or "okay" in user:
        print("Bot: Alright. Let me know if you need any more help.")

    elif "bye" in user:
        print("Bot: Thank you for contacting support.Have a great day!")
        break

    else:
        print("Bot: I'm sorry, I didn't understand your query.")

