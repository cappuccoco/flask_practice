
// 判定页码
$(document).ready(
    function () {
        var num = data1.pageNum
        var totalnum = data2.totalPageNum

        if (num === 1 ){
            $("#up").hide()
        }

        if (num === totalnum){
            $("#down").hide()
        }

        $("#test").html(num,totalnum)
    }
)







