
// 查重 通过查重 true 没通过 false
function checkid() {
    var oUid = document.getElementById("userID")
    var id = oUid.value
    $.get(
        "/checkid",
        {'id':id},
        function (data) {
            if (data.check === 'ok'){
                return true
            }
            else {
                return false
            }
        }
    )
}

function fnRegist() {
    var oUid = document.getElementById("userID")
    var oUpass = document.getElementById("pwd")
    var oUpass2 = document.getElementById("pwd2")
    var oUname = document.getElementById("username")
    var oUemail = document.getElementById("email")
    var oError = document.getElementById("error_box")
    var oform = document.getElementById("regist_form")
    var isError = true;

    // 用户id
    if (oUid.value.length > 20 || oUid.value.length < 6) {
        oError.innerHTML = "账号请输入6-20位字符";
        isError = false;
        return false;
    }else if((oUid.value.charCodeAt(0)>=48) && (oUid.value.charCodeAt(0)<=57)){
        oError.innerHTML = "首字符必须为字母";
        isError = false;
        return false;
    }else for(var i=0;i<oUid.value.charCodeAt(i);i++){
        if((oUid.value.charCodeAt(i)<48)||(oUid.value.charCodeAt(i)>57) && (oUid.value.charCodeAt(i)<97)||(oUid.value.charCodeAt(i)>122)){
            oError.innerHTML = "必须为字母跟数字组成";
            isError = false;
            return false;
        }
    }

    // 用户id查重
    // if (checkid() === false){
    //     oError.innerHTML = "账号重复,请换一个";
    //     isError = false;
    //     return false;
    // }
    var id = oUid.value;
    $.post(
        "/checkid",
        {'id':id},
        function (data) {
            if (data.check === 'ok'){
                // return true
            }
            else {
                oError.innerHTML = "账号重复,请换一个";
                isError = false;
                return false;
            }
        }
    )







    //密码
    if (oUpass.value.length > 20 || oUpass.value.length < 6) {
        oError.innerHTML = "密码请输入6-20位字符";
        isError = false;
        return false;
    }

    //密码一致
    if (oUpass.value !== oUpass2.value ){
        oError.innerHTML = "两次密码不一致";
        isError = false;
        return false;
    }

    //用户名
    if (oUname.value.length > 20 || oUname.value.length < 6) {
        oError.innerHTML = "用户名请输入6-20位字符";
        isError = false;
        return false;
    }

    //邮箱格式
    var myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    if(!myreg.test(oUemail.value))
            {
                 oError.innerHTML='邮箱格式有误';
                 isError = false;
                 return false;
            }

    return true
    // window.alert("注册成功,正在跳转登录界面")
    // window.location.href="http://www.baidu.com"
}