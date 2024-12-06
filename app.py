from flask import Flask, render_template, request, jsonify, redirect, url_for
import random
import json
import hashlib
import os
# import requests
# from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/redirect_to_qqmusic')
def redirect_to_qqmusic():
    song_name = request.args.get('song_name', '')
    artist_name = request.args.get('artist_name', '')

    # 构造搜索链接
    search_url = f"https://y.qq.com/n/ryqq/search?w={song_name} {artist_name}"
    return render_template('redirect.html', search_url=search_url)

# @app.route('/get_song_id', methods=['GET'])
# def get_song_id():
#     song_name = request.args.get('song_name')
#     artist_name = request.args.get('artist_name')
#     if not song_name or not artist_name:
#         return jsonify({"error": "缺少歌曲名或歌手名"}), 400

#     # 构造搜索 URL
#     search_url = f"https://y.qq.com/n/ryqq/search?w={song_name} {artist_name}"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
#         "Referer": "https://y.qq.com/",
#         "Accept-Language": "zh-CN,zh;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br"
#     }

#     try:
#         response = requests.get(search_url, headers=headers)
#         if response.status_code != 200:
#             return jsonify({"error": f"无法访问 QQ 音乐搜索页面，状态码: {response.status_code}"}), 500

#         # 使用 BeautifulSoup 解析 HTML
#         soup = BeautifulSoup(response.text, 'html.parser')
#         song_link = soup.find('a', {'class': 'js_song'})  # 找到第一首歌曲链接
#         if not song_link:
#             return jsonify({"error": "未找到相关歌曲"}), 404

#         # 提取 songID
#         song_id = song_link['href'].split('/')[-1]
#         return jsonify({"song_id": song_id})

#     except Exception as e:
#         return jsonify({"error": f"获取歌曲信息时发生错误: {str(e)}"}), 500



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


# Load music data at startup
music_data_file = 'music_data.json'
if os.path.exists(music_data_file):
    with open(music_data_file, 'r', encoding='utf-8') as f:
        music_data = json.load(f)
else:
    music_data = []

# Load mood data at startup
mood_file = 'mood.json'
if os.path.exists(mood_file):
    with open(mood_file, 'r', encoding='utf-8') as f:
        mood_data = json.load(f)
else:
    mood_data = []


@app.route('/')
def index():
    return render_template('index.html')  # Render the index page


@app.route('/pick_music/', methods=['GET'])
def pick_bottle():
    if music_data:
        song = random.choice(music_data)  # Pick a random song
        return jsonify(song)  # Return the song data as JSON
    else:
        return jsonify({'error': 'No music data available'}), 404


@app.route('/send_bottle', methods=['POST'])
def send_bottle():
    # 获取表单数据
    song_name = request.form.get('song_name').strip()
    artist_name = request.form.get('artist_name').strip()
    mood = request.form.get('mood').strip()

    # 检查歌曲是否已存在
    duplicate = any(
        song['song_name'] == song_name and song['artist_name'] == artist_name
        for song in music_data
    )

    if not duplicate:
        # 添加新歌曲到 music_data
        music_entry = {'song_name': song_name, 'artist_name': artist_name}
        music_data.append(music_entry)

        # 写入到 music_data.json
        with open(music_data_file, 'w', encoding='utf-8') as f:
            json.dump(music_data, f, indent=4, ensure_ascii=False)

    # 添加心情到 mood_data
    mood_data.append({'mood': mood,'song_name': song_name, 'artist_name': artist_name})

    # 写入到 mood.json
    with open(mood_file, 'w', encoding='utf-8') as f:
        json.dump(mood_data, f, indent=4, ensure_ascii=False)

    # 返回 JSON 响应，表示发送成功
    return jsonify({"success": True, "message": "瓶子已成功丢出！"})


# @app.route('/send_success')
# def send_success():
#     return render_template('send_success.html')  # Render success page



# Print out all routes in the Flask app
for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

