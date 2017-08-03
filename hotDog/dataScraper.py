#Website Scraper
#So to train at ML, I'm going to have the catagories of 
#hot dog and hamburger instead of hot dog and not hot dog...
#for the image data sets I'm using image-net.org


#Hamburger Image URLs
burgerUrlOfUrls = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07697100"
burgerImagesDestination = "/media/hydroguy45/ML Data/hotDog/burger"

#Hot Dog Image URLs
hotDogUrlOfUrls = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07697537"
hotDogImagesDestination = "/media/hydroguy45/ML Data/hotDog/dog"

def recoverImages (urlOfUrls, imageDestination):
	print("We'll that worked")