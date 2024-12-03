from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)

# Load music data
with open('music_data.json', 'r', encoding='utf-8') as f:
    music_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')  # Render the index page

@app.route('/pick_music/', methods=['GET'])
def pick_bottle():
    song = random.choice(music_data)  # Pick a random song
    return render_template('pick_music.html', song=song)  # Render the pick_music page

@app.route('/send_bottle/', methods=['POST'])
def send_bottle():
    song_name = request.form['song_name']
    artist_name = request.form['artist_name']
    music_data.append({"song_name": song_name, "artist_name": artist_name})
    
    # Save updated music data
    with open('music_data.json', 'w', encoding='utf-8') as f:
        json.dump(music_data, f, ensure_ascii=False, indent=4)
        
    return render_template('success.html')  # Render the form page


@app.route('/send_bottle_form', methods=['GET'])
def send_bottle_form():
    return render_template('send_bottle_form.html')  # Render the form page


if __name__ == "__main__":
    app.run(debug=True)
