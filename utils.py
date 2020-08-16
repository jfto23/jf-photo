from config import S3_BUCKET, S3_KEY, S3_SECRET
import boto3

BASE_URL = f"https://{S3_BUCKET}.s3.amazonaws.com/"

class Album:
    def __init__(self,title,cover_link="", images=[]):
        self.title = title
        self.cover_link = cover_link
        self.images = images

s3 = boto3.resource(
        's3',
        aws_access_key_id=S3_KEY,
        aws_secret_access_key=S3_SECRET)

bucket = s3.Bucket(S3_BUCKET)

images = []
for obj in bucket.objects.all():
    if obj.key[-1] != "/":
        images.append(obj.key)

dct = {}
for image in images:
    album = image[:image.index("/")]
    if dct.get(album):
        dct[album].append(image)
    else:
        dct[album] = [f"{BASE_URL}{image}"]


albums = []
for album_title, images in dct.items():
    album = Album(album_title,
            images[0],
            images)
    albums.append(album)

for album in albums:
    print(album.title)
    print(album.cover_link)
    print(album.images)




