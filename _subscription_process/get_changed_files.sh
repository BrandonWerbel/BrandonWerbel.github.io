touch file_names.txt
# files_changed=$(/usr/bin/git diff-tree --no-commit-id --name-only -r $(/usr/bin/git log --format="%H" -n 1))
files_changed=${{ steps.Jitterbug.outputs.all }}
echo "$files_changed" > file_names.txt
echo "::debug:: $files_changed"