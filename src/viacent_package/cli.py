import argparse
from src.viacent_package.count_unique_chars import counter_unique_chars


def process_string(input_string):
    print(f"Processing string: {input_string}")
    unique_count = counter_unique_chars(input_string)
    print(f"Number of unique characters in string: "
          f"{unique_count}")

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Processing file: {file_path}")
            unique_count = counter_unique_chars(content)
            print(f"Number of unique characters in file: "
                  f"{unique_count}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Process a string or a text file.")
    parser.add_argument("--string", type=str,
                        help="String to be processed.")
    parser.add_argument("--file", type=str,
                        help="Path to the text file to be processed.")
    args = parser.parse_args()
    if args.file:
        process_file(args.file)
    elif args.string:
        process_string(args.string)
    else:
        print("Error: You must provide either --string or --file parameter.")

if __name__ == "__main__":
    main()
