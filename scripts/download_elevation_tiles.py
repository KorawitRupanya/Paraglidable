import os
import inc.dropbox_downloader as dbx

scripts_dir = os.path.dirname(os.path.realpath(__file__))

root_dir = scripts_dir + "/.."
dest_dir = root_dir + "/tiler/_cache/elevation"
if os.path.isdir("/workspaces/Paraglidable"): # in docker
	www_dir = root_dir + "/www/"
else: # on production server
	www_dir = "/var/www/html/"

os.makedirs(dest_dir, exist_ok=True)
os.makedirs(www_dir + "data", exist_ok=True)
os.system("ln -s "+ dest_dir +" "+ www_dir +"data/elevation")

# Dropbox links (replace ... with real ones, make sure to use ?dl=1)
files = [
    ("https://www.dropbox.com/scl/fi/0c6errf1tgrg8asls6gip/5.zip?rlkey=n3ixra7yyto3lcj2sawgkzf69&st=lmoqsxuo&dl=0", "5.zip"),
    ("https://www.dropbox.com/scl/fi/tlirn7yqi1z0o4w380ewh/6.zip?rlkey=821s5cki8c34t8gbn020wpt8m&st=s6qgwotd&dl=0", "6.zip"),
    ("https://www.dropbox.com/scl/fi/3rqv0lewhx14lziomg6ug/7.zip?rlkey=316yxuvvun7jp6k8jwji2bxxv&st=z6gthuco&dl=0", "7.zip"),
    ("https://www.dropbox.com/scl/fi/rybnp77obsxe8js7cc2ev/8.zip?rlkey=kir9gzov37r8n8uak3m3pik55&st=bqo5onpp&dl=0", "8.zip"),
    ("https://www.dropbox.com/scl/fi/b7g4y8gjpj5mvsa63s4ib/9.zip?rlkey=pjjwqs35cprmin9anyczp1fbs&st=pnqks37p&dl=0", "9.zip"),
]

for dropbox_url, res_file in files:
    print("Downloading", os.path.join(dest_dir, res_file), "...")
    dbx.download(dropbox_url, dest_dir, res_file)