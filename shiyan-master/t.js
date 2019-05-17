var secondsInit = 0;
var hdflag = 0;
var login_flag = "1";

function _fresh() {
    secondsInit++;
    var seconds = secondsInit;
    var result = '';
    if (seconds >= 3600) {
        var h = Math.floor(seconds / 3600);
        result += h + "小时";
        seconds -= 3600 * h;
    }
    if (seconds >= 60) {
        var m = Math.floor(seconds / 60);
        result += m + "分";
        seconds -= 60 * m;
    }
    result += seconds + "秒";
    document.getElementById('_lefttime').innerHTML = result;

    if ((hdflag % 60) === 0) {
        $.post("exam_xuexi_online.php", {
            "cmd": 'xuexi_online'
        }, function (data) {
            data = eval('(' + data + ')');
            if (data.status === 1) {
                $('#xuexi_online').html(data.shichang);
            }
        });
    }

    if (hdflag > 300) {
        if (confirm("您已经在此页面5分钟了，是否继续？")) {
            hdflag = 0;
        }
    }
    hdflag++;

}

if (login_flag) {
    _fresh()
    setInterval(_fresh, 1000);
}


