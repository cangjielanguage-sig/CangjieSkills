### init(UInt8, UInt8, UInt8, Float32)

```cangjie
public init(red: UInt8, green: UInt8, blue: UInt8, alpha!: Float32 = 1.0)
```

**功能：** 构造一个Color类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|red|UInt8|是|-|RGB中红色通道取值。|
|green|UInt8|是|-|RGB中绿色通道取值。|
|blue|UInt8|是|-|RGB中蓝色通道取值。|
|alpha|Float32|否|1.0| **命名参数。** 透明通道取值，取值范围 [0.0, 1.0]。|

### init(UInt32)

```cangjie
public init(value: UInt32)
```

**功能：** 构造一个Color类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|UInt32|是|-|Uint32颜色取值。alpha，R，G，B通道按顺序各占输入的8位，若只输入R,G,B三个通道，则alpha通道默认取0xff。|

### static func alphaAdapt(UInt32)

```cangjie
public static func alphaAdapt(origin: UInt32): UInt32
```

**功能：** 调整颜色的Alpha通道。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|origin|UInt32|是|-|UInt32颜色取值。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|调整Alpha通道后的UInt32颜色取值。|

### func toUInt32()

```cangjie
public func toUInt32(): UInt32
```

**功能：** 转为Uint32颜色取值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|Uint32颜色取值。|