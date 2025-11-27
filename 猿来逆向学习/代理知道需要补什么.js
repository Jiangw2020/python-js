// 全局异常断点


// var window = {
//     name: "樵夫",
//     age: 18,
//     chi:function(){
//         console.log("樵夫爱吃东西");
//         return 123;
//     }
// }
//
// window = new Proxy(window, {
//     // handler: 具体发生什么操作, 要被劫持
//     // 从该对象获取数据的时候. 自动拦截
//     // target目标对象,
//     // pro属性名
//     get(target, pro, receiver){
//         // return obj[pro] ;   // 死循环
//         // 反射 -> 你可以理解成就是从目标对象中获取某个属性, (可以忽略掉代理)
//         var val = Reflect.get(target, pro, receiver);
//         console.log("在代理中获取到了", pro, val);
//         return val;
//     },
//     set(target, pro, value, receiver){
//         console.log("给对象,设置属性", pro, "=", value);
//         Reflect.set(target, pro, value, receiver);
//     },
//     apply(target, thisArg, arg_list){
//         console.log("有人调用函数了, ")
//         var ret = Reflect.apply(target, thisArg, arg_list);
//         console.log("函数执行完了, 结果是 ", ret);
//         return ret;
//     }
// });



function obj_proxy(obj, name){
    return new Proxy(obj, {
        get(target, pro, rece){
            var val = Reflect.get(target, pro, rece);
            console.log("从",  name, "获取", pro, "该属性的值是", val);
            if (typeof val == 'object'){
                return obj_proxy(val, pro); // 灵魂~~~ 777777 999
            } else if(typeof val == 'function'){
                return func_proxy(val, pro);
            }
            return val;
        },
        set(target, pro, val, rece){
            console.log("向",  name, "设置", pro, "该属性的值是", val);
            Reflect.set(target, pro, val, rece);
        }
    });
}

function func_proxy(func, name){
    return new Proxy(func, {
        apply(target, thisArg, arg_list){
             var ret = Reflect.apply(target, thisArg, arg_list);
             console.log("调用了"+name+"函数", "函数的返回值是", ret);
             if (typeof ret == 'object'){
                return obj_proxy(ret, name+"的返回值"); // 灵魂~~~ 777777 999
             } else if(typeof ret == 'function'){
                return func_proxy(ret, name+"的返回值");
             }
             return ret;
        }
    })
}

var window = obj_proxy({}, "window");
var navigator = obj_proxy({
    userAgent: "樵夫的浏览器",
    plugins: {
        abc:{
            def:{}
        },
        chi: function(){
            return {
                hehe: "嘿嘿",
                miao:{
                    duomiao: "很秒"
                }
            }
        }
    },
},"navigator");
var document =  obj_proxy({},"document");
window.navigator = navigator;
window.document = document
//
// console.log(window.navigator.plugins.abc.def);

window.navigator.plugins.chi()['miao']['duomiao']
// console.log(window.navigator.plugins.chi()['miao']['duomiao']);
// console.log(window.document.aa)
