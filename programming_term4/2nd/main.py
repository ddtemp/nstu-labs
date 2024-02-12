#!/usr/bin/python
import argparse
import os

def remove_extension(file_name_with_extension):
    dot_index = file_name_with_extension.rfind(".")
    
    if dot_index != -1:
        return file_name_with_extension[:dot_index]
    else:
        return file_name_with_extension

def file_processing(source_file, character_to_remove):
    if not os.path.exists(source_file):
        print(f"Error: file '{source_file}' does not exist.")
        return
    elif len(character_to_remove) > 1:
        print(f"Error: character '{character_to_remove}' is too long.")
        return

    result_file = remove_extension(source_file)
    
    with open(source_file, 'r') as source_file:
        source_content = source_file.read()

    new_content = source_content.replace(character_to_remove, "") 

    with open(result_file + ".help", 'w') as result_file:
        result_file.write(new_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Removing specified character from a file')
    parser.add_argument('file', help='Path to the source file (REQUIRED)')
    parser.add_argument('character', help='Character to be removed from the file (REQUIRED)')

    arguments = parser.parse_args()

    file_processing(arguments.file, arguments.character)
