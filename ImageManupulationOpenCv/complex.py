from tkinter import TRUE
import cv2
'''
Display Image, Thn destroy Window on hitting the Escape Key
'''

img = cv2.imread('./mandrill_colour.png')

while TRUE:
    cv2.imshow('mandrill_colour', img)

    '''
    The cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. 
    The function waits for specified milliseconds for any keyboard event. If you press any key 
    in that time, the program continues.
    '''
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

'''
Save an Image 
'''
cv2.imwrite('finalImage.png', img)
