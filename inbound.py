import csv
from datetime import datetime
import os
import glob  # Useful for finding files matching a pattern


def clean_and_process_data(input_path, output_path,rejected_path):
    # print(input_path)
    # print(output_path)
    # Check if the specific input file exists
    if not os.path.exists(input_path):
        print(f"Error: Required source file '{input_path}' not found.")
        return

    processed_count = 0
    skipped_count = 0
    # clean_inbound_08142026_time
    print(f"\nStarting pipeline for: {input_path} -> {output_path}")

    # Use the dynamic arguments instead of hardcoded names
    with (open(input_path, mode='r', encoding='utf-8', newline='') as infile, \
            open(output_path, mode='w', encoding='utf-8', newline='') as outfile, \
            open(rejected_path, mode='w', encoding='utf-8', newline='') as rejectedfile):

        # print("print infile")
        # print(outfile)
        reader = csv.DictReader(infile)
        fieldnames = ['user_id', 'email', 'country', 'joined_date', 'status']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        rejected_fieldnames = [
            'user_id',
            'email',
            'country',
            'joined_date',
            'status',
            'error_reason'
        ]

        rejected_writer = csv.DictWriter(
            rejectedfile,
            fieldnames=rejected_fieldnames
        )

        rejected_writer.writeheader()

        for row in reader:
            try:
                email = row.get('email', '').strip().upper()
                country = row.get('country', '').strip().upper()
                    raw_date = row.get('joined_date', '').strip()

                if not email or '@' not in email:
                    raise ValueError(f"Invalid email: '{email}'")

                parsed_date = datetime.strptime(raw_date, "%m/%d/%Y").date()
                formatted_date = parsed_date.strftime("%Y-%m-%d")
                #clean file header
                writer.writerow({
                    'user_id': row['user_id'],
                    'email': email,
                    'country': country if country else 'UNKNOWN',
                    'joined_date': formatted_date,
                    'status': 'ACTIVE'
                })
                processed_count += 1


            except (ValueError, KeyError) as e:
                print(f"[{input_path}] Skipping Row {reader.line_num}: Error -> {e}")
                rejected_writer.writerow({
                    'user_id': row.get('user_id', ''),
                    'email': row.get('email', ''),
                    'country': row.get('country', ''),
                    'joined_date': row.get('joined_date', ''),
                    'status': row.get('status', ''),
                    'error_reason': str(e)
                })

                skipped_count += 1

                continue

    print(f"Finished: {processed_count} processed, {skipped_count} skipped.")


def main():
    print("--- Starting File Processing Suite ---")

    # 1. Look for all raw CSV files in the current folder
    target_files = glob.glob("C:\\Users\\MTS\\Downloads\\inbound.csv")

    # 2. Defensive check if files are missing
    if not target_files:
        print("Error: No data files matching 'raw_*.csv' were found.")
        print("Please place 'raw_us_users.csv' and 'raw_eu_users.csv' in this folder.")
        return

    print(f"Found {len(target_files)} file(s) to clean: {target_files}")
    system_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 3. Dynamically process each discovered file
    for input_file in target_files:
        print(input_file)

        # Swap out 'raw_' prefix for 'cleaned_' prefix
        # need to use an f-string by adding f before the string for printing the system datetime.
        output_file = input_file.replace("C:\\Users\\MTS\\Downloads\\inbound.csv",
                                         f"C:\\Users\\MTS\\Downloads\\cleaned_inbound_{system_datetime}.csv")
        rejected_file = input_file.replace("C:\\Users\\MTS\\Downloads\\inbound.csv",
            f"C:\\Users\\MTS\\Downloads\\rejected_inbound_{system_datetime}.csv")
        print(output_file)

        # Call your dynamic function inside the main loop
        clean_and_process_data(
            input_file,
            output_file,
            rejected_file
        )

    print("\n--- All file operations completed successfully ---")


# Execute the entire application sequentially
main()
