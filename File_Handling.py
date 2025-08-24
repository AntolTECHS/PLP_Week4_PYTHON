def modify_content(text: str) -> str:
    """
    Modify the content of the file.
    For demo: convert text to uppercase and add line numbers.
    """
    lines = text.splitlines()
    modified = [f"{i+1}: {line.upper()}" for i, line in enumerate(lines)]
    return "\n".join(modified)


def main():
    try:
        # Ask user for input file
        filename = input("Enter the filename to read: ").strip()

        # Try reading the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content
        new_content = modify_content(content)

        # Ask for output file
        output_file = input("Enter the output filename: ").strip()
        with open(output_file, "w") as outfile:
            outfile.write(new_content)

        print(f"✅ Modified content has been written to '{output_file}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


if __name__ == "__main__":
    main()
