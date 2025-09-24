import frida, time

device = frida.get_usb_device()
try:
    # 使用确认过的包名
    pid = device.spawn("com.che168.autotradercloud")
    time.sleep(3)  # 关键：等待进程初始化
    session = device.attach(pid)
    device.resume(pid)
    print("成功附加到进程！")
except Exception as e:
    print(f"失败: {e}")
