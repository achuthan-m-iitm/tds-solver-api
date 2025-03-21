import zipfile
import os

# Create a temporary directory to hold text files
os.makedirs("temp_txts", exist_ok=True)

# Create two sample text files
with open("temp_txts/one.txt", "w") as f:
    f.write("This is line 1.\nThis is line 2.\n")

with open("temp_txts/two.txt", "w") as f:
    f.write("Line A\nLine B\nLine C\n")

# Create a zip archive
with zipfile.ZipFile("test_texts.zip", "w") as zipf:
    zipf.write("temp_txts/one.txt", arcname="one.txt")
    zipf.write("temp_txts/two.txt", arcname="two.txt")

print("Created test_texts.zip with 2 text files.")

# Optional cleanup
# import shutil
# shutil.rmtree("temp_txts")
