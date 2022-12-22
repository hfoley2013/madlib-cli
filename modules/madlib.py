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
    """
    Takes a parameter called file, opens the file, and renders the content.
    The function returns the rendered content in a variable names 'content'.
    This content is used to generate a template for use in 'parse_template()'
    :param file:
    :return: content
    """
    try:
        with open(file) as f:
            content = f.read()
            return content
    except FileNotFoundError:
       raise FileNotFoundError



# Parse the file into usable parts
def parse_template(template):
    """
    Takes in the content from 'read_template()' function and iterates through the characters of the string in order to remove any words contained within "{}".
    Characters contained inside "{}" are parsed out and added to the 'stripped_parts' list; all other characters are added to the 'stripped_str' variable.
    The function returns two variables: 'stripped_str', which contains all characters not encased in "{}"; and 'stripped_parts' which contains all the characters contained within "{}" from the original text.
    :param template:
    :return: stripped_str, tuple(stripped_parts)
    """
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
    """
    This function takes in a parameter 'text', which is the return value from 'parse_template()' called tuple(stripped_parts).
    The function then prompts the user to enter a word that fits the description of each of the elements contained within the tuple.
    The function returns each of these user inputs as a consolidated list once the user answers all prompts.
    :param text:
    :return: new_word_list
    """
    new_word_list = []
    for word in text:
        new_word = input(f"> Enter a {word}: ")
        new_word_list.append(new_word)
    return new_word_list



# With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template
def merge(text, inputs):
    """
    This function takes in two parameters: text, which is the return value of 'parse_template()' called 'stripped_str'; and inputs, which is the return value of 'prompt_user()' called new_word_list.
    The function then combines the user inputs into the text are prints the result to the console.
    :param text:
    :param inputs:
    :return: text.format(*inputs))
    """
    print(text.format(*inputs))
    return text.format(*inputs)



# After the resulting Madlib has been completed, provide the completed response back to the user in the command line

def main(file_path):
    """
    This function takes a file path as a parameter and is responsible for executing the madlib program in its entirety.
    The file path is passed to 'read_template()' to generate a script that can then be parsed into usable parts by the 'parse_template()' function.
    The return value of 'parse_template()' is stored as 'txt' and 'parts', which are then passed to 'user_inputs()' and 'merge()' functions to prompt the user for inputs and then combining those inputs into the parsed text from the 'parse_template()' function.
    The program terminates with writing the result of the program into a new file and saves it to the 'text' folder.
    :param file_path:
    :return:
    """
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