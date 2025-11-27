(function() {
    var originalSend = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.send = function(body) {
        // 在发送请求前，我们可以获取到body（即请求体）
        debugger
        // 这里可以对body进行修改，如果需要修改的话
        // 然后调用原始的send方法
        return originalSend.apply(this, arguments);
    };
})();