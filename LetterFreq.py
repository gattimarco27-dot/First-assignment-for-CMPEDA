import time
import argparse
import os
import matplotlib.pyplot as plt

total_letters = 0
oldchar = "a"
letters = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
inBook = False
nLines = 0
nWords = 0
def valid_path(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"Path '{path}' does not exist.")
    return path

parser = argparse.ArgumentParser(description="Analyze letter frequencies and statistics in a text file.")
start_time = time.time()
parser.add_argument(
    "--file", type=valid_path, help="Path to the text file to analyze", required=True)
parser.add_argument(
    "--onlybook", action="store_true", help="Analyze only the main book content (ignore preface, appendix, etc.)")
parser.add_argument(
    "--graph", action="store_true", help="Display a bar chart of letter frequencies using matplotlib")
parser.add_argument(
    "--generalstats", action="store_true", help="Show general statistics (lines, words, etc.) about the book")
args = parser.parse_args()
book = args.onlybook
with open(args.file, "r", encoding="utf-8") as file:
    while True:
        char = file.read(1)
        if book == True:
            if(oldchar == "\n" and char == "*"):
                file.readline()
                inBook = not inBook
            oldchar = char
        if book==False:
            inBook = True 
        if not char:
            break
        if inBook:
            if(args.generalstats):
                if char == "\n":
                    nLines = nLines + 1
                if char == " ":
                    nWords=nWords + 1
            if not char.isalpha() or not char.isascii():
                continue
            total_letters = total_letters+1
            char = char.lower()
            letters[char] = letters[char] + 1
relative_letters = {k: v / total_letters for k, v in letters.items()}
end_time = time.time()
print(f"Total elapsed time: {end_time - start_time:.4f} seconds")
if args.generalstats:
    print("Number of lines: ", nLines)
    print("Number of words: ", nWords)
    print("Number of letters: ", total_letters)
if args.graph:
    plt.bar(relative_letters.keys(), relative_letters.values())
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency Histogram')
    plt.show()