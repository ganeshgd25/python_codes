

# # Python File I/O – One-Line Summary
# ### `open()`
# Used to **open a file** so that Python can read or write data in it.

# ---

# ### `close()`

# Used to **close the file** and release system resources after file operations are finished.

# ---

# ### `write()`

# Used to **write text into a file** and returns the **number of characters written**.

# ---

# ### `read()`

# Used to **read the entire file or specified number of characters** from the current cursor position.

# ---

# ### `readline()`

# Used to **read one line at a time** from the file (includes newline `\n`).

# ---

# ### `readlines()`

# Used to **read all lines of a file and return them as a list**.

# ---

# ### `tell()`

# Used to **return the current position of the file cursor**.

# ---

# ### `seek()`

# Used to **move the file cursor to a specific position in the file**.

# ---

# ### `with open()`

# Used to **open a file safely and automatically close it after operations**.

# ---

# # Example File Flow

# Typical file handling pattern:

# ```python
# with open("file.txt", "r") as f:
#     data = f.read()
# ```

# Open → Read → Auto Close.

# ---

# # Modes Quick Reference

# | Mode | Action                 |
# | ---- | ---------------------- |
# | `r`  | Read file              |
# | `w`  | Write (overwrite file) |
# | `a`  | Append content         |
# | `x`  | Create new file        |
















# with open("ganesh.txt" , "r") as f:
#     content= f.read()
#     print(content)

# with open("ganesh.txt", "w") as f:
#     gd= f.write("Hello Ganesh")
#     print(gd)


# with open("ganesh.txt", "a") as f:
#     gd= f.write("\nHello Ganesh hi")
#     print(gd)

# with open("ganesh.txt", "w") as f:
#     x = f.write("Python\n")
#     y = f.write("Backend\n")

# print(x, y)

# with open("ganesh.txt") as f:
#     data =[line.strip() for line in f.readline()] 
#     print(data)


# with open("ganesh.txt") as f:
#     data =f.readline()
#     print(data)

with open("ganesh.txt") as f:
    print(f.readline())
    print(f.read())