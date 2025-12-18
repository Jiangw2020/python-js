// var t =[o, undefined]; // 请求
// n = Promise.resolve(e);
// this.interceptors.request.forEach((function(e) {
//     t.unshift(e.fulfilled, e.rejected)
// }
// )),
//
// // t = [哈哈, 呵呵, o, undefined] // 怼完请求拦截器
// this.interceptors.response.forEach((function(e) {
//     t.push(e.fulfilled, e.rejected)
// }
// ));
// // // t = [哈哈, 呵呵, o, undefined, 哈尔滨, 牡丹江]  # 怼完响应拦截器
//
// for (; t.length; ) //程序执行到这里时候,  t里面装的,就是axios完整的流程
//     n = n.then(t.shift(), t.shift());
// // 第一次循环
//  n = n.then(哈哈, 呵呵); // 请求发送之前
//  // 第二次循环
//  n = n.then(o, undefined); // 发请求
//   // 第三次循环
//  n = n.then(哈尔滨, 牡丹江); // 响应回来之后, 干什么
//
// // 使用拦截器 -> 请求
// axios.interceptors.request.use(function(){哈哈}, function(){呵呵})
// // 响应
// axios.interceptors.response.use(function(){哈尔滨}, function(){牡丹江})
//
// // t里面装的是完整的流程
//
// [请求拦截器,  o, undefined,  响应拦截器]