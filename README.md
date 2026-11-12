# Dropbox Folder Uploader

A small Python script that uploads the contents of a local folder to a Dropbox folder.

## Requirements

- Python 3
- A Dropbox API access token with the required file-write permissions
- The `dropbox` Python SDK

Install the dependency:

```bash
python -m pip install dropbox
```

## Configure credentials

Set the token as an environment variable. Do not hardcode credentials in source code or commit them to Git.

PowerShell:

```powershell
$env:DROPBOX_ACCESS_TOKEN = "your-token"
python c101/uploadingFolders.py
```

The script reads `DROPBOX_ACCESS_TOKEN` at runtime and exits with an error if it is missing.

## Usage

Run the script and provide:
1. The local folder path.
2. The destination Dropbox folder path.

## Security note

Any token that was previously committed to a public repository must be revoked or rotated in the Dropbox developer console. Removing it from the current source file does not remove it from Git history and does not invalidate the exposed credential.
