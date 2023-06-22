# ========
# IMPORTS
# ========
import os
import shutil

# =========


# ===========
# CONSTANTS
# ===========

srcDir = "/mnt/c/Users/joaom/Documents/"
dstDir = ""

file_types = [".jpg", ".jpeg", ".png"]
list_all_file_types = True
recursive_search = False

# ===========


# ===========
# FUNCTIONS
# ===========

def get_src_files() :
    src_files = []
    if not(recursive_search) :
        src_files = [x for x in os.listdir(srcDir) if os.path.isfile(os.path.join(srcDir,x))]
    else :
        for root, dirs, files in os.walk(srcDir):
            for file in files:
                src_files.append(os.path.join(root,file))
        
    return src_files

# ===========




# ===========
# MAIN
# ===========

print("Getting files...")
srcFiles = get_src_files()

src_file_types = [x.split(".")[-1] for x in srcFiles if "." in x]
src_file_types = list(set(src_file_types))
print("====== FILE TYPES ======")
print(src_file_types)
print("\nCurrent file types: ")
print(file_types)
print("WANT TO ADD MORE FILE TYPES? IF YES:\n 1. SPECIFY THEM, SEPARATED BY COMMA ONLY\n 2. TYPE 0 TO ADD ALL FILE TYPES\n 3. LEAVE BLANK TO KEEP CURRENT FILE TYPES")
new_file_types = input("\n>>> ")


