import os


commit_msg = "Test with easy python script to auto push and stuff"


os.system("git add .")
os.system(f'git commit -m "{commit_msg} test"')
os.system("git push")

print("\033[32mPushed Successfully.\033[0m")  # Green text