import datetime
now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d %H:%M")

with open("README.md", "r") as f:
    readme = f.read()

readme = f'{readme[:readme.find("Last updated: ")]}Last updated: {now_str}'

with open("README.md", "w") as f:
    f.write(readme)

print("README.md file updated successfully")
