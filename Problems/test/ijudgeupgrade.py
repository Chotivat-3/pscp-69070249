"""I LOVE YU"""
text = input()
out = ''
key_start = text.startswith("https://ijudge.it.kmitl.ac.th/problems/")
if key_start:
    text = text[len("https://ijudge.it.kmitl.ac.th/problems/"):]
    if text.endswith("/"):
        text = text[:len(text)-1]
    key_num = len(text)
    if key_num == 4 and text[0] in "0123" and text.isdigit():
        out = f"{text[0]} STAR"
if out:
    print(out)
else:
    print("INVALID")
