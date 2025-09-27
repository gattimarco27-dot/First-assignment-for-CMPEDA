import argparse
import os
import matplotlib.pyplot as plt

total_letters = 0
lines = 0
oldchar = "a"
letters = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
def valid_path(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"Path '{path}' does not exist.")
    return path

parser = argparse.ArgumentParser()
parser.add_argument(
    "--file", type=valid_path, help="Path to file that the program process", required=True
)
parser.add_argument("--onlybook", action="store_true", help="Process only the book content")
args = parser.parse_args()
inBook = args.onlybook

with open(args.file, "r", encoding="utf-8") as file:
    while True:
        if inBook == True:
            char = file.read(1)
        if inBook == False:
            char = file.read(1)
            if(oldchar == '\n' and char == "*"):
                print(file.readline())
                print("dentro al libro")
                inBook = True
            oldchar = char
        if(oldchar == '\n' and char == "*"and inBook == True and not args.onlybook):
                print(file.readline())
                print("fine del libro")
                break
        oldchar = char
        if not char:
            break
        if not char.isalpha() or not char.isascii():
            continue
        if inBook:
            total_letters = total_letters+1
            char = char.lower()
            letters[char] = letters[char] + 1

        
relative_letters = {k: v / total_letters for k, v in letters.items()}
print(total_letters)
plt.bar(relative_letters.keys(), relative_letters.values())
plt.xlabel('Letters')
plt.ylabel('Frequency')
plt.title('Letter Frequency Histogram')
plt.show()