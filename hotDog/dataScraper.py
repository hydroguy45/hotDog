#Website Scraper (Python 3)
#So to train at ML, I'm going to have the catagories of 
#hot dog and hamburger instead of hot dog and not hot dog...
#for the image data sets I'm using image-net.org...
#edit: since hot dogs and burgers are quite similar, and I don't have many hot dog pics... I'll opt for a different
#possible catagory, cats... because cats and dogs.... oh I so funny.... any way, so I'm changing the image sources

import urllib
from urllib import request
from PIL import Image, ImageChops
import os
#TODO:
# -make everything a jpg
# -grayscale everything


#Cat Image URLs
catUrlOfUrls = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02121808"
catImagesDestination = "/media/hydroguy45/ML Data/hotDog/cat/"

#Hot Dog Image URLs
hotDogUrlOfUrls = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07697537"
hotDogImagesDestination = "/media/hydroguy45/ML Data/hotDog/dog/"

def recoverImages (urlOfUrls, imageDestination):
	i = 0
	with Image.open(request.urlopen("https://s.yimg.com/pw/images/en-us/photo_unavailable.png")).resize((40,40), Image.ANTIALIAS).convert("L") as photoNoLongerAvailable:
		with request.urlopen(urlOfUrls) as r:
			lines = r.read().splitlines()
			for line in lines:
				url = line.decode("utf-8")
				if url != "https://www.loafnjug.com/images/hot-dog-and-tea.jpg":
					if i%10 == 0:
						print("{}%".format(i/len(lines)))
					try:
						imageString = request.urlretrieve(url, imageDestination + "{}.jpg".format(i))
						try:
							with open(imageDestination + "{}.jpg".format(i), "r+b") as f:
								with Image.open(f) as image:
									os.remove(imageDestination + "{}.jpg".format(i))
									final = image.resize((40,40), Image.ANTIALIAS).convert("L")
									final.save(imageDestination + "{}.jpg".format(i))
									if ImageChops.difference(final, photoNoLongerAvailable).getbbox() is None:
										os.remove(imageDestination + "{}.jpg".format(i))
						except:
							os.remove(imageDestination + "{}.jpg".format(i))
					except:
						print("Exception")

					i = i + 1
	print("We'll that worked")

if __name__ == "__main__":
	print("Starting")
	recoverImages(catUrlOfUrls, catImagesDestination)
	recoverImages(hotDogUrlOfUrls, hotDogImagesDestination)