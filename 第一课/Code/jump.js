	var width;
	var roleX=0;
	var roleY = 300;
	var power = 0;
	var pillarsArray  = [0, 200,400,550,800,1150];
	document.onkeydown=keydown;
	document.onkeyup=keyup;
	
	function right_move(powerLocal)
	{	
		var times = 0;
		// for (times =0; times<=powerLocal; times++) {
		// 	if( x < width -100){
		// 		x += 20;
		// 	}
		// 	document.getElementById("role").style.left=x + "px";
		// }
		// dropDown();
		var interval = setInterval(() => {
			if( roleX < width -100){
				roleX += 20;
			}
			document.getElementById("role").style.left=roleX + "px";
			if (times >= powerLocal) {
				dropDown();
				clearInterval(interval);
			}
			times++;
		},20)
	}
	function keydown(e)//e是火狐下的隐藏对象，相当于IE下的event
	{
		var ev=e || window.event;//兼容火狐和IE,
		//使用 || 运算符的好处是，当e可用时，ev=e,既火狐浏览器下，
		//非火狐浏览器时e为undefined，ev=window.event，既IE和webkit浏览器
		if(ev.keyCode==32)
		{
			power++;
		}
	}
	function keyup(e)
	{
		var ev=e || window.event;
		if(ev.keyCode==32)
		{
			right_move(power);
			power = 0;
		}
	}

	function setPillar() {
		var border = document.getElementById("border");
        for (var i = 0; i < pillarsArray.length; i++) {
			var pillar = document.createElement('div');
			pillar.className = "pillar"
			border.appendChild(pillar);
			pillar.style.left = pillarsArray[i] + "px";
		}
	}

	function dropDown() {
		var isDrop = true;
        var pillowIndex = 0;
		for(var i = 0; i<pillarsArray.length; i++) {
			if((roleX+50)>pillarsArray[i] && (roleX+10)<(pillarsArray[i]+80)){
				isDrop = false;
                pillowIndex = i;
                break;
			}
		}
		if (isDrop === true){
			var interval = setInterval(() => {
				roleY -= 20;
				document.getElementById("role").style.bottom= roleY + "px";
				if (roleY < -80) {
					alert("game over!");
					clearInterval(interval);
					location.reload();
				}
			},20)
		} else if (pillowIndex === pillarsArray.length - 1) {
            alert("you win!!!\r\ncongratulations!!!");
            location.reload();
        }
	}

	window.onload = function()
	{
		width = document.getElementById('border').offsetWidth;
		setPillar();
	}