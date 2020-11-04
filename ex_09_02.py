file_name = input("Enter file: ")
if len(file_name) < 1 :
    file_name = "mbox-short.txt"
handle = open(file_name)

days = dict()

for line in handle :
    line.rstrip()
    if not line.startswith("From ") : continue
    words = line.split()
    days[words[2]] = days.get(words[2], 0) + 1

for key in days :
    print(key, days[key])
