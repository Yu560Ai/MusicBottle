## MusicBottle

A simple Flask-powered web app that suggests music based on your mood.  
Powered by a JSON database of tracks and a lightweight interface to pick and play songs.

---

### 🚀 Features

- **Mood–based recommendations**  
  Pick from a set of moods and get a curated playlist.  
- **Lightweight**  
  Built with pure Flask and vanilla JavaScript—no heavy frameworks.  
- **Easy to extend**  
  Add new moods or tracks by editing `mood.json` or `music_data.json`.

---

### 🗂️ Repository Structure

```
MusicBottle/
├── app.py                  # Main Flask application
├── music_data.json         # Your library of songs & metadata
├── mood.json               # Available moods and mappings
├── static/
│   ├── css/                # Stylesheets
│   └── js/                 # Client-side scripts
└── templates/
    ├── index.html          # Home page (mood picker)
    └── pick_music.html     # Recommendation results
```

---

### 💻 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Yu560Ai/MusicBottle.git
   cd MusicBottle
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS / Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
   > _If you don’t have a `requirements.txt` yet, you only need Flask:_
   > ```bash
   > pip install Flask
   > ```

---

### ▶️ Usage

1. **Start the server**  
   ```bash
   python app.py
   ```
2. **Open in your browser**  
   Visit `http://localhost:5000/`

3. **Pick your mood**  
   Select a mood and see the recommended tracks.

---

### ⚙️ Configuration

- **Add/Edit Tracks**  
  Open `music_data.json` and follow the existing structure:
  ```json
  [
    {
      "title": "Song Title",
      "artist": "Artist Name",
      "url": "https://path.to/track.mp3"
    },
    ...
  ]
  ```

- **Add/Edit Moods**  
  Modify `mood.json`:
  ```json
  {
    "Happy": ["pop", "dance"],
    "Sad": ["acoustic", "blues"],
    ...
  }
  ```

---

### 🤝 Contributing

1. Fork the repo  
2. Create a feature branch: `git checkout -b feature/YourFeature`  
3. Commit your changes: `git commit -m "Add some feature"`  
4. Push to the branch: `git push origin feature/YourFeature`  
5. Open a Pull Request

Please include tests or manual steps to verify your feature.

---

### 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### 📬 Contact

For questions or suggestions, feel free to open an issue or reach out to the maintainer at  
**dunyinzhang@gmail.com**  

Enjoy the music! 🎵
