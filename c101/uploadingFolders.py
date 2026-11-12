import os
import posixpath

import dropbox
from dropbox.files import WriteMode


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, _, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = posixpath.join(file_to, relative_path.replace(os.sep, "/"))

                with open(local_path, "rb") as file:
                    dbx.files_upload(
                        file.read(),
                        dropbox_path,
                        mode=WriteMode("overwrite"),
                    )


def main():
    access_token = os.environ.get("DROPBOX_ACCESS_TOKEN")
    if not access_token:
        raise RuntimeError(
            "Set the DROPBOX_ACCESS_TOKEN environment variable before running this script."
        )

    transfer = TransferData(access_token)
    file_from = input("Enter the local folder path to transfer: ").strip()
    file_to = input("Enter the destination Dropbox folder path: ").strip()

    transfer.upload_file(file_from, file_to)
    print("Upload completed.")


if __name__ == "__main__":
    main()
