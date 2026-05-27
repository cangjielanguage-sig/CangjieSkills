### hdc无法运行

**现象描述：**

使用命令行执行hdc.exe/hdc 二进制文件无法运行。

**可能原因&解决方法：**

- 运行环境异常

   Linux运行环境：建议使用Ubuntu18.04及以上64版本，如出现libc++.so引用错误，请使用ldd/readelf等命令检查库引用。

   macOS运行环境：建议使用macOS 11及以上版本。

   Windows运行环境：建议使用Windows10/Windows11 64位版本，如低版本缺失WinUSB库/驱动，请使用Zadig工具更新。对于符合设备，需要使用Zadig工具安装libusb-win32驱动。详情请见：[Zadig链接](https://github.com/pbatard/libwdi/releases)。

- 运行方式不当：请使用命令行依照正确命令运行hdc工具，而非鼠标双击文件。

### 其他问题排查常用步骤

1. 命令行执行`hdc list targets`查看返回值。
2. 查看`设备管理`是否有`HDC Device`。
3. 执行`hdc kill`关闭server后，执行`hdc -l5 start`收集日志（hdc.log位于执行端TEMP目录，不同平台目录位置存在差异，可参见[server端日志](#server端日志)）。
4. 通过hdc.log日志定位相关问题。