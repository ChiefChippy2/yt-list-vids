from main import *

id = get_upload_pl('technothepig')
vids = pl_vids(id)
assert len(vids) == 328

print('OK')