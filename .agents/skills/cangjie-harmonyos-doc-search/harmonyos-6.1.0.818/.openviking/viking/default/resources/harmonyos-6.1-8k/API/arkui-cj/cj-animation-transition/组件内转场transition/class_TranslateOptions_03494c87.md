## class TranslateOptions

```cangjie
public class TranslateOptions {
    public var x: ?Length
    public var y: ?Length
    public var z: ?Length
    public init(x!: ?Length = None, y!: ?Length = None, z!: ?Length = None)
}
```

**功能：** 定义平移选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var x

```cangjie
public var x: ?Length
```

**功能：** x轴上的平移距离。对于数字类型，单位为vp，取值范围为(-∞, +∞)。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var y

```cangjie
public var y: ?Length
```

**功能：** y轴上的平移距离。对于数字类型，单位为vp，取值范围为(-∞, +∞)。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var z

```cangjie
public var z: ?Length
```

**功能：** z轴上的平移距离。对于数字类型，单位为vp，取值范围为(-∞, +∞)。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Length, ?Length, ?Length)

```cangjie
public init(x!: ?Length = None, y!: ?Length = None, z!: ?Length = None)
```

**功能：** TranslateOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** x轴上的平移距离。<br>初始值：0.0.vp。|
|y|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** y轴上的平移距离。<br>初始值：0.0.vp。|
|z|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** z轴上的平移距离。<br>初始值：0.0.vp。|