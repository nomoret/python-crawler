import csv


def save_to_csv(posts):
    file = open("posts.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(['id', 'subject'])

    for post in posts:
        writer.writerow(list(post.values()))
