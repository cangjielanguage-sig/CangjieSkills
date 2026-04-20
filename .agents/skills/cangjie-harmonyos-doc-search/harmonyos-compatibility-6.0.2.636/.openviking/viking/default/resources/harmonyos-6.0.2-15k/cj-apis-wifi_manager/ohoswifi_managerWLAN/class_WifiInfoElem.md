## class WifiInfoElem

```cangjie
public class WifiInfoElem <: ToString {
    public let eid: UInt32
    public let content: Array<UInt8>
}
```

**功能：** WLAN热点信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- ToString

### let content

```cangjie
public let content: Array<UInt8>
```

**功能：** 元素内容。

**类型：** Array\<UInt8>

**读写能力：** 只读

**起始版本：** 19

### let eid

```cangjie
public let eid: UInt32
```

**功能：** 元素ID。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前类的字符串表示。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前类的字符串表示。|