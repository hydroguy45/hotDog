#Website Scraper (Python 3)
#So to train at ML, I'm going to have the catagories of 
#hot dog and hamburger instead of hot dog and not hot dog...
#for the image data sets I'm using image-net.org
import urllib
from urllib import request

#Hamburger Image URLs
burgerUrlOfUrls = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07697100"
burgerImagesDestination = "/media/hydroguy45/ML Data/hotDog/burger/"

#Hot Dog Image URLs
hotDogUrlOfUrls = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07697537"
hotDogImagesDestination = "/media/hydroguy45/ML Data/hotDog/dog/"

def recoverImages (urlOfUrls, imageDestination):
	i = 0
	with request.urlopen(urlOfUrls) as r:
		lines = r.read().splitlines()
		for line in lines:
			url = line.decode("utf-8")
			print(url)
			try:
				imageString = request.urlretrieve(url, imageDestination + "_{}.jpg".format(i))
			except:
				print("Exception")
			i = i + 1
	print("We'll that worked")

if __name__ == "__main__":
	print("Starting")
	recoverImages(burgerUrlOfUrls, burgerImagesDestination)
	recoverImages(hotDogUrlOfUrls, hotDogImagesDestination)