from collections import Counter
import re

"""
This will only read file if its in the same
directory as the code. 
No need to make it unnecessarily complex
"""

def open_file(f_name: str) -> str:
    with open(f_name) as f:
        return f.read()
    
def get_freq(text: str) -> list[tuple[str, int]]:
    lowered_txt: str = text.lower()
    words: list[str] = re.findall(r"\b\w+\b", lowered_txt)

    word_counts: Counter = Counter(words)

    return word_counts.most_common()


def main() -> None:
    flag: str = input("Do you want to read a file? Y/N :").lower()
    if flag == "y" :
        while True:
            try:
                fname : str = input('Enter File Name: ')
                text : str = open_file(fname).strip()        
            except FileNotFoundError:
                print(f"Error: The file '{fname}' was not found.")
            except PermissionError:
                print(f"Error: You do not have permission to read the file '{fname}'.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            else:
                break
    if flag == "n" :
        text: str = input("Enter your text: ").strip()
    word_freq: list[tuple[str, int]] = get_freq(text)

    for word, count in word_freq:
        print(f"Word : {word:<15}  {"":^15} Freq : {count:<10}")


if __name__ == "__main__":
    main()


"""
Homework:
1. Create a function that allows the user to read a file directly (such as a txt)
so the user doesn't have to copy and paste text.

"""
