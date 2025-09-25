Java.perform(function () {
    let SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil");
    SecurityUtil["encodeMD5"].implementation = function (str) {
        console.log(`SecurityUtil.encodeMD5 is called: str =${str}`);
        let result = this["encodeMD5"](str);
        console.log(`SecurityUtil.encodeMD5 result =${result}`);
        return '123';
    }
});

// attach 方案 frida -UF -l hook.js
// spawn 方案 frida -U -f com.che168.autotradercloud -l hook.js