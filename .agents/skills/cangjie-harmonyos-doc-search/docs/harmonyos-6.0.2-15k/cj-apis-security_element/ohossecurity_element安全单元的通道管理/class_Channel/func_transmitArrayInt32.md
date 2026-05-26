### func transmit(Array\<Int32>)

```cangjie
public func transmit(command: Array<Int32>): Array<Int32>
```

**功能：** 向SE发送APDU数据，数据符合ISO/IEC 7816规范。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|command|Array\<Int32>|是|需要发送到SE的APDU数据。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int32>|返回接收到的响应APDU数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[SE错误码](../../errorcodes/cj-errorcode-secure_element.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|The parameter check failed. Possible causes: <br>1. Mandatory parameters are left unspecified.<br>2. Incorrect parameters types.<br>3. Parameter verification failed.|
  |801|Capability not supported.|
  |3300101|IllegalStateError, an attempt is made to use an SE session or channel that has been closed.|
  |3300103|SecurityError, the command is filtered by the security policy.|
  |3300104|IOError, there is a communication problem to the reader or the SE.|