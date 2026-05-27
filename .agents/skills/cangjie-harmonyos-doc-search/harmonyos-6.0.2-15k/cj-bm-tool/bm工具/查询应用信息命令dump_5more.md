## 查询应用信息命令（dump）

```bash
bm dump [-h] [-a] [-n bundleName] [-s shortcutInfo] [-d deviceId]
```

**查询命令参数列表：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h | 帮助信息。 |
| -a | 可选参数，查询系统已经安装的所有应用。 |
| -n | 可选参数，查询指定Bundle名称的详细信息。 |
| -s | 可选参数，查询指定Bundle名称下的快捷方式信息。 |
| -d | 可选参数，查询指定设备中的包信息。默认查询当前设备。 |

示例：

```bash
# 显示所有已安装的Bundle名称
bm dump -a
# 查询该应用的详细信息
bm dump -n com.ohos.app
# 查询该应用的快捷方式信息
bm dump -s -n com.ohos.app
# 查询跨设备应用信息
bm dump -n com.ohos.app -d xxxxx
```

## 清理命令（clean）

```bash
bm clean [-h] [-c] [-n bundleName] [-d] [-i appIndex]
```

**清理命令参数列表：**

| 参数 | 参数说明 |
| -------- | --------- |
| -h | 帮助信息。 |
| -c&nbsp;-n | -n为必选参数，-c为可选参数。清除指定Bundle名称的缓存数据。 |
| -d&nbsp;-n | -n为必选参数，-d为可选参数。清除指定Bundle名称的数据目录。 |
| -i | 可选参数，清除分身应用的数据目录。默认为0。|

示例：

```bash
# 清理该应用下的缓存数据
bm clean -c -n com.ohos.app
# 清理该应用下的用户数据
bm clean -d -n com.ohos.app
# 执行结果
clean bundle data files successfully.
```

## 获取udid命令（get）

```bash
bm get [-h] [-u]
```

**获取udid命令参数列表：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h |帮助信息。 |
| -u | 必选参数，获取设备的udid。|

示例：

```bash
# 获取设备的udid
bm get -u
# 执行结果
udid of current device is :
23CADE0C
```

## 快速修复命令（quickfix）

```bash
bm quickfix [-h] [-a -f filePath [-t targetPath] [-d]] [-q -b bundleName] [-r -b bundleName]
```

> **注意：**
>
> hqf文件制作方式可参考[HQF打包指令](./cj-packing-tool.md#hqf打包指令)。

**快速修复命令参数列表：**

|   参数  | 参数说明 |
| -------- | -------- |
| -h | 帮助信息。 |
| -a&nbsp;-f | -a为可选参数，指定-a后，-f为必选参数。执行快速修复补丁安装命令，file-path对应hqf文件，支持传递1个或多个hqf文件，或传递hqf文件所在的目录。 |
| -q&nbsp;-b | -q为可选参数，指定-q后，-b为必选参数，未指定-q。根据包名查询补丁信息。 |
| -r&nbsp;-b | -r为可选参数，指定-r后，-b为必选参数。根据包名卸载未使能的补丁。|
| -t | 可选参数，快速修复应用到指定目标路径。|
| -d | 可选参数，应用快速修复调试模式。|

**示例1：**

```bash
# 根据包名查询补丁包信息
bm quickfix -q -b com.ohos.app
```

**执行结果：**

```text
Information as follows:
ApplicationQuickFixInfo:
bundle name: com.ohos.app
bundle version code: xxx
bundle version name: xxx
patch version code: x
patch version name:
cpu abi:
native library path:
type:
```

**示例2：**

```bash
# 快速修复补丁安装
bm quickfix -a -f /data/app/
```

**执行结果：**

```text
apply quickfix succeed.
```

**示例3：**

```bash
# 快速修复补丁卸载
bm quickfix -r -b com.ohos.app
```

**执行结果：**

```text
delete quick fix successfully
```

## 共享库查询命令（dump-shared）

```bash
bm dump-shared [-h] [-a] [-n bundleName] [-m moduleName]
```

**共享库查询命令参数列表：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h | 帮助信息。 |
| -a | 可选参数，查询系统中已安装所有共享库。|
| -n | 可选参数，查询指定共享库包名的详细信息。|
| -m | 可选参数，查询指定共享库包名和模块名的详细信息。|

示例：

```bash
# 显示所有已安装共享库包名
bm dump-shared -a
# 显示该共享库的详细信息
bm dump-shared -n com.ohos.lib
# 显示指定应用指定模块依赖的共享库信息
bm dump-dependencies -n com.ohos.app -m entry
```