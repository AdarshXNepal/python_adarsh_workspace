''' Spam Comment Detector '''

spam_count = 0
clean_count = 0

# 🔢 Ask how many comments you want to check
count = int(input("How many comments do you want to check? "))

# 🚫 Spam keywords
spam_phrases = ["buy now", "subscribe", "click this", "make money", "visit here"]

for i in range(count):
    comment = input("Enter your comment: ")
    comment = comment.lower()

    # Check if any spam phrase is in the comment
    if any(phrase in comment for phrase in spam_phrases):
        print("⚠️ Spam detected! Your comment may be flagged.")
        spam_count += 1
    else:
        print("✅ Thank you for your clean comment.")
        clean_count += 1

# 📊 Summary
print("\n------ Summary ------")
print("Total Comments Checked:", count)
print("Spam Comments:", spam_count)
print("Clean Comments:", clean_count)
