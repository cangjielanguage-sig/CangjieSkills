### 9568292 UserID为0的用户只能安装singleton应用

**错误信息：**

error: install failed due to zero user can only install singleton app.

**错误描述：**

UserID 0用户只允许安装singleton权限应用，singleton权限应用只允许被UserID 0用户安装。

**可能原因：**

singleton权限应用安装未指定UserID 0。

**处理步骤：**

应用是singleton权限，安装时指定UserID 0。

```bash
# 指定userId安装命令
hdc install -p hap名.hap -u 0
```

### 9568263 无法降级安装

**错误信息：**

error: install version downgrade.

**错误描述：**

正在安装应用的VersionCode小于系统中已安装应用的VersionCode，安装失败。

**可能原因：**

正在安装应用的VersionCode小于系统中已安装应用的VersionCode。

**处理步骤：**

卸载已安装的应用，重新安装新应用。

### 9568301 模块类型不一致

**错误信息：**

error: moduleName is inconsistent.

**错误描述：**

正在安装的模块名称在系统中已经存在，但模块名称不一致，导致安装失败。

**可能原因：**

待安装应用模块名称在系统中已存在，但模块类型不一致，导致安装失败。

**处理步骤：**

检查系统中已安装应用的模块名是否与待安装的模块名重复，若模块名称一致但类型不一致，修改对应模块module.json5中type属性。

### 9568303 企业设备管理禁止安装

**错误信息：**

error: Failed to install the HAP because the installation is forbidden by enterprise device management.

**错误描述：**

存在应用管控策略，安装失败。

**可能原因：**

存在应用管控策略。

**处理步骤：**

由于企业管控，暂无解决方案。请提[在线工单](https://developer.huawei.com/consumer/cn/support/feedback/#/)获取帮助。

### 9568304 应用不支持当前设备类型

**错误信息：**

error: device type is not supported.

**错误描述：**

正在安装的应用不支持当前设备类型，安装失败。

**可能原因：**

正在安装的应用不支持当前设备类型。

**处理步骤：**

如需要适配当前设备，请在应用设备类型配置中增加当前设备类型。应用deviceTypes配置包含phone（手机）、tablet（平板）、2in1（2合1设备）、tv（智慧屏）、wearable（智能手表）和car（车机）。

### 9568308 应用包类型不一致

**错误信息：**

error: install bundleType not same.

**错误描述：**

应用包类型不一致，导致安装失败。

**可能原因：**

安装多HAP应用时，存在两个模块的bundleType属性不一致。

**处理步骤：**

检查并确保多HAP应用中各模块app.json5的bundleType属性一致。

### 9568317 应用的多进程配置与系统配置不匹配

**错误信息：**

error: isolationMode does not match the system.

**错误描述：**

安装应用时，设置的isolationMode与系统配置项允许的系统配置不匹配。

**可能原因：**

- 场景一：设备支持隔离模式，即persist.bms.supportIsolationMode为true时，HAP配置的isolationMode为nonisolationOnly。
- 场景二：设备不支持隔离模式，即persist.bms.supportIsolationMode为false时，HAP配置的isolationMode为isolationOnly。

**处理步骤：**

按照设备的隔离模式配置HAP配置文件isolationMode属性。

```bash
# 查询设备persist.bms.supportIsolationMode值，若返回errNum is:106说明没配置
hdc shell
param get persist.bms.supportIsolationMode
# 配置设备persist.bms.supportIsolationMode值
hdc shell
param set persist.bms.supportIsolationMode [true|false]
```

### 9568315 数据代理的uri属性错误

**错误信息：**

error: uri in proxy data is wrong.

**错误描述：**

应用module.json文件中proxyData标签的uri属性验证失败。

**可能原因：**

uri不满足格式规范。

**处理步骤：**

确认uri满足格式规范。

```text
// uri格式规范
不同数据代理的uri不可重复，且需要满足datashareproxy://当前应用包名/xxx的格式
```