window.onload = function(){
	jsxel.init(100,100,5);
	for(i=1;i<10;i++){
		for(j=1;j<10;j++){
			jsxel.frect(i,j,5,5,jsxel.color[jsxel.random(0,15)]);
		}
	}
};
