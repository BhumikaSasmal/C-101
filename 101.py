import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
    
def main():
    access_token="sl.BFem9oyzXFzGt3oeQgnf8cowng34zJQGsI6Sig1FF8Q9KUBbjaNP01vU9K9qp8gMroG5BjVb4cljSsolJq5hHuMlPx4mkH69rZQUtE0l9lyazt4YNLn2xG9FbZO7hhPXFWltZLZyP926"
    transferData=TransferData(access_token)
    file_from= input("Enter the File path to transfer: ")
    file_to = input("Enter the file path to upload to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("File has been transfered.")

main()