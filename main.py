from classes.FileIo import FileIo


file = FileIo("myfile.txt")
file.overwrite_file("some text more ")
file.append_file("\nI added this text")
file.read_file()
