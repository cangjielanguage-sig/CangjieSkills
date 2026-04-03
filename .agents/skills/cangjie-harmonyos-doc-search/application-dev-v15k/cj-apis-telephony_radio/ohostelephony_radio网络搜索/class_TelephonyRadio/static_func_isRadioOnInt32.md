### static func isRadioOn(Int32)

```cangjie
public static func isRadioOn(slotId!: Int32 = 0): Bool
```

**功能：** 判断Radio是否打开。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|否|0| **命名参数。** 卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2<br>如果不指定slotId，默认判断卡槽1打开。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回判断Radio是否打开的结果。<br>- true：Radio打开<br>- false：Radio关闭|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
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

let ret = TelephonyRadio.isRadioOn(slotId: 1)
AppLog.info("TelephonyRadio.isRadioOn suceess: data -> ${ret}")
```