## enum CardType

```cangjie
public enum CardType <: Equatable<CardType> & ToString {
    | PAYMENT
    | OTHER
    | ...
}
```

**功能：** 定义卡模拟应用所使用的业务类型。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**父类型：**

- Equatable\<CardType>
- ToString

### OTHER

```cangjie
OTHER
```

**功能：** 其他类型。

**起始版本：** 19

### PAYMENT

```cangjie
PAYMENT
```

**功能：** 支付类型。

**起始版本：** 19

### func !=(CardType)

```cangjie
public operator func !=(other: CardType): Bool
```

**功能：** 对卡模拟应用所使用的业务类型进行判不等。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CardType](#enum-cardtype)|是|卡模拟应用所使用的业务类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果卡模拟应用所使用的业务类型不同，返回true，否则返回false。|

### func ==(CardType)

```cangjie
public operator func ==(other: CardType): Bool
```

**功能：** 对卡模拟应用所使用的业务类型进行判等。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[CardType](#enum-cardtype)|是|卡模拟应用所使用的业务类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果卡模拟应用所使用的业务类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回卡模拟应用所使用的业务类型的字符串表示。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|卡模拟应用所使用的业务类型的字符串表示。|

## enum NfcEventType

```cangjie
public enum NfcEventType <: Equatable<NfcEventType> & ToString {
    | HceCmd
    | ...
}
```

**功能：** 回调函数的事件类型。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**父类型：**

- Equatable\<NfcEventType>
- ToString

### HceCmd

```cangjie
HceCmd
```

**功能：** 接收到hce指令事件。

**起始版本：** 19

### func !=(NfcEventType)

```cangjie
public operator func !=(other: NfcEventType): Bool
```

**功能：** 对回调函数的事件类型进行判不等。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[NfcEventType](#enum-nfceventtype)|是|回调函数的事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果回调函数的事件类型不同，返回true，否则返回false。|

### func ==(NfcEventType)

```cangjie
public operator func ==(other: NfcEventType): Bool
```

**功能：** 对回调函数的事件类型进行判等。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[NfcEventType](#enum-nfceventtype)|是|回调函数的事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果回调函数的事件类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回回调函数事件类型的字符串表示。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|回调函数事件类型的字符串表示。|