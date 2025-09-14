import os
import inc.dropbox_downloader as dbx

scripts_dir = os.path.dirname(os.path.realpath(__file__))

root_dir = scripts_dir + "/.."
dest_dir = root_dir + "/neural_network/bin/data"

files = [
    ("https://www.dropbox.com/scl/fi/suooo95i3yurvz65bl99h/flights_by_cell_day_spot.pkl.zip?rlkey=e0ov1y0yy1b7kexqfrtxgk9cc&st=yty2vknq&dl=0", "flights_by_cell_day_spot.pkl.zip"),
    ("https://www.dropbox.com/scl/fi/jyf6x3y3obdp1uus53p72/flights_by_cell_day.pkl.zip?rlkey=jxgg6axfk9gvimfju68s3tkao&st=1qo3k0ak&dl=0", "flights_by_cell_day.pkl.zip"),
    ("https://www.dropbox.com/scl/fi/32whv1zaevlq0o02b80d4/flights_by_spot.pkl.zip?rlkey=i0zflt42j6708u8ogsod70bx0&st=bvp2oq54&dl=0", "flights_by_spot.pkl.zip"),
    ("https://www.dropbox.com/scl/fi/1sm4mx6tua4140xh2nh75/meteo_content_by_cell_day.pkl.zip?rlkey=agsnmn7eziv5lzv64caqa00l3&st=hryw8avp&dl=0", "meteo_content_by_cell_day.pkl.zip"),
    ("https://www.dropbox.com/scl/fi/2z8f2imxaaofts4kduzxc/meteo_days.pkl.zip?rlkey=qr26guymxzpv7iop981pwlxhx&st=unlrmdc7&dl=0", "meteo_days.pkl.zip"),
    ("https://www.dropbox.com/scl/fi/om55tinsfih8368uam35g/meteo_params.pkl.zip?rlkey=z402q158xksmregwc4qekw4kl&st=uumwwm3v&dl=0", "meteo_params.pkl.zip"),
    ("https://www.dropbox.com/scl/fi/fvxa21doza7zkbqdorrxp/mountainess_by_cell_alt.pkl.zip?rlkey=3gyzu1bwxcyjd3cmxxsmdug9z&st=2r246gil&dl=0", "mountainess_by_cell_alt.pkl.zip"),
    ("https://www.dropbox.com/scl/fi/1m354a4jbsgzrjdniqmv2/sorted_cells_latlon.pkl.zip?rlkey=aw1a1r9toppawfa14gfbjpier&st=drhavwbk&dl=0", "sorted_cells_latlon.pkl.zip"),
    ("https://www.dropbox.com/scl/fi/3xwii8d4dqql28ulr6zs8/spots_by_cell.pkl.zip?rlkey=1c4xpj9h7yj01ax59iw0id6xk&st=3votkq2a&dl=0", "sorted_cells.pkl.zip"),
    ("https://www.dropbox.com/scl/fi/3xwii8d4dqql28ulr6zs8/spots_by_cell.pkl.zip?rlkey=1c4xpj9h7yj01ax59iw0id6xk&st=b4ewq450&dl=0", "spots_by_cell.pkl.zip"),
    ("https://www.dropbox.com/scl/fi/9ulpqafh53c5k49d53gfw/spots_merged.pkl.zip?rlkey=z9rx0vsdolqf8f5ombdv0lejz&st=hv6eatl7&dl=0", "spots_merged.pkl.zip"),
    ("https://www.dropbox.com/scl/fi/kueb70umxsfxe72yclhjf/spots.pkl.zip?rlkey=y00mat258o8twx1tnajz1idkf&st=2xfg8a6k&dl=0", "spots.pkl.zip")
]

for dropbox_url, res_file in files:
    print("Downloading", os.path.join(dest_dir, res_file), "...")
    dbx.download(dropbox_url, dest_dir, res_file)
