from textwrap import dedent
# Global Variables



# Print a welcome message
def welcome():
    print(dedent("""
    Welcome to "Choose Your Own Adventure"!
    Enter the type of words as prompted by the computer to create your own descriptive adventure.
    """))

# Read a template Madlib file
def read_template(file):
    try:
        with open(file) as f:
            content = f.read()
            return content
    except FileNotFoundError:
       raise FileNotFoundError



# Parse the file into usable parts
def parse_template(template):
    stripped_str = ""
    stripped_parts_str = ""
    stripped_parts = []

    is_part = False
    for char in template:
        if char == "{":
            stripped_str += char
            is_part = True
        elif is_part == True and char != "}":
            stripped_parts_str += char
        elif is_part == True and char == "}":
            stripped_str += char
            is_part = False
            stripped_parts.append(stripped_parts_str)
            stripped_parts_str = ""
        else:
            stripped_str += char
    return stripped_str, tuple(stripped_parts)



# Prompt the user to submit a series of words to fit each of the required components of the Madlib template
def prompt_user(text):
    new_word_list = []
    for word in text:
        new_word = input(f"> Enter a {word}: ")
        new_word_list.append(new_word)
    return new_word_list



# With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template
def merge(text, inputs):
    print(text.format(*inputs))
    return text.format(*inputs)



# After the resulting Madlib has been completed, provide the completed response back to the user in the command line

def main(file_path):
    welcome()
    script = read_template(file_path)
    txt, parts = parse_template(script)
    user_inputs = prompt_user(parts)
    result = merge(txt, user_inputs)
    print(result)
    new_file = file_path.replace(".txt", ".replaced.txt")
    with open(new_file, "w") as f:
        f.write(result)

if __name__ == "__main__":
    # source_file = "./text/spam.txt"
    source_file = "./text/videogame.txt"
    main(source_file)

# Write the completed text (Example)to a new file on your file system (in the repo)