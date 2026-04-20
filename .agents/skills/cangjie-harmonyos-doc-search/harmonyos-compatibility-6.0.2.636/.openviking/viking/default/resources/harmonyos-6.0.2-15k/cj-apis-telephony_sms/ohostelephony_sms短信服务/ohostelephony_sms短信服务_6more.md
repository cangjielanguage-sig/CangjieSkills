# ohos.telephony_sms（短信服务）

短信服务提供了管理短信的一些基础能力，包括创建、发送短信，获取发送短信的默认SIM卡槽ID，以及检查当前设备是否具备短信发送和接收能力等。

## 导入模块

```cangjie
import kit.TelephonyKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func createMessage(Array\<Int32>, String)

```cangjie
public func createMessage(pdu: Array<Int32>, specification: String): ShortMessage
```

**功能：** 根据协议数据单元（PDU）和指定的短信协议创建短信实例。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pdu|Array\<Int32>|是|-|协议数据单元，从收到的信息中获取。|
|specification|String|是|-|短信协议类型。<br/>- 3gpp：表示GSM/UMTS/LTE SMS。<br/>- 3gpp2：表示CDMA SMS。|

**返回值：**

|类型|说明|
|:----|:----|
|[ShortMessage](#class-shortmessage)|短信实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
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

let pdu: Array<Int32> = [0x01, 0x00, 0x05, 0x81, 0x01, 0x80, 0xF6, 0x00, 0x00, 0x05, 0xE8, 0x32, 0x9B, 0xFD, 0x06]
let message = createMessage(pdu, "3gpp")
```

## func getDefaultSmsSimId()

```cangjie
public func getDefaultSmsSimId(): Int32
```

**功能：** 获取发送短信的默认SIM卡ID。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|发送短信的默认SIM卡ID：<br/>与SIM卡绑定，从1开始递增。<br/>无卡时返回值为-1。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |8300001|Invalid parameter value.|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300004|Do not have sim card.|
  |8300999|Unknown error code.|
  |8301001|SIM card is not activated.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

getDefaultSmsSimId()
```

## func getDefaultSmsSlotId()

```cangjie
public func getDefaultSmsSlotId(): Int32
```

**功能：** 获取发送短信的默认SIM卡槽ID。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|发送短信的默认SIM卡：<br/>- 0：卡槽1。<br/>- 1：卡槽2。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

getDefaultSmsSlotId()
```