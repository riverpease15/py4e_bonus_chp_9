file_name = input("Enter file: ")
if len(file_name) < 1 :
    file_name = "mbox-short.txt"
handle = open(file_name)

emails = dict()

for line in handle :
    line.rstrip()
    if not line.startswith("From ") : continue
    line = line.split()
    email = line[1]
    emails[email] = emails.get(email,0) + 1

for key in emails :
    print(key, emails[key])
