function get_sign(){

}
var CryptoJS = require('crypto-js')
var r = CryptoJS

function s(e) {
    e = decodeURIComponent(e);
    for (var t = String.fromCharCode(e.charCodeAt(0) - e.length), n = 1; n < e.length; n++)
        t += String.fromCharCode(e.charCodeAt(n) - t.charCodeAt(n - 1));
    return t
}
function get_sign(e) {
    e = CryptoJS.MD5("6key_web_new_fanyi".concat('6dVjYLFyzfkFkk').concat(e.replace(/(^\s*)|(\s*$)/g, ""))).toString().substring(0, 16);
    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "%5C%C2%80%C2%9A%C2%A8%C2%B6%C2%B8y%C2%9B%C2%B2%C2%8F%7C%7F%C2%97%C3%88%C2%A9d"
      , n = r.enc.Utf8.parse(s(t))
      , o = r.AES.encrypt(e, n, {
        mode: r.mode.ECB,
        padding: r.pad.Pkcs7
    });
    return encodeURIComponent(o.toString())
}
function decrypt_data(e) {
    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "aahc3TfyfCEmER33";
    if (!e)
        return null;
    var n = r.enc.Utf8.parse(t)
      , o = r.AES.decrypt(e, n, {
        mode: r.mode.ECB,
        padding: r.pad.Pkcs7
    });
    return decodeUnicode(o.toString(r.enc.Utf8))
}

function decodeUnicode(str) {
    return str.replace(/\\u[\dA-Fa-f]{4}/g, function(match) {
        return String.fromCharCode(parseInt(match.replace(/\\u/g, ''), 16));
    });
}