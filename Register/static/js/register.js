var form1 =document.getElementById("input3");
var scheme=form1.elements["scheme"];
var password1 = document.getElementById("password_based");

   
function check(){
	
	if (scheme.value=="token"){
		if(password1.value==null||password1.value==""){
			alert("请输入密码！");
			password1.focus();
			return false;
		}
	}
	
}

