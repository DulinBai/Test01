var form =document.getElementById("input");
var token=form.elements["state1"];
var password=form.elements["password"];
var file=form.elements["file"];

   
function check(){
	if (token.value=="token"){
		if(password.value==null||password.value==""){
			alert("请输入密码！");
			password.focus();
			return false;
		}
	}
	else{
		if(file.value==null||file.value==""){
			alert("请上传证书文件！");
			return false;
		}
	}
}
