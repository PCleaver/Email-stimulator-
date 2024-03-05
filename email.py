class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

Inbox = []

def populate_inbox():
    email1 = Email("sender45@hotmail.com", "Welcome to HyperionDev!", "Great work on the bootcamp!")
    email2 = Email("sender46@outlook.com", "Congratulations!", "Your excellent marks!")
    email3 = Email("sender3@yahoo.com", "Important Announcement", "Please read this message carefully.")
    Inbox.extend([email1, email2, email3])

def list_emails():
    for index, email in enumerate(Inbox):
        print(f"{index} {email.subject_line}")

def read_email(index):
    email = Inbox[index]
    print(f"\nEmail from {email.email_address}\nSubject: {email.subject_line}\n\n{email.email_content}\n")
    email.mark_as_read()
    print(f"Email from {email.email_address} marked as read.\n")

# Populate the initial Inbox with sample emails
populate_inbox()

# Main Program Loop
while True:
    print("Welcome to the Email Simulator!")
    print("Please choose an option:")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        list_emails()
        email_index = int(input("Enter the index of the email you want to read: "))
        read_email(email_index)

    elif choice == "2":
        unread_emails = [email for email in Inbox if not email.has_been_read]
        if unread_emails:
            print("Unread Emails:")
            for email in unread_emails:
                print(email.subject_line)
            print()
        else:
            print("No unread emails.\n")

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid choice. Please try again.\n")
