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

# @app.route('/pick_music/', methods=['GET'])
# def pick_bottle():
#     song = random.choice(music_data)  # Pick a random song
#     return render_template('pick_music.html', song=song)  # Render the pick_music page

@app.route('/pick_music/', methods=['GET'])
def pick_bottle():
    song = random.choice(music_data)  # Pick a random song
    print(song)  # 在终端打印返回的歌曲信息
    return jsonify(song)  # Return the song data as JSON


@app.route('/send_bottle/', methods=['POST'])
def send_bottle():
    song_name = request.form['song_name']
    artist_name = request.form['artist_name']

    # 数据验证：确保 song_name 和 artist_name 都非空，并且没有恶意输入
    if not song_name or not artist_name:
        return render_template('error.html', error_message="歌曲名和歌手名不能为空。")
    
    # 清理输入（去除空格，避免恶意空格注入）
    song_name = song_name.strip()
    artist_name = artist_name.strip()

    # 检查是否已存在该歌曲（根据歌曲名和歌手名组合来判断）
    if any(song['song_name'] == song_name and song['artist_name'] == artist_name for song in music_data):
        return render_template('error.html', error_message="这首歌已经存在，请勿重复添加。")

    music_data.append({"song_name": song_name, "artist_name": artist_name})
    
    # Save updated music data
    with open('music_data.json', 'w', encoding='utf-8') as f:
        json.dump(music_data, f, ensure_ascii=False, indent=4)
        
    return render_template('success.html')  # Render the form page


@app.route('/send_bottle_form', methods=['GET'])
def send_bottle_form():
    return render_template('send_bottle_form.html')  # Render the form page


# Print out all routes in the Flask app
for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == "__main__":
    app.run(debug=True)
