# Google-Docs Hooker Backend

The official Backend Engine for the gdocs-hooker extension. Trivial API Server to upload the downloaded to doc to the shared folder.

### Quick Start

1. Create a service account in your google cloud console. Get the `.json` file for connecting to your service account. 
2. Create a folder in your personal google drive account and share the access to that folder to your service account.
3. Clone the repository
```bash
git clone https://github.com/Harichandra-Prasath/Gdocs_Hooker_Backend.git
```
4. Download the requirements  
```bash
pip3 install -r requirements.txt
```
5. Create a .env file   
```bash
SHARED_FOLDER_ID=<Your shared Folder ID>
GOOGLE_CREDS_JSON=<Path for your .json file>
PORT=<Engine Port that you want to use>
```
6. Run the server  
```bash
python3 main.py --env-file <Path to .env file>
```

### Notes

1. If you have multiple google accounts, you can use the general run.sh for single entrypoint.  
2. You have to get the gdocks-hooker extension and configure it to use this backend engine.
