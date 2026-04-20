## class BorderRadiuses

```cangjie
public class BorderRadiuses {
    public var topLeft: ?Length
    public var topRight: ?Length
    public var bottomLeft: ?Length
    public var bottomRight: ?Length
    public init(topLeft!: ?Length = None, topRight!: ?Length = None, bottomLeft!: ?Length = None, bottomRight!: ?Length = None)
}
```

**功能：** 圆角类型，用于描述组件边框圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var topLeft

```cangjie
public var topLeft: ?Length
```

**功能：** 组件左上角圆角半径。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var topRight

```cangjie
public var topRight: ?Length
```

**功能：** 组件右上角圆角半径。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var bottomLeft

```cangjie
public var bottomLeft: ?Length
```

**功能：** 组件左下角圆角半径。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var bottomRight

```cangjie
public var bottomRight: ?Length
```

**功能：** 组件右下角圆角半径。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Length, ?Length, ?Length, ?Length)

```cangjie
public init(topLeft!: ?Length = None, topRight!: ?Length = None, bottomLeft!: ?Length = None, bottomRight!: ?Length = None)
```

**功能：** 初始化一个BorderRadiuses对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|topLeft|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 组件左上角圆角半径。初始值为0.vp。|
|topRight|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 组件右上角圆角半径。，初始值为0.vp。|
|bottomLeft|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 组件左下角圆角半径。初始值为0.v2。|
|bottomRight|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 组件右下角圆角半径。初始值为0.vp。|