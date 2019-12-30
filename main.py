from liquor import extract_last_page, extract_post
from save import save_to_csv

gallery_name = "alcohol"
# last_liquor_page = extract_last_page(gallery_name)
last_liquor_page = 1
posts = extract_post(gallery_name, last_liquor_page)
print(posts)
save_to_csv(posts)
