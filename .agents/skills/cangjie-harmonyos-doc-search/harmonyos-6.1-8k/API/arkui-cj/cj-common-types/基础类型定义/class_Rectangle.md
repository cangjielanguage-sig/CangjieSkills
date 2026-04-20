## class Rectangle

```cangjie
public class Rectangle {
    public var x: ?Length
    public var y: ?Length
    public var width: ?Length
    public var height: ?Length
    public init(x!: ?Length = None, y!: ?Length = None, width!: ?Length = None, height!: ?Length = None)
}
```

**功能：** 定义区域位置类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var x

```cangjie
public var x: ?Length
```

**功能：** 触摸点相对于组件左上角的x轴坐标。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var y

```cangjie
public var y: ?Length
```

**功能：** 触摸点相对于组件左上角的y轴坐标。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var width

```cangjie
public var width: ?Length
```

**功能：** 触摸热区的宽度。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var height

```cangjie
public var height: ?Length
```

**功能：** 触摸热区的高度。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Length, ?Length, ?Length, ?Length)

```cangjie
public init(x!: ?Length = None, y!: ?Length = None, width!: ?Length = None, height!: ?Length = None)
```

**功能：** 构造一个Rectangle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 触摸点相对于组件左上角的x轴坐标。初始值为0.vp。|
|y|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 触摸点相对于组件左上角的y轴坐标。初始值为0.vp。|
|width|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 触摸热区的宽度。初始值为100.percent。|
|height|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 触摸热区的高度。初始值为100.percent。|