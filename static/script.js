// 微信 JSSDK 配置
wx.config({
    debug: false,
    appId: 'yourAppId',
    timestamp: 'yourTimestamp',
    nonceStr: 'yourNonceStr',
    signature: 'yourSignature',
    jsApiList: ['updateAppMessageShareData', 'updateTimelineShareData']
});

// 微信分享 QQ 音乐链接
function shareMusicToWeChat(songId) {
    const musicUrl = `https://y.qq.com/n/ryqq/songDetail/${songId}`;
    wx.updateAppMessageShareData({
        title: '推荐好听的音乐',
        desc: '来自音乐漂流瓶的分享',
        link: musicUrl,
        imgUrl: 'https://y.qq.com/favicon.ico', // QQ音乐的图标
        success: function () {
            alert('分享成功！');
        }
    });
}


// 显示指定的弹窗
function showPopup(popupId) {
    hideAllPopups();
    document.getElementById(popupId).style.display = "block";
}

// 隐藏指定的弹窗
function closePopup(popupId) {
    document.getElementById(popupId).style.display = "none";
}

// 隐藏所有弹窗
function hideAllPopups() {
    document.querySelectorAll(".popup").forEach(popup => popup.style.display = "none");
}

// 显示“捡瓶子”的弹窗
// function pickBottle() {
//     hideAllPopups();
//     $.get("/pick_music", function(data) {
//         if (data.error) {
//             alert(data.error);
//         } else {
//             const songInfo = `${data.song_name} - ${data.artist_name}`;
//             document.getElementById("song-info").innerText = `歌曲: ${songInfo}`;
//             showPopup('pick-popup');
//         }
//     });
// }

// function pickBottle() {
//     hideAllPopups();
//     $.get("/pick_music", function(data) {
//         if (data.error) {
//             alert(data.error);
//         } else {
//             // 获取歌曲信息
//             const songInfo = `${data.song_name} - ${data.artist_name}`;
//             const searchUrl = `https://y.qq.com/n/ryqq/search?w=${encodeURIComponent(data.song_name)}`;

//             // 更新弹窗内容
//             document.getElementById("song-info").innerText = `歌曲: ${songInfo}`;
            
//             // 动态生成 QQ 音乐链接
//             const songLinkElement = document.getElementById("song-link");
//             songLinkElement.innerHTML = `<a href="${searchUrl}" target="_blank">在QQ音乐中搜索此歌曲</a>`;

//             showPopup('pick-popup');
//         }
//     });
// }

// function pickBottle() {
//     hideAllPopups();
//     $.get("/pick_music", function(data) {
//         if (data.error) {
//             alert(data.error);
//         } else {
//             const songName = data.song_name;
//             const artistName = data.artist_name;

//             // 构造 QQ 音乐搜索链接
//             const searchUrl = `https://y.qq.com/n/ryqq/search?w=${encodeURIComponent(songName)} ${encodeURIComponent(artistName)}`;

//             // 显示歌曲信息
//             document.getElementById("song-info").innerText = `歌曲: ${songName} - ${artistName}`;

//             // 嵌入搜索页面到 iframe 中
//             const player = document.getElementById("music-player");
//             player.src = searchUrl;

//             // 显示弹窗
//             showPopup('pick-popup');
//         }
//     });
// }


// function pickBottle() {
//     hideAllPopups(); // 隐藏所有弹窗
//     $.get("/pick_music", function(data) {
//         if (data.error) {
//             alert(data.error); // 显示错误信息
//         } else {
//             // 获取歌曲信息并显示
//             const songInfo = `${data.song_name} - ${data.artist_name}`;
//             document.getElementById("song-info").innerText = `歌曲: ${songInfo}`;

//             // 为“去听音乐”按钮生成 QQ 音乐搜索链接
//             const searchUrl = `https://y.qq.com/m/client/search/index.html#/searchResult?key=${encodeURIComponent(data.song_name)}%20${encodeURIComponent(data.artist_name)}`;
//             const musicButton = document.getElementById("music-button");
//             musicButton.setAttribute("onclick", `window.location.href='${searchUrl}'`);

