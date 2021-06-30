//获取系统时间
window.onload = function(){
    var myDate = new Date();//获取系统当前时间
    var mon = myDate.getMonth() + 1;
    var day = myDate.getDay();
    switch (day) {
        case 0:d = "星期天";break;
        case 1:d = "星期一";break;
        case 2:d = "星期二";break;
        case 3:d = "星期三";break;
        case 4:d = "星期四";break;
        case 5:d = "星期五";break;
        case 6:d = "星期六";break;

    }
    /*
     1 myDate.getYear(); //获取当前年份(2位)
     2 myDate.getFullYear(); //获取完整的年份(4位,1970-????)
     3 myDate.getMonth(); //获取当前月份(0-11,0代表1月)
     4 myDate.getDate(); //获取当前日(1-31)
     5 myDate.getDay(); //获取当前星期X(0-6,0代表星期天)*/
    //alert(myDate.getFullYear()+"/"+mon+"/"+myDate.getDate()+" "+d);
    document.getElementById("getTime").innerHTML = myDate.getFullYear()+"/"+mon+"/"+myDate.getDate()+" "+d;

}

function changeC(id, flag){
    if(flag == "over") {
        document.getElementById(id).style.color = "yellow";
        document.getElementById(id).style.textDecoration = "underline ";

    }else if(flag == "out"){
        document.getElementById(id).style.color = "";
        document.getElementById(id).style.textDecoration = "none";
    }

}
function showType(){//bLeftBottom_3   hidden_info
    document.getElementById("hidden_info").style.display="block";
}
function hideType(){//bLeftBottom_3   hidden_info
    document.getElementById("hidden_info").style.display="none";
}
function c1() {
    document.getElementById("i1").src="img/img/vm11.gif";
    document.getElementById("i2").src="img/img/vm2.gif";
    document.getElementById("xx").style.display = "block";
    document.getElementById("yy").style.display = "none";
}
function c2() {
    document.getElementById("i2").src="img/img/vm21.gif";
    document.getElementById("i1").src="img/img/vm1.gif";
    document.getElementById("xx").style.display = "none";
    document.getElementById("yy").style.display = "block";
}
function checkBuyNum(){
    var bnum = document.getElementById("buyNum");
    // alert(bnum.value);
    if(bnum.value == 0){

        document.getElementById("tips").innerHTML = "不能再少了！";
        document.getElementById("btn1").disabled=true;
    }
    else if(bnum.value > 20){

        document.getElementById("tips").innerHTML = "太多啦！";
        document.getElementById("btn1").disabled=true;
    }
    else{
        document.getElementById("tips").innerHTML = "";
        document.getElementById("btn1").disabled=false;
    }
}
function changeInfo(id) {
    switch (id) {
        case "card1":
            for(var i=1;i<6;i++){
                if(i!=1){
                    document.getElementById("card"+i).style.borderColor="darkgray";
                    document.getElementById("info"+i).style.display="none";
                }
                else{
                    document.getElementById("info"+i).style.display="block";
                    document.getElementById("card"+i).style.borderColor="darkgray darkgray white darkgray";
                }
            }
            break;
        case "card2":

            for(var i=1;i<6;i++){
                if(i!=2){
                    document.getElementById("card"+i).style.borderColor="darkgray";
                    document.getElementById("info"+i).style.display="none";
                }
                else{
                    document.getElementById("info"+i).style.display="block";
                    document.getElementById("card"+i).style.borderColor="darkgray darkgray white darkgray";
                }
            }

            break;
        case "card3":

            for(var i=1;i<6;i++){
                if(i!=3){
                    document.getElementById("card"+i).style.borderColor="darkgray";
                    document.getElementById("info"+i).style.display="none";
                }
                else{
                    document.getElementById("info"+i).style.display="block";
                    document.getElementById("card"+i).style.borderColor="darkgray darkgray white darkgray";
                }
            }
            break;
        case "card4":
            for(var i=1;i<6;i++){
                if(i!=4){
                    document.getElementById("card"+i).style.borderColor="darkgray";
                    document.getElementById("info"+i).style.display="none";
                }
                else{
                    document.getElementById("info"+i).style.display="block";
                    document.getElementById("card"+i).style.borderColor="darkgray darkgray white darkgray";
                }
            }
            break;
        case "card5":

            for(var i=1;i<6;i++){
                if(i!=5){
                    document.getElementById("card"+i).style.borderColor="darkgray";
                    document.getElementById("info"+i).style.display="none";
                }
                else{
                    document.getElementById("info"+i).style.display="block";
                    document.getElementById("card"+i).style.borderColor="darkgray darkgray white darkgray";
                }
            }
            break;
    }

}
function changebigImg() {
    var imgEle = document.getElementById("bigImg");
    imgEle.src = event.srcElement.src;

}
function showBigImg() {
    document.getElementById("showBigImg").style.display="block";
    bigImgEle = document.getElementById("bigImgShow");
    bigImgEle.src = event.srcElement.src;

    // alert("yy");
}
function hiddenBigImg() {
    document.getElementById("showBigImg").style.display="none";
}
function Mmove(){
    //放大镜中的图片
    var obj = document.getElementById("bigImgShow");
    //获取鼠标相对位移
    var offx = obj.width/event.srcElement.width;
    var offy = obj.height/event.srcElement.height;
    //获取放大镜外div容器
    var div = document.getElementById("showBigImg");
    div.scrollLeft = (event.offsetX*offx);
    div.scrollTop = (event.offsetY*offy);


}
//JQ
$(function(){
    //设置定时任务
    for(var i=1;i<12;i++){
        $("#num").append("<li>"+i+"</li>");
    }
    $("#num li").eq(0).css("background-color","yellow").siblings("li").css("background-color","darkgray");

    setInterval("changeImg()", 3000);
    //点击下方数字更换图片
    $("#num li").click(function(){
        $("#img1").attr("src", "img/Wrzcnet/"+$(this).text()+".jpg").css("width","100%").css("height","100%");
        $("#num li").eq($(this).text()-1).css("background-color","yellow").siblings("li").css("background-color","darkgray");

        // alert($(this).text());

    });
    //提交按钮状态切换
    $("#agree").change(function(){
        if($("#agree").prop("checked")){
            $("#submit").prop('disabled',false);//按钮可用
        }
        else{
            $("#submit").prop('disabled',true);//按钮可用
        }
    });
    //验证表单
    $("#regForm").validate({
            rules:{
                username:{
                    required:true,
                    minlength:3
                },
                password1:{
                    required:true,
                    minlength:6
                },
                password2:{
                    required:true,
                    equalTo:"#password1"
                },
                email:{
                    required:true,
                    email:true
                }
            }
        }

    );
    //登录页面用户信息验证
    //验证用户名
    $("#log_username").blur(function(){//离焦时判断是否为空\\
        var len = $(this).val().length;
        var pattern_chin =/^[\u4E00-\u9FA5A-Za-z0-9_]+$/;
        if(!pattern_chin.test($(this).val())&&len>0){
            $("#uTips").text("含非法字符！");

        }
        else if(len== 0){
            $("#uTips").text("用户名不能为空！");
        }
        else if(len <3){
            $("#uTips").text("长度不能少于3位！");

        }
        // 中文、英文、数字包括下划线：^[\u4E00-\u9FA5A-Za-z0-9_]+$

        else{
            $("#uTips").text("");
        }


    });
    //验证密码
    $("#log_password").blur(function(){//离焦时判断是否为空\\
        var len = $(this).val().length;
        var pattern_chin =/^[\u4E00-\u9FA5A-Za-z0-9_]+$/;
        //中文、英文、数字包括下划线：^[\u4E00-\u9FA5A-Za-z0-9_]+$
        if(!pattern_chin.test($(this).val())&&len>0){

            $("#pTips").text("含非法字符！");
        }
        else if(len== 0){
            $("#pTips").text("密码不能为空！");
        }
        else if(len < 6){
            $("#pTips").text("长度不能少于6位！");
        }

        else{
            $("#pTips").text("");
        }



    });


});
var i=1;
function changeImg(){

    i++;
    //("img/Wrzcnet/"+i+".jpg");
    $("#img1").attr("src", "img/Wrzcnet/"+i+".jpg").css("width","100%").css("height","100%");
    if(i==11){
        i=0;
    }
    $("#num li").eq(i-1).css("background-color","yellow").siblings("li").css("background-color","darkgray");


}
function checkBuyNum(){
    var bnum = document.getElementById("buyNum");
    // alert(bnum.value);
    if(bnum.value == 0){

        document.getElementById("tips").innerHTML = "不能再少了！";
        document.getElementById("btn1").disabled=true;
    }
    else if(bnum.value < 20){
        document.getElementById("tips").innerHTML = "您在开玩笑吗？？？？？？";
        document.getElementById("btn1").disabled=true;
    }
    else if(bnum.value > 20){

        document.getElementById("tips").innerHTML = "太多啦！";
        document.getElementById("btn1").disabled=true;
    }
    else{
        document.getElementById("tips").innerHTML = "";
        document.getElementById("btn1").disabled=false;
    }
}
function changeInfo(id) {
    switch (id) {
        case "card1":
            for(var i=1;i<6;i++){
                if(i!=1){
                    document.getElementById("card"+i).style.borderColor="darkgray";
                    document.getElementById("info"+i).style.display="none";
                }
                else{
                    document.getElementById("info"+i).style.display="block";
                    document.getElementById("card"+i).style.borderColor="darkgray darkgray white darkgray";
                }
            }
            break;
        case "card2":

            for(var i=1;i<6;i++){
                if(i!=2){
                    document.getElementById("card"+i).style.borderColor="darkgray";
                    document.getElementById("info"+i).style.display="none";
                }
                else{
                    document.getElementById("info"+i).style.display="block";
                    document.getElementById("card"+i).style.borderColor="darkgray darkgray white darkgray";
                }
            }

            break;
        case "card3":

            for(var i=1;i<6;i++){
                if(i!=3){
                    document.getElementById("card"+i).style.borderColor="darkgray";
                    document.getElementById("info"+i).style.display="none";
                }
                else{
                    document.getElementById("info"+i).style.display="block";
                    document.getElementById("card"+i).style.borderColor="darkgray darkgray white darkgray";
                }
            }
            break;
        case "card4":
            for(var i=1;i<6;i++){
                if(i!=4){
                    document.getElementById("card"+i).style.borderColor="darkgray";
                    document.getElementById("info"+i).style.display="none";
                }
                else{
                    document.getElementById("info"+i).style.display="block";
                    document.getElementById("card"+i).style.borderColor="darkgray darkgray white darkgray";
                }
            }
            break;
        case "card5":

            for(var i=1;i<6;i++){
                if(i!=5){
                    document.getElementById("card"+i).style.borderColor="darkgray";
                    document.getElementById("info"+i).style.display="none";
                }
                else{
                    document.getElementById("info"+i).style.display="block";
                    document.getElementById("card"+i).style.borderColor="darkgray darkgray white darkgray";
                }
            }
            break;
    }

}
function changebigImg() {
    var imgEle = document.getElementById("bigImg");
    imgEle.src = event.srcElement.src;

}
function showBigImg() {
    document.getElementById("showBigImg").style.display="block";
    bigImgEle = document.getElementById("bigImgShow");
    bigImgEle.src = event.srcElement.src;

    // alert("yy");
}
function hiddenBigImg() {
    document.getElementById("showBigImg").style.display="none";
}
function Mmove(){
    //放大镜中的图片
    var obj = document.getElementById("bigImgShow");
    //获取鼠标相对位移
    var offx = obj.width/event.srcElement.width;
    var offy = obj.height/event.srcElement.height;
    //获取放大镜外div容器
    var div = document.getElementById("showBigImg");
    div.scrollLeft = (event.offsetX*offx);
    div.scrollTop = (event.offsetY*offy);


}
