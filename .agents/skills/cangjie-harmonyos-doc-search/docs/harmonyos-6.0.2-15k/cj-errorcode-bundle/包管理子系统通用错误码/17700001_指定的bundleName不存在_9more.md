## 17700001 指定的bundleName不存在

**错误信息**

The specified bundle name is not found.

**错误描述**

调用查询等接口时，传入的bundleName不存在。

**可能原因**

1. 输入的bundleName有误。
2. 系统中对应的应用没有安装。

**处理步骤**

1. 检查bundleName拼写是否正确。
2. 确认对应的应用是否安装。

## 17700002 指定的moduleName不存在

**错误信息**

The specified module is not found.

**错误描述**

调用查询或者免安装相关接口时，传入的moduleName不存在。

**可能原因**

1. 输入的moduleName有误。
2. 系统中对应的应用没有安装该模块。

**处理步骤**

1. 检查moduleName拼写是否正确。
2. 确认对应的应用是否安装该模块。

## 17700003 指定的abilityName不存在

**错误信息**

The specified ability is not found.

**错误描述**

调用查询等接口时，传入的abilityName不存在。

**可能原因**

1. 输入的abilityName有误。
2. 系统中对应的应用不存在该abilityName对应的ability。

**处理步骤**

1. 检查abilityName拼写是否正确。
2. 确认对应的应用是否存在该abilityName对应的ability。

## 17700004 指定的用户不存在

**错误信息**

The specified user ID is not found.

**错误描述**

调用与用户相关接口时，传入的用户不存在。

**可能原因**

1. 输入的用户名有误。
2. 系统中没有该用户。

**处理步骤**

1. 检查用户名拼写是否正确。
2. 确认系统中存在该用户。

## 17700005 指定的appId为空字符串

**错误信息**

The specified app ID is empty string.

**错误描述**

调用appControl模块中的相关接口时，传入的appId为空字符串。

**可能原因**

传入的appId为空字符串。

**处理步骤**

检查appId是否为空字符串。

## 17700006 查询的权限不存在

**错误信息**

The specified permission is not found.

**错误描述**

调用bundleManager模块中的getPermissionDef接口时，传入的权限不存在。

**可能原因**

1. 传入的permission名称拼写有误。
2. 系统中不存在对应的权限。

**处理步骤**

1. 检查permission拼写是否正确。
2. 确认系统中是否有该权限。

## 17700007 输入的设备Id有误

**错误信息**

The specified device ID is not found.

**错误描述**

调用distributedBundle模块相关接口时，传入的设备id有误。

**可能原因**

1. 传入的deviceId拼写有误。
2. deviceId不存在。

**处理步骤**

1. 检查deviceId拼写是否正确。
2. 确认deviceId是否存在。

## 17700010 文件解析失败导致应用安装失败

**错误信息**

Failed to install the HAP because the HAP fails to be parsed.

**错误描述**

调用installer模块中的install接口时，传入的HAP解析失败。

**可能原因**

1. HAP的格式不是zip格式。
2. HAP的配置文件不满足json格式。
3. HAP的配置文件缺少必要的字段。

**处理步骤**

1. 确认hap的格式是zip。
2. 确认hap的配置文件满足配置文件json格式。
3. 检查DevEco Studio编译hap时是否有错误提示，缺省字段时会有相应的报错。

## 17700011 签名校验失败导致应用安装失败

**错误信息**

Failed to install the HAP because the HAP signature fails to be verified.

**错误描述**

调用installer模块中的install接口时，签名校验失败导致应用安装失败。

**可能原因**

1. HAP没有签名。
2. hap签名信息来源不可靠。
3. 升级的HAP与已安装的HAP签名信息不一致。
4. 多个hap的签名信息不一致。

**处理步骤**

1. 确认hap包是否签名成功。
2. 确认hap包的签名证书是从应用市场申请。
3. 确认多个hap包签名时使用的证书相同。
4. 确认升级的ha包p签名证书与已安装的hap包相同。