import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("尿大夫")  # 需要hook的app名称

scr = """
Java.perform(function(){
let SafeUtils = Java.use("com.uulife.medical.utils.SafeUtils");
SafeUtils["getSign"].implementation = function (j) {
    console.log(`SafeUtils.getSign is called: j=${j}`);
    let result = this["getSign"](j);
    console.log(`SafeUtils.getSign result=${result}`);
    return result;
}
});
"""

script = session.create_script(scr)


def on_message(message, data):
    print(11)


script.on("message", on_message)
script.load()
sys.stdin.read()
