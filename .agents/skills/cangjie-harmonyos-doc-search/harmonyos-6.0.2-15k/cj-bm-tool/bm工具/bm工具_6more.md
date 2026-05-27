# bm工具

Bundle Manager（包管理工具，简称bm）是实现应用安装、卸载、更新、查询等功能的工具，bm为开发者提供基本的应用安装包的调试能力。

> **说明：**
>
> 当前仓颉仅支持开发HAR和HAP包，不支持HSP包，因此本工具中关于HSP包相关的功能，在仓颉程序中不可用。

## 环境要求（hdc工具）

在使用本工具前，开发者需要先获取[hdc工具](./cj-hdc.md)，执行hdc shell。

## bm工具命令列表

| 命令 | 描述 |
| -------- | -------- |
| help | 帮助命令，用于查询bm支持的命令信息。 |
| install | 安装命令，用于安装应用。 |
| uninstall | 卸载命令，用于卸载应用。 |
| dump | 查询命令，用于查询应用的相关信息。 |
| clean | 清理命令，用于清理应用的缓存和数据。此命令在root版本下可用，在user版本下打开开发者模式可用。其它情况不可用。|
| get | 获取udid命令，用于获取设备的udid。 |
| quickfix | 快速修复相关命令，用于执行补丁相关操作，如补丁安装、补丁查询。 |
| compile | 应用执行编译AOT命令。 |
| copy-ap | 把应用的ap文件拷贝到/data/local/pgo目录下，供shell用户读取文件。 |
| dump-dependencies | 查询应用依赖的模块信息。 |
| dump-shared | 查询应用间HSP应用信息。 |
| dump-overlay | 打印overlay应用的overlayModuleInfo。 |
| dump-target-overlay | 打印目标应用的所有关联overlay应用的overlayModuleInfo。 |

## 帮助命令（help）

```bash
# 显示帮助信息
bm help
```

## 安装命令（install）

```bash
bm install [-h] [-p filePath] [-r] [-w waitingTime] [-s hspDirPath]
```

**安装命令参数列表：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h | 帮助信息。 |
| -p | 必选参数，指定路径和多个HAP同时安装。 |
| -r | 可选参数，覆盖安装一个HAP。默认值为覆盖安装。 |
| -s | 根据场景判断，安装应用间HSP时为必选参数，其他场景为可选参数。安装应用间共享库， 每个路径目录下只能存在一个同包名的HSP。 |
| -w | 可选参数，安装HAP时指定bm工具等待时间，最小的等待时长为5s，最大的等待时长为600s,&nbsp;默认缺省为5s。 |

示例：

```bash
# 安装一个hap
bm install -p /data/app/ohos.app.hap
# 覆盖安装一个hap
bm install -p /data/app/ohos.app.hap -r
# 安装一个应用间共享库
bm install -s xxx.hsp
# 同时安装使用方应用和其依赖的应用间共享库
bm install -p aaa.hap -s xxx.hsp yyy.hsp
# 安装一个hap,等待时间为10s
bm install -p /data/app/ohos.app.hap -w 10
```

## 卸载命令（uninstall）

```bash
bm uninstall [-h] [-n bundleName] [-m moduleName] [-k] [-s] [-v versionCode]
```

**卸载命令参数列表：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h | 帮助信息。 |
| -n | 必选参数，指定Bundle名称卸载应用。|
| -m | 可选参数，指定卸载应用的一个模块。默认卸载所有模块。 |
| -k | 可选参数，卸载应用时保存应用数据。默认卸载应用时不保存应用数据。 |
| -s | 根据场景判断，安装应用间HSP时必选参数，其他场景为可选参数。卸载指定的共享库。|
| -v | 可选参数，指定共享包的版本号。默认卸载同包名的所有共享包。 |

示例：

```bash
# 卸载一个应用
bm uninstall -n com.ohos.app
# 卸载应用的一个模块
bm uninstall -n com.ohos.app -m com.ohos.app.EntryAbility
# 卸载一个shared bundle
bm uninstall -n com.ohos.example -s
# 卸载一个shared bundle的指定版本
bm uninstall -n com.ohos.example -s -v 100001
# 卸载一个应用，并保留用户数据
bm uninstall -n com.ohos.app -k
```