### func openLogicalChannel(Array\<Int32>)

```cangjie
public func openLogicalChannel(aid: Array<Int32>): Channel
```

**功能：** 打开逻辑通道，参考[ISO 7816-4]协议，返回Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回None。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|aid|Array\<Int32>|是|在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。|

**返回值：**

|类型|说明|
|:----|:----|
|[Channel](#class-channel)|可用的逻辑Channel对象实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[SE错误码](../../errorcodes/cj-errorcode-secure_element.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|The parameter check failed. Possible causes: <br>1. Mandatory parameters are left unspecified.<br>2. Incorrect parameters types.<br>3. Parameter verification failed.|
  |801|Capability not supported.|
  |3300101|IllegalStateError, an attempt is made to use an SE session that has been closed.|
  |3300102|NoSuchElementError, the AID on the SE is not available or cannot be selected or a logical channel is already open to a non-multi-selectable applet.|
  |3300103|SecurityError, the calling application cannot be granted access to this AID or the default applet on this session.|
  |3300104|IOError, there is a communication problem to the reader or the SE.|

### func openLogicalChannel(Array\<Int32>, Int32)

```cangjie
public func openLogicalChannel(aid: Array<Int32>, p2: Int32): Channel
```

**功能：** 打开逻辑通道，参考[ISO 7816-4]协议，返回Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回None。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|aid|Array\<Int32>|是|在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。|
|p2|Int32|是|此Channel上执行SELECT APDU命令的P2参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[Channel](#class-channel)|可用的逻辑Channel对象实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[SE错误码](../../errorcodes/cj-errorcode-secure_element.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|The parameter check failed. Possible causes: <br>1. Mandatory parameters are left unspecified.<br>2. Incorrect parameters types.<br>3. Parameter verification failed.|
  |801|Capability not supported.|
  |3300101|IllegalStateError, an attempt is made to use an SE session that has been closed.|
  |3300102|NoSuchElementError, the AID on the SE is not available or cannot be selected or a logical channel is already open to a non-multi-selectable applet.|
  |3300103|SecurityError, the calling application cannot be granted access to this AID or the default applet on this session.|
  |3300104|IOError, there is a communication problem to the reader or the SE.|