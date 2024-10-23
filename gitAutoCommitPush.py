import os

# commit_msg = input("\033[34mCommit Message > \033[0m")

commit_msg = input("\033[34mCommit Message > ")
print("\033[0m")

os.system("pip freeze > requirements.txt")
os.system("git add .")
os.system(f'git commit -m "{commit_msg}"')
os.system("git push")

print("\033[32mPushed Successfully.\033[0m")
