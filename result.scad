module a(){difference(){
    cube(size=[20, 20, 6]);
    translate(v=[0, 0, -0.1]){
        linear_extrude(height=7){
            union(){
                translate(v=[0, 0, 0]){
                    translate(v=[5, 5, 0]){
                        circle(r=1.5, d=3, $fn=100);
                    };
                };
                translate(v=[0, 10, 0]){
                    translate(v=[5, 5, 0]){
                        circle(r=1.5, d=3, $fn=100);
                    };
                };
                translate(v=[10, 0, 0]){
                    translate(v=[5, 5, 0]){
                        circle(r=1.5, d=3, $fn=100);
                    };
                };
                translate(v=[10, 10, 0]){
                    translate(v=[5, 5, 0]){
                        circle(r=1.5, d=3, $fn=100);
                    };
                };
            };
        };
    };
};
};
projection() a();