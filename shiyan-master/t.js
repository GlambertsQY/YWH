var ti = $("body");
var video = $(".catalogue_ul1 li[id*=video-]");
var i = 1;
var v = 1;
var flag = 0;
video.css("color", "blue");
console.log("已选取" + video.length + "个小节,并已用蓝色标明,请检查是否有遗漏,如有遗漏,概不负责");
// if (document.getElementsByClassName('currentTime')[0].textContent === document.getElementsByClassName('duration')[0].textContent)
//     document.getElementById('playButton').click();
setTimeout(function () {
    $('.speedTab15').click();
    $('.volumeIcon').click();
    console.log("已进行静音和1.5倍加速");
}, 3000);
ti.on("DOMNodeInserted", function (e) {
    if (e.target.textContent == "关闭") {
        console.log("检测到第" + i + "个弹题窗口");
        window.setTimeout(function () {
            document.getElementById("tmDialog_iframe").contentWindow.document.getElementsByClassName("answerOption")[0].getElementsByTagName("input")[0].click();
            $(".popbtn_cancel").click();
            console.log("已关闭");
            flag = 0;
            console.log('flag : ' + flag);
            console.log('i : ' + i);
        }, 3000);
        i++;
        console.log('i : ' + i);
    } else if (document.getElementsByClassName('currentTime')[0].textContent === document.getElementsByClassName('duration')[0].textContent
        && flag === 0) {
        flag = 1;
        console.log('flag : ' + flag);
        console.log("检测到视频观看完成，准备跳到下一节");
        $('.next_lesson_bg').find('a').trigger('click');
        console.log("已跳转");
        setTimeout(function () {
            if (document.getElementsByClassName('currentTime')[0].textContent === document.getElementsByClassName('duration')[0].textContent)
                $('.playButton').click();
            $('.volumeIcon').click();
            $('.speedTab15').click();
            console.log("已进行静音和1.5倍加速");
        }, 6000);
        v++;
        console.log("目前播放了" + v + "个视频");
    }
});