# Obsidian Sync
**A python script for syncing your [obsidian vaults](https://obsidian.md/).**

I started using obsidian recently, but I haven't used used it enough to pay for [sync](https://help.obsidian.md/Licenses+%26+add-on+services/Obsidian+Sync).<br>
So I made this script to manually upload your backups to mega.nz :)

Based on:
* https://github.com/r4v10l1/python-zip-folder (Minecraft upload shit)
* https://github.com/mikkelrask/python-zip-folder (Sick rice)

### Installation
```bash
git clone https://github.com/r4v10l1/PythonObsidianSync
cd PythonObsidianSync
pip install -r requirements.txt
python ObsidianSync.py
```

### Configuration
You need to change the folowing variables inside the `.env` file:
* **email**: Your mega.nz email.
* **password**: Your mega.nz password.
* **obsidian-path**: Local Obsidian vault path
* **displayDetails**: `true` or `false`
* **delete-local-file**: `true` or `false`. Will delete the local .zip file after uploading.
