import os

fp = open("stupidTest.txt", 'r')
data = int(fp.read())
fp.close()
data += 1

fp = open("stupidTest.txt", 'w')
fp.write(str(data))
fp.close()


os.system("git add .")
os.system(f'git commit -m "{data} test"')
os.system("git push")
