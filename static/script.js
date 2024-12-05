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
function pickBottle() {
    hideAllPopups();
    $.get("/pick_music", function(data) {
        if (data.error) {
            alert(data.error);
        } else {
            const songInfo = `${data.song_name} - ${data.artist_name}`;
            document.getElementById("song-info").innerText = `歌曲: ${songInfo}`;
            showPopup('pick-popup');
        }
    });
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
