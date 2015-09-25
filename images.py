from cImage import *

print("rotate90() function takes around 20 seconds to execute.")
##IMPORTANT! Read following line if grading please:##
#my rotate90() function takes 20 to execute. call display(rotate90(#/imagefile))
#or use the tyrion.gif, and call display(rotate90(tyrion))

tyrion = Image("tyrion.gif")


def display(image):
    display = ImageWin("Show Image", image.getWidth(), image.getHeight())
    image.draw(display)

def greyScale(originalImage):
    width = originalImage.getWidth()
    height = originalImage.getHeight()
    newImage = EmptyImage(width, height)
    for x in range(width):
        for y in range(height):
            originalPixel = originalImage.getPixel(x,y)
            newPixelAverage = int((originalPixel.red + originalPixel.green + originalPixel.blue)/3)
            newPixelSet = Pixel(newPixelAverage, newPixelAverage, newPixelAverage)
            newImage.setPixel(x, y, newPixelSet)
    return newImage
#display(greyScale(#image))

def lighten(originalImage, percentIncrease):
    width = originalImage.getWidth()
    height = originalImage.getHeight()
    newImage = EmptyImage(width, height)
    percentIncrease += 1
    for x in range(width):
        for y in range(height):
            originalPixel = originalImage.getPixel(x,y)
            if int(originalPixel.red*percentIncrease) < 255 and int(originalPixel.red*percentIncrease) > 0:
                newPixelRed = int(originalPixel.red*percentIncrease)
            elif int(originalPixel.red*percentIncrease) < 0:
                newPixelRed = 0
            else:
                newPixelRed = 255
            if int(originalPixel.green*percentIncrease) < 255 and int(originalPixel.green*percentIncrease) > 0:
                newPixelGreen = int(originalPixel.green*percentIncrease)
            elif int(originalPixel.green*percentIncrease) < 0:
                newPixelGreen = 0
            else:
                newPixelGreen = 255
            if int(originalPixel.blue*percentIncrease) < 255 and int(originalPixel.blue*percentIncrease) > 0:
                newPixelBlue = int(originalPixel.blue*percentIncrease)
            elif int(originalPixel.blue*percentIncrease) < 0:
                newPixelBlue = 0
            else:
                newPixelBlue = 255
            newPixelSet = Pixel(newPixelRed, newPixelGreen, newPixelBlue)
            newImage.setPixel(x,y, newPixelSet)
    return newImage
#display(lighten(#image,#percentIncrease))

def rotateNeg90(originalImage):
    width = originalImage.getWidth()
    height = originalImage.getHeight()
    newImage = EmptyImage(height,width)
    yPixel = 0

    for x in range(height-1):
        xPixel = width-1
        while xPixel >= 0:
            for y in range(width-1):

                if xPixel >= 0:
                    copyPixel = originalImage.getPixel(xPixel,yPixel)
                    newImage.setPixel(x, y, copyPixel)
                xPixel -= 1
        yPixel += 1
    return newImage

def rotate90(originalImage):
    rotatedImage = rotateNeg90(rotateNeg90(rotateNeg90(originalImage)))
    return rotatedImage



def test_rotate(width, height):
    test_array = []


    # once yPixel reaches height, go down 1 from width, re-iterate through height
    yPixel = 0

    for x in range(height+1):
        xPixel = width
        while xPixel >= 0:
            for y in range(width):

                if xPixel >= 0:

                    test_array += [xPixel, yPixel]

                xPixel -= 1
        yPixel += 1
    return test_array
      

#considered solutions lacking fruition.

#how to do this!...
    


#use getPixel()

#    for x in range(width):
#        yPixelCount = height
#        for y in range(height):
#            newYPixel = x
#            newXPixel = yPixelCount
#            yPixelCount -= 1
#            
#        print(newYPixel, newXPixel)
#    rotatedImage = rotate90(originalImage)
#    for x in range(width):
#        for y in range(height):
#            if int((x+width)*.99607) > 255:
#                newPixelSetX = 255
#            elif int((x+width)*.99607) < 0:
#                newPixelSetX = 0
#            else:
#                newPixelSetX = int((x+width)*.99607)
#            if int((y+width)*.99607) > 255:
#                newPixelSetY = 255
#            elif int((y+width)*.99607) < 0:
#                newPixelSetY = 0
#            else:
#                newPixelSetY = int((y+width)*.99607)
#            newPixelSet = originalImage.getPixel(newPixelSetX, newPixelSetY)
#            newPixelSet = originalImage.getPixel(x+width, y+width)
#            newPixelSet = Pixel(newPixelSetY, newPixelSetX)
#            newImage.setPixel(x, y, newPixelSet)
#    return newImage
#display(rotate(#image))
#    return rotatedImage


#rethink

#go bottom-up.
