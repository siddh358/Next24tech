import tkinter as tk
from tkinter import messagebox
import lyricsgenius

class LyricsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lyrics Finder")
        
        # Labels and entry fields
        self.artist_label = tk.Label(root, text="Artist Name:")
        self.artist_label.pack()
        self.artist_entry = tk.Entry(root, width=50)
        self.artist_entry.pack()
        
        self.song_label = tk.Label(root, text="Song Title:")
        self.song_label.pack()
        self.song_entry = tk.Entry(root, width=50)
        self.song_entry.pack()
        
        # Fetch lyrics button
        self.fetch_button = tk.Button(root, text="Fetch Lyrics", command=self.fetch_lyrics)
        self.fetch_button.pack()
        
        # Text box to display lyrics
        self.lyrics_text = tk.Text(root, wrap='word', height=20, width=60)
        self.lyrics_text.pack()
        
        # Genius API client
        self.genius = lyricsgenius.Genius("YOUR_GENIUS_API_ACCESS_TOKEN")
        
    def fetch_lyrics(self):
        artist = self.artist_entry.get()
        song = self.song_entry.get()
        
        if not artist or not song:
            messagebox.showerror("Input Error", "Please enter both artist and song title")
            return
        
        try:
            song_lyrics = self.genius.search_song(song, artist)
            if song_lyrics:
                self.lyrics_text.delete(1.0, tk.END)
                self.lyrics_text.insert(tk.END, song_lyrics.lyrics)
            else:
                messagebox.showinfo("No Lyrics Found", "Could not find lyrics for the song.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LyricsApp(root)
    root.mainloop()
