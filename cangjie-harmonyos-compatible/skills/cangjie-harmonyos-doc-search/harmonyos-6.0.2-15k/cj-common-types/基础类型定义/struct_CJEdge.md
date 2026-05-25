## struct CJEdge

```cangjie
public struct CJEdge {
    public init(topLength: Length, rightLength: Length, bottomLength: Length, leftLength: Length)
}
```

**功能：** 边框长度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Length, Length, Length, Length)

```cangjie
public init(topLength: Length, rightLength: Length, bottomLength: Length, leftLength: Length)
```

**功能：** 构造边框长度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|topLength|[Length](#interface-length)|是|-|上侧边框长度。|
|rightLength|[Length](#interface-length)|是|-|右侧边框长度。|
|bottomLength|[Length](#interface-length)|是|-|底部边框长度。|
|leftLength|[Length](#interface-length)|是|-|左侧边框长度。|