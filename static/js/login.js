function fnLogin() {
    var oUname = document.getElementById("userid")
    var oUpass = document.getElementById("pwd")
    var oError = document.getElementById("error_box")
    var oform = document.getElementById("login_form")
    var isError = true;
    if (oUname.value.length > 20 || oUname.value.length < 6) {
        oError.innerHTML = "用户名请输入6-20位字符";
        isError = false;
        return false;
    }else if((oUname.value.charCodeAt(0)>=48) && (oUname.value.charCodeAt(0)<=57)){
        oError.innerHTML = "首字符必须为字母";
        isError = false;
        return false;
    }else for(var i=0;i<oUname.value.charCodeAt(i);i++){
        if((oUname.value.charCodeAt(i)<48)||(oUname.value.charCodeAt(i)>57) && (oUname.value.charCodeAt(i)<97)||(oUname.value.charCodeAt(i)>122)){
            oError.innerHTML = "必须为字母跟数字组成";
            isError = false;
            return false;
        }
    }

    if (oUpass.value.length > 20 || oUpass.value.length < 6) {
        oError.innerHTML = "密码请输入6-20位字符"
        isError = false;
        return false;
    }

    return true
    // window.alert("正在登录")
    // window.location.href="http://www.baidu.com"
}