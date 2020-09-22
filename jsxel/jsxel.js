jsxel = {
	color: ["#000000","#1D2B53","#7E2553","#008751",
			"#AB5236","#5F574F","#C2C3C7","#FFF1E8",
			"#FF004D","#FFA300","#FFEC27","#00E436",
			"#29ADFF","#83769C","#FF77AB","#FFCCAA"],
	scale: 5,
	
	init: function(w,h){
		c = document.createElement("canvas");
		c.width = w;
		c.height = h;
		ctx = c.getContext("2d");
		document.body.appendChild(c);
	},
	
	rect: function(x,y,w,h,col,lw){
		ctx.strokeStyle = col;
		ctx.lineWidth = lw;
		ctx.strokeRect(x,y,w,h);
	},
	
	frect: function(x,y,w,h,col){
		ctx.fillStyle = col;
		ctx.fillRect(x,y,w,h);
	},
	
	text: function(x,y,t,col,f="20px Verdana"){
		ctx.font = f;
		ctx.strokeStyle = col;
		ctx.strokeText(t,x,y);
	},
	
};