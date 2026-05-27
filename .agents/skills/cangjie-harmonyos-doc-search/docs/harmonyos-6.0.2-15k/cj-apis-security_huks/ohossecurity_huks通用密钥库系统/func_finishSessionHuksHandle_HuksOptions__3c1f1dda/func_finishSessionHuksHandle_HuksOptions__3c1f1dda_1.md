## func finishSession(HuksHandle, HuksOptions, Array\<UInt8>)

```cangjie
public func finishSession(handle: HuksHandle, options: HuksOptions, token: Array<UInt8>): Option<Array<UInt8>>
```

**功能：** finishSession操作密钥接口。[security_huks.initSession](#func-initsessionstring-huksoptions)、[security_huks.updateSession](#func-updatesessionhukshandle-huksoptions-arrayuint8)、[security_huks.finishSession](#func-finishsessionhukshandle-huksoptions-arrayuint8)为三段式接口，需要一起使用。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|handle|[HuksHandle](#class-hukshandle)|是|finishSession操作的handle。|
|options|[HuksOptions](#class-huksoptions)|是|finishSession的参数集合。|
|token|Array\<UInt8>|是|表示USER IAM服务的AuthToken的值。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<Array\<UInt8>>|输出处理结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[HUKS错误码](../../errorcodes/cj-errorcode-huks.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息      |
  | :-------- | :------------- |
  | 401 | Parameter error. |
  | 801 | Capability not supported.  |
  | 12000001 | algorithm mode is not supported. |
  | 12000002 | algorithm param is missing. |
  | 12000003 | algorithm param is invalid. |
  | 12000004 | operating file failed. |
  | 12000005 | IPC communication failed. |
  | 12000006 | error occurred in crypto engine. |
  | 12000007 | this credential is already invalidated permanently. |
  | 12000008 | verify authtoken failed. |
  | 12000009 | authtoken is already timeout. |
  | 12000011 | queried entity does not exist. |
  | 12000012 | external error. |
  | 12000014 | memory is insufficient. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.hilog.Hilog
import kit.UniversalKeystoreKit.*