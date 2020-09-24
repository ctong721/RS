w = 70;
h = 110;
x = 0;
y = 0;
p1 = f(w,h,10000,1000);
user = [{'name':'u1','x':30,'y':40,'zt':1,'color':8,'eat':0},
{'name':'u2','x':35,'y':50,'zt':1,'color':4,'eat':0},
{'name':'u3','x':30,'y':60,'zt':1,'color':5,'eat':0}]

function f(w,h,s,e){
	var point = [];
	for(i=0;i<w;i++){
		var tmp = [];
		for(j=0;j<h;j++){
			tmp[j] = 0;
		}
		point[i] = tmp;
	}
	for(i=0;i<w;i++){
		for(j=0;j<h;j++){
			point[i][j] = jsxel.random(9,12);
		}
	}
	for(i=0;i<s;i++){
		point[jsxel.random(0,w)][jsxel.random(0,h)] = 11;
	}
	for(i=0;i<e;i++){
		point[jsxel.random(0,w)][jsxel.random(0,h)] = 9;
	}
	return point;
}

function move(p1,user){
	for(i=0;i<user.length;i++){
		var zt = [0,0,0,0];
        var cz = [];
        var zx = -1;
        zt[0] = p1[user[i].x+1][user[i].y];
        zt[1] = p1[user[i].x][user[i].y+1];
        zt[2] = p1[user[i].x-1][user[i].y];
        zt[3] = p1[user[i].x][user[i].y-1];
		for(j=0;j<4;j++){
			if(zt[j]==11||zt[j]==9){
                cz.push(j);
			}
		}
		//console.log("cz len:"+cz.length);
		if(cz.length != 0){
            zx = cz[jsxel.random(-1,cz.length)];
		}
		//console.log("zx:"+zx);
		if(zx >= 0){
            if(zx == 0){
                user[i].x = user[i].x+1;
			}else if(zx == 1){
                user[i].y = user[i].y+1;
			}else if(zx == 2){
                user[i].x = user[i].x-1;
			}else if(zx == 3){
                user[i].y = user[i].y-1;
			}
		}
		if(p1[user[i].x][user[i].y] == 9){
            user[i].eat = user[i].eat+1;
            p1[user[i].x][user[i].y] = 11;
		}
		for(j=0;j<user.length;j++){
            if(j != i){
                if(user[i].x == user[j].x){
                    if(user[i].y == user[j].y){
                        if(user[i].eat > user[j].eat){
                            user[j].zt = 0;
                        }else if(user[i]['eat']<user[j]['eat']){
                            user[i].zt = 0;
						}
					}
				}
			}
		}
	}
}


window.onload = function(){
	jsxel.init(w,h,5);
	jsxel.touchstart(function(){
		x = Math.floor(jsxel.e.touches[0].clientX);
		y = Math.floor(jsxel.e.touches[0].clientY);
	});
	jsxel.touchmove(function(){
		x = Math.floor(jsxel.e.touches[0].clientX);
		y = Math.floor(jsxel.e.touches[0].clientY);
	});
	function draw(){
		jsxel.cls("#ffffff");
		move(p1,user);
		for(i=0;i<w;i++){
			for(j=0;j<h;j++){
				jsxel.frect(i,j,1,1,jsxel.color[p1[i][j]]);
			}	
		}
		for(i=0;i<user.length;i++){
			if(user[i].zt == 1){
				jsxel.frect(user[i].x,user[i].y,1,1,jsxel.color[user[i].color]);
			}
		}
		jsxel.text(10,30,jsxel.frame_count,jsxel.color[1])
		jsxel.text(100,30,user[0].eat,jsxel.color[user[0].color])
		jsxel.text(150,30,user[1].eat,jsxel.color[user[1].color])
		jsxel.text(200,30,user[2].eat,jsxel.color[user[2].color])
		jsxel.text(250,30,x,jsxel.color[1])
		jsxel.text(300,30,y,jsxel.color[1])
	}
	jsxel.run(draw);
};
