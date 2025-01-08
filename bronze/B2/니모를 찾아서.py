import sys
input = sys.stdin.readline

while True:
    sentense = input().rstrip()
    if sentense == "EOI":
        break
    else:
        sentense = sentense.lower()
        print("Found" if "nemo" in sentense else "Missing")