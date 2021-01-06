touch file_names.txt
files_changed=$(/usr/bin/git diff-tree --no-commit-id --name-only -r $(/usr/bin/git log --format="%H" -n 1))
echo "$files_changed" > file_names.txt