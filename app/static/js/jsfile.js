/*
function addLoadEvent(func){
	var oldonload=window.onload;
	if (typeof(oldonload)!="function") {
		window.onload=func;
	} else {
		window.onload=function(){
			oldonload();
			func();
		}
	}
}
*/

function waterFall(parent, pin){
	var oParent=document.getElementById(parent);
	var oPin=oParent.getElementsByClassName(pin);
	var oPinW=oPin[0].offsetWidth;
	var num=Math.floor(document.getElementsByClassName('container')[0].offsetWidth/oPinW);
	oParent.style.width=oPinW*num+"px";
	
	var pinHArr=[];//高度数组
	for (i=0; i<oPin.length; i++) {
		if(i<num){
			pinHArr.push(oPin[i].offsetHeight);
		} else {
			var HMin=Math.min.apply(null, pinHArr);
			var HMinIndex=arrayMinIndex(pinHArr, HMin);
			oPin[i].style.position="absolute";
			oPin[i].style.top=HMin+"px";
			oPin[i].style.left=HMinIndex*oPinW+"px";
			pinHArr[HMinIndex]+=oPin[i].offsetHeight;
		}
	}
}

function arrayMinIndex(arr, value){
	for(var i in arr){
		if (value==arr[i]) {
			return i;
		}
	}
}

function checkHeight(){
	var oParent=document.getElementById("main");
	var oPin=oParent.getElementsByClassName("pin");
	var lastPin=oPin[oPin.length-1];
	var oPinH=lastPin.offsetTop+Math.floor(lastPin.offsetHeight);
	var height=(document.documentElement.scrollTop || document.body.scrollTop) + (document.documentElement.clientHeight || document.body.clientHeight);
//	console.log(height)
	return (oPinH<=height)?true:false;
}

function scrollShow(dataInt){
	if(checkHeight()){
	// var dataInt = get_scroll_source();
	// console.log(dataInt);

	var oParent=document.getElementById("main");
	for(var i=0; i<dataInt.length; i++){
		var oBox=document.createElement("div");
		var oPin=document.createElement("div");
		var oLink=document.createElement("a");
		var img=document.createElement("img");
		img.setAttribute("src", dataInt[i]);
		img.className="example-image";
		oLink.setAttribute("href", dataInt[i]);
		oLink.setAttribute("data-lightbox", "example-set");
		oLink.setAttribute("data-title", "The next image in the set is preloaded as you're viewing.");
		oLink.className="example-image-link";
		oBox.className="box";
		oPin.className="pin";
		oLink.appendChild(img);
		oBox.appendChild(oLink);
		oPin.appendChild(oBox);
		oParent.appendChild(oPin);
	}
	waterFall("main", "pin");
	}
}

function get_scroll_source() {
    var count = $('div.pin').length;
    $.ajax({
        url: '/gallery/api/gallery/more',
        type: 'get',
        dataType: 'json',
        data: {'count': count},
        success: function (data) {
            scrollShow(data);
        },
        error: function (e) {
            console.log(e);
        }
    });
}

window.onload=function(){
	waterFall("main", "pin");
	window.onscroll=function(){
		get_scroll_source();
	}
};
