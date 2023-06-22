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

# file_types
#  list of expected file types to be copied
file_types = [".jpg", ".jpeg", ".png"]

# recursive_search
#  True: search for files in subdirectories
#  False: search for files only in srcDir
recursive_search = False

# failed_files
#  list of files that failed to be copied
failed_files = []

# ===========


# ===========
# FUNCTIONS
# ===========

def print_const_info() :
    print("\n====== CONSTANTS INFO ======")
    print("Source Directory: " + srcDir)
    print("Destination Directory: " + dstDir)
    print("Recursive Search: " + str(recursive_search))
    print("====================================\n\n")

def get_src_files() :
    global srcDir
    src_files = []
    if not(recursive_search) :
        src_files = [x for x in os.listdir(srcDir) if os.path.isfile(os.path.join(srcDir,x))]
    else :
        for root, dirs, files in os.walk(srcDir):
            for file in files:
                src_files.append(os.path.join(root,file))
        
    return src_files


def get_final_file_types(src_file_types) :
    global file_types
    file_types = list(set(file_types) & set(src_file_types))
    print("====== AVAILABLEFILE TYPES ======")
    print(src_file_types)
    print("====== CURRENTFILE TYPES ======")
    print(file_types)
    print("\nWANT TO ADD MORE FILE TYPES? IF YES:\n 1. SPECIFY THEM, SEPARATED BY COMMA ONLY (without \".\")\n 2. TYPE 0 TO ADD ALL FILE TYPES\n 3. LEAVE BLANK TO KEEP CURRENT FILE TYPES")
    ok = False
    while not(ok):
        new_file_types = input("\n>>> ")
        update_file_types(new_file_types,src_file_types)
        print("====== CURRENT FILE TYPES ======")
        print(file_types)
        sure = input("Are you sure? (y/n) ")
        if sure == "y" :
            ok = True
                
                
        


def update_file_types(inpt,src_file_types):
    global file_types
    if inpt == "0" :
        file_types = src_file_types
    elif inpt == "" :
        pass
    else :
        file_types += inpt.split(",")
        file_types = list(set(file_types) & set(src_file_types))
        

    return file_types

# ===========




# ===========
# MAIN
# ===========

print_const_info()

print("Getting files...")
srcFiles = get_src_files()

src_file_types = [x.split(".")[-1] for x in srcFiles if "." in x]
src_file_types = list(set(src_file_types))
get_final_file_types(src_file_types)

final_src_files = [x for x in srcFiles if x.split(".")[-1] in file_types]

num_copied = 0
for file in final_src_files :
    try :
        shutil.copy2(os.path.join(srcDir,file),dstDir)
        num_copied+=1
    except :
        failed_files.append(file)
        
        
print(f"Of {len(final_src_files)}, successfuly copied {num_copied} files")
print(f"Accuracy of {(round(num_copied/len(final_src_files))*100,5)}%")


with open("CopyFilesFiles/UnsuccessfulCopies.txt", "w") as file:
    for failed_file in failed_files:
        file.write(failed_file + "\n")

    
    


