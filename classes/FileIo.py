class FileIo:

    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        f = open(self.filename, 'r')
        print(f.read())

    def append_file(self, text):
        f = open(self.filename, 'a')
        f.write(text)
        f.close()

    def overwrite_file(self, text):
        f = open(self.filename, 'w')
        f.write(text)
        f.close()
