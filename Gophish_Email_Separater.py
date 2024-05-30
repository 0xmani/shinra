import csv
import os

# Function to split emails into batches and write to CSV files
def split_emails_to_csv(input_file, batch_size=50):
    with open(input_file, 'r') as infile:
        emails = [line.strip() for line in infile]
        num_emails = len(emails)
        num_batches = (num_emails + batch_size - 1) // batch_size

        # Create a directory to store CSV files
        if not os.path.exists('email_batches'):
            os.makedirs('email_batches')

        # Write each batch of emails to a separate CSV file
        for i in range(num_batches):
            start_idx = i * batch_size
            end_idx = min((i + 1) * batch_size, num_emails)
            batch_emails = emails[start_idx:end_idx]

            output_file = f'email_batches/batch_{i+1}.csv'
            with open(output_file, 'w', newline='') as outfile:
                fieldnames = ['First Name', 'Last Name', 'Email', 'Position']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                for email in batch_emails:
                    writer.writerow({'First Name': '', 'Last Name': '', 'Email': email, 'Position': ''})

# Example usage
split_emails_to_csv('inputs.txt')
