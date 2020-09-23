window.onload = function(){
	jsxel.init(61,51,6);
	function draw(){
		jsxel.cls("#ffffff");
		for(i=0;i<60;i++){
			for(j=0;j<50;j++){
				jsxel.frect(i,j,1,1,jsxel.color[jsxel.random(0,15)]);
			}	
		}	
	}
	jsxel.run(draw);
};
