// 定一个全局变量jw
var jw
// 找加载器
function r(i){
    // 出现类似 return e[i].call(t.exports, t, t.exports, r)报错，说明缺少i模块
    // 打印i，查看缺少的模块
    console.log(i)
}
// 把加载器赋值给全局变量
jw = r
// 通过加载器加载123模块
jw(123)
// 然后执行123模块的方法
var result = jw(123)()
console.log(result)



// 123模块的代码在webpackJsonp数组的第32个元素
(window.webpackJsonp = window.webpackJsonp || []).push([[32],{
    123: function (module, exports, __webpack_require__) {
        module.exports = function () {
            console.log("hello world")
        }
    }
}])
// 如果有第三个参数，直接扔掉



// 如果文件太大,可以require引入
require("../观鸟")