### static func isCellularDataRoamingEnabled(Int32)

```cangjie
public static func isCellularDataRoamingEnabled(slotId: Int32): Bool
```

**功能：** 检查蜂窝数据业务是否启用漫游。调用该接口前，请先插入SIM卡。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>0：卡槽1。<br>1：卡槽2。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回检查蜂窝数据业务是否启用漫游。<br>true：蜂窝数据业务已启用漫游。<br>false：蜂窝数据业务已禁用漫游。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |8300001|Invalid parameter value.|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300999|Unknown error code.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

try {
    let result2 = TelephonyData.isCellularDataRoamingEnabled(0)
    AppLog.info("isCellularDataRoamingEnabled: ${result2}")
} catch (e: Exception) {
    AppLog.info("Exception: ${e.toString()}")
}
```