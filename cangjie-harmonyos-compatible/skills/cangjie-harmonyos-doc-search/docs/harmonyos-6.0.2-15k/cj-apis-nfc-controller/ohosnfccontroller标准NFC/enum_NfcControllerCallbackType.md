## enum NfcControllerCallbackType

```cangjie
public enum NfcControllerCallbackType <: Equatable<NfcControllerCallbackType> & ToString {
    | NfcStateChange
    | ...
}
```

**功能：** 回调函数的事件类型。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**父类型：**

- Equatable\<NfcControllerCallbackType>
- ToString

### NfcStateChange

```cangjie
NfcStateChange
```

**功能：** NFC开关状态事件。

**起始版本：** 20

### func !=(NfcControllerCallbackType)

```cangjie
public operator func !=(other: NfcControllerCallbackType): Bool
```

**功能：** 对回调函数的事件类型进行判不等。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[NfcControllerCallbackType](#enum-nfccontrollercallbacktype)|是|回调函数的事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果回调函数的事件类型不同，返回true，否则返回false。|

### func ==(NfcControllerCallbackType)

```cangjie
public operator func ==(other: NfcControllerCallbackType): Bool
```

**功能：** 对回调函数的事件类型进行判等。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[NfcControllerCallbackType](#enum-nfccontrollercallbacktype)|是|回调函数的事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果回调函数的事件类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回回调函数的事件类型的字符串表示。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|回调函数的事件类型的字符串表示。|