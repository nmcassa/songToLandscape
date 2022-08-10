# songToLandscape
 My best attempt at making a midi file print to resemble a landscape

## Soft - Vacations
![](landscapes/VACATIONS%20-%20Soft.png)

## Backstreet Boys
![](landscapes/Backstreet%20Boys%20-%20I%20Want%20It%20That%20Way.png)

Other examples in the landscapes folders. Pre-sorted pics in images folder.

To use just throw any song (midi file) into the music folder and run main.py (w/ requirements from pip below).

I don't know RGB values or color theory well so I just created the landscape by giving every RBG value a score that was:
```
blue / green * (blue + green)
```
and sorting it. The result is meh, kinda looks like a landscape, not really on the lower pixel count ones. It would be great to have the darker greens that are around the middle be on the bottom below the lighter greens or something similar. I don't know man, I don't really get it. 

Help is welcome

### Failed attempt
I've read and tried to implement the possibility of splitting up the sky and the land, then sorting by a contrast level. The reason I wasn't able to finish this is because to do this we need to find the contrast between each pixel and the atmospheric color levels. I don't know what an atmospheric color level is. Also this was slow because we needed to sort through the large array of rgb values multiple more times. 

## Requires
```
PIL (pillow)
mido
```
