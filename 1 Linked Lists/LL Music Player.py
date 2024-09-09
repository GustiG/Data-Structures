#   Practice - Music Player           from codechef.com
class Node:
    def __init__(self, songId):
        self.songId = songId
        self.prev = None
        self.next = None

class MusicPlayer:
    def __init__(self):
        self.head = None
        self.currentSong = None

    # Function to add a song to the end of the list
    def addSong(self, songId):
        # Complete this function
        new_song = Node(songId)
        if not self.head:
            self.head = new_song
            self.currentSong = new_song
            return
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            new_song.prev = curr
            curr.next = new_song

# Function to play the next song
    def playNext(self):
        # Complete this function
        if self.currentSong.next:
            self.currentSong = self.currentSong.next
        
    # Function to play the previous song
    def playPrev(self):
        # Complete this function
        if self.currentSong.prev:
            self.currentSong = self.currentSong.prev

        
    # Function to switch to a specific song
    def switchSong(self, songId):
        # Complete this function
        temp = self.head
        while temp is not None:
            if temp.songId == songId:
                self.currentSong = temp
                return
            temp = temp.next
        
        
    # Function to return the songId of the current song playing
    def current(self):
        # Complete this function
        return self.currentSong.songId
        
# Main function to test the music player -- only on the site
if __name__ == "__main__":
    player = MusicPlayer()
    queries = int(input())
    while queries > 0:
        line = input().split()
        query = int(line[0])

        if query == 1:
            songId = int(line[1])
            player.addSong(songId)
        elif query == 2:
            player.playNext()
        elif query == 3:
            player.playPrev()
        elif query == 4:
            songId = int(line[1])
            player.switchSong(songId)
        elif query == 5:
            print(player.current())
        else:
            print("Invalid query!")
        queries -= 1
