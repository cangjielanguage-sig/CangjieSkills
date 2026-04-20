## 共享库依赖关系查询命令（dump-dependencies）

显示指定应用和指定模块依赖的共享库信息。

```bash
bm dump-dependencies [-h] [-n bundleName] [-m moduleName]
```

**共享库依赖关系查询命令参数列表：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h | 帮助信息。 |
| -n | 必选参数，查询指定共享库包名的详细信息。|
| -m | 可选参数，查询指定应用指定模块依赖的共享库信息。|

示例：

```Bash
# 显示指定应用指定模块依赖的共享库信息
bm dump-dependencies -n com.ohos.app -m entry
```

## 应用执行编译AOT命令（compile）

应用执行编译AOT命令。

```bash
bm compile [-h] [-m mode] [-r bundleName] [-a]
```

**compile命令参数列表：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h | 帮助信息。 |
| -a | 可选参数，编译所有应用。|
| -m | 可选参数，可选值为partial或者full。根据包名编译应用。|
| -r | 可选参数，移除应用的结果。|

示例：

```bash
# 根据包名编译应用
bm compile -m partial com.example.myapplication
```

## 拷贝ap文件命令（copy-ap）

拷贝ap文件到指定应用的/data/local/pgo路径。

```bash
bm copy-ap [-h] [-a] [-n bundleName]
```

**copy-ap命令参数列表：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h | 帮助信息。 |
| -a | 可选参数，默认所有包相关ap文件。拷贝所有包相关ap文件。|
| -n | 可选参数，默认当前应用包名。根据包名拷贝对应包相关的ap文件。|

示例：

```bash
# 根据包名移动对应包相关的ap文件
bm copy-ap -n com.example.myapplication
```

## 查询overlay应用信息命令（dump-overlay）

打印overlay应用的overlayModuleInfo。

```bash
bm dump-overlay [-h] [-b bundleName] [-m moduleName] [-t targetModuleName]
```

**dump-overlay命令参数列表：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h | 帮助信息。 |
| -b | 必选参数，获取指定应用的所有OverlayModuleInfo信息。|
| -m | 可选参数，默认当前应用主模块名。根据指定的包名和module名查询OverlayModuleInfo信息。|
| -t | 可选参数，根据指定的包名和目标module名查询OverlayModuleInfo信息。|

示例：

```bash
# 根据包名来获取overlay应用com.ohos.app中的所有OverlayModuleInfo信息
bm dump-overlay -b com.ohos.app

# 根据包名和module来获取overlay应用com.ohos.app中overlay module为entry的所有OverlayModuleInfo信息
bm dump-overlay -b com.ohos.app -m entry

# 根据包名和module来获取overlay应用com.ohos.app中目标module为feature的所有OverlayModuleInfo信息
bm dump-overlay -b com.ohos.app -m feature
```

## 查询应用的overlay相关信息命令（dump-target-overlay）

查询目标应用的所有关联overlay应用的overlayModuleInfo信息。

```bash
bm dump-target-overlay [-h] [-b bundleName] [-m moduleName]
```

**dump-target-overlay命令参数列表：**

| 参数 | 参数说明 |
| -------- | -------- |
| -h | 帮助信息。 |
| -b | 必选参数，获取指定应用的所有OverlayBundleInfo信息。|
| -m | 可选参数，默认当前应用主模块名。根据指定的包名和module名查询OverlayBundleInfo信息。|

示例：

```bash
# 根据包名来获取目标应用com.ohos.app中的所有关联的OverlayBundleInfo信息
bm dump-target-overlay-b com.ohos.app

# 根据包名和module来获取目标应用com.ohos.app中目标module为entry的所有关联的OverlayModuleInfo信息
bm dump-target-overlay -b com.ohos.app -m entry
```