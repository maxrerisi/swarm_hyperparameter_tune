import os


# commit_msg = input("\033[34mCommit Message > \033[0m")

commit_msg = input("\033[34mCommit Message > ")

os.system("git add .")
os.system(f'git commit -m "{commit_msg} test"')
os.system("git push")

print("\033[32mPushed Successfully.\033[0m")  # Green text
