// sojson是统一框架，不会改变业务逻辑

// 0.抓包找到js文件
// 2.hook setInterval，反调试的setInterval代码后改回去
var setInterval_ = setInterval
setInterval = function (){
    // debugger
}
// 3.抓包工具替换成我们改写的js文件
// 一般不要格式化，有格式化检测
// 先进入页面，再打开F12，在hook掉setInterval的情况下，可以直接进行调试

// 格式化检测  hook toString
var func_toString = Function.prototype.toString;
Function.prototype.toString = function (){
    var s = func_toString.apply(this, arguments)
    console.log(s)
    debugger
    // 被debugger时，控制台输this，可以快速定位到被检测的方法位置
    return s
}
// 能不能hook 正则 返回true呢？

// 处理无限debugger
Function = function () {
    for (let i = 0; i < arguments.length ; i++) {
         arguments[i] = arguments[i].replace("debugger","")
    }
}

// 如果console.logs 失效了，提前备份，如v6
var log_ = console.log