//             // 显示弹窗
//             showPopup('pick-popup');
//         }
//     });
// }

// function pickBottle() {
//     hideAllPopups(); // 隐藏所有弹窗

//     // 请求后端接口，获取歌曲信息
//     $.get("/pick_music", function (data) {
//         if (data.error) {
//             alert(data.error); // 显示错误信息
//         } else {
//             // 动态设置歌曲信息
//             const songInfo = `${data.song_name} - ${data.artist_name}`; // 动态生成歌曲信息
//             const songInfoElement = document.getElementById("song-info");
//             songInfoElement.innerText = songInfo;

//             // 动态绑定跳转按钮的点击事件
//             const musicButton = document.getElementById("music-button");
//             musicButton.setAttribute("onclick", `redirectToQQMusic('${songInfo}')`);

//             // 显示弹窗
//             showPopup("pick-popup");
//         }
//     }).fail(function () {
//         alert("无法连接到服务器，请稍后重试。"); // 错误处理
//     });
// }

// function redirectToQQMusic(songInfo) {
//     const appLink = `qqmusic://search?key=${encodeURIComponent(songInfo)}`;
//     console.log("Attempting to redirect to:", appLink);

//     // 创建隐形的 iframe 加载深度链接
//     const iframe = document.createElement("iframe");
//     iframe.style.display = "none";
//     iframe.src = appLink;
//     document.body.appendChild(iframe);

//     // 如果跳转失败，显示提示
//     setTimeout(() => {
//         console.log("Failed to redirect. App might not be installed.");
//         alert("如未安装 QQ 音乐，请先下载并安装后重试。");
//     }, 2000);
// }

// function redirectToQQMusic(songInfo) {
//     // 跳转到中间页面
//     const redirectUrl = `/redirect.html?key=${encodeURIComponent(songInfo)}`;
//     window.location.href = redirectUrl;
// }

function pickBottle() {
    hideAllPopups(); // 隐藏所有弹窗

    // 请求后端接口，获取歌曲信息
    $.get("/pick_music", function (data) {
        if (data.error) {
            alert(data.error); // 显示错误信息
        } else {
            // 动态设置歌曲信息
            const songInfo = `${data.song_name} - ${data.artist_name}`;
            const songInfoElement = document.getElementById("song-info");
            songInfoElement.innerText = songInfo;

            // 显示弹窗
            showPopup("pick-popup");
        }
    }).fail(function () {
        alert("无法连接到服务器，请稍后重试。"); // 错误处理
    });
}



// 显示弹窗
function showPopup(id) {
    document.getElementById(id).style.display = "block";
}

// 关闭弹窗
function closePopup(id) {
    document.getElementById(id).style.display = "none";
}

// 隐藏所有弹窗
function hideAllPopups() {
    const popups = document.querySelectorAll(".popup");
    popups.forEach(popup => popup.style.display = "none");
}


// 显示“丢瓶子”的弹窗
function showSendBottlePopup() {
    showPopup('send-popup');
}

// 发送瓶子并显示成功弹窗
function sendBottle() {
    const songName = document.getElementById("song_name").value.trim();
    const artistName = document.getElementById("artist_name").value.trim();
    const mood = document.getElementById("mood").value.trim();

    if (!songName || !artistName || !mood) {
        alert("请填写所有字段！");
        return;
    }

    $.post("/send_bottle", { song_name: songName, artist_name: artistName, mood: mood }, function(response) {
        if (response.success) {
            hideAllPopups();
            document.getElementById("success-message").innerText = response.message;
            showPopup('success-popup');
        } else {
            alert("发送失败，请重试！");
        }
    });
}

// 显示帮助弹窗
function showHelpPopup() {
    showPopup('help-popup');
}
