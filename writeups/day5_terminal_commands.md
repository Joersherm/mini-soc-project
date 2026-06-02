# Day 5: Terminal Commands

## Commands

### pwd
- prints which directory the user is currently working in

```bash
pwd
```

### ls
- list files and folders of the current directory
- -a reveals hidden files
- -l lists information on each file

```bash
ls
```

### cd
- changes the directory the user is in
```bash
cd new_directory
```

### mkdir
- makes a new directory
```bash
mkdir name_of_directory
```

### touch
- makes new files
```bash
touch new_file_name
```

### rmdir
- removes directory only if empty
```bash
rmdir directory
```

### rm
- removes files
- -r means that it should a directory and all files in it
```bash
rm file_name
```

### mv
- renames a file or moves it to a new directory
```bash
mv old_name new_name
```
```bash
mv file new_directory/
```

### cp
- allow for copying contents of one file into a new file
- -r allows the same to be done for directories
```bash
cp old_file new_file
```

### cat
- if only one arguement is passed then the contents of that file are printed
- if 2 arguements are passed then the contents of both are printed back to back
```bash
cat file1 file2
```

### less
- shows program page by page
- space bar to scroll down a page
- b to scroll up a page
```bash
less program
```

### echo
- repeats an instruction
```bash
echo hello
```

### find
- finds files based on specific paramaters
- can search for files containing specific strings using wildcards (*)
- -type d means to look specificlly for a directory
- -name causes it to look for a specific name
```bash
find directory_name -name "name"
```

### grep
- looks for a specific word in a file and highlights it
```bash
grep word filename
```