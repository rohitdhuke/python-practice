def extract_substrings(file_path, search_inputs):
    results = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire content of the file
            content = file.read()
            print(content)
            for item in search_inputs:
                if item in content:
                    # Split at the first occurrence of the search input
                    # [1] takes everything after the search input
                    print(f"Lvl 1 {item}")
                    # print(content.split(item, 1)[1])
                    after_input = content.split(item, 1)[1]
                    print(f"after input {after_input}")

                    # .split() without arguments splits by any whitespace
                    # [0] takes the very first word found
                    substring = after_input.split(None, 1)[0]
                    results[item] = substring
                else:
                    results[item] = None  # Or "Not Found"

    except FileNotFoundError:
        print("Error: The file was not found.")

    return results


# --- Example Usage ---
my_file = r'C:\Users\MTS\Downloads\SearchFile_sample.txt'
my_inputs = ['HumanResources', 'Production', 'Sales']

extracted_data = extract_substrings(my_file, my_inputs)

for key, value in extracted_data.items():
    print(f"Search: {key} -> Extracted: {value}")