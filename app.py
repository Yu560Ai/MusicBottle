from flask import Flask, render_template, request, jsonify
import random
import json
import hashlib

app = Flask(__name__)

# 微信公众号验证接口
@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    if request.method == 'GET':
        # 验证微信服务器身份
        token = 'leleyuhan2024'  # 与微信公众号后台配置的 Token 一致
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')

        # 验证签名
        list_to_hash = [token, timestamp, nonce]
        list_to_hash.sort()
        hashcode = hashlib.sha1(''.join(list_to_hash).encode('utf-8')).hexdigest()

        if hashcode == signature:
            return echostr
        else:
            return "Verification failed", 403

    elif request.method == 'POST':
        # 处理用户消息（比如“捡瓶子”或“丢瓶子”）
        data = request.data  # 接收微信推送的 XML 数据
        # 解析 XML 并返回响应消息（后续实现）
        return "success"

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
    app.run(host="0.0.0.0", port=80, debug=True)
