from random import randint

playlist = ["Беспечный ангел", "Stardust", "Либо кодить либо нах", "American boy"]

playlistStrightOrder = list(range(0, 4))
playlistMixOrder = list()

while len(playlistMixOrder) < len(playlist):
    currentSongIndex = randint(0, len(playlist) - 1)
    if currentSongIndex not in playlistMixOrder:
        playlistMixOrder.append(currentSongIndex)

print(playlistStrightOrder)
print(playlistMixOrder)

for currentSongIndex in playlistStrightOrder:
    print(playlist[currentSongIndex])

for currentSongIndex in playlistMixOrder:
    print(playlist[currentSongIndex])
