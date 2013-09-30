# CapLoad

A screen-capture utility for OSX

1. Lets you select what area of the screen to capture
2. `rsync`'s the image with a unique name to the server of your choice
3. Copies the remote URL to your clipboard 


## Installation

### Adjust `REMOTE` section of `capload.py` to match your server:

https://github.com/dancrew32/capload/blob/master/capload.py#L12-L20

### Set capload up as an OSX Service:

![Service setup](http://i.danmasq.com/cap.1380516153.png)

### Save your service, set keyboard shortcut

e.g. `Command + Shift + 4`:

![keyboard shortcut](http://i.danmasq.com/cap.1380516296.png)

Run it!
`Command + Shift + 4`, select area, paste url
