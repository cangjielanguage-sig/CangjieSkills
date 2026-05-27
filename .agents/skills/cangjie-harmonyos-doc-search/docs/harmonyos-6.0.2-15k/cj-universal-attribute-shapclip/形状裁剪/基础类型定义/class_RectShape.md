### class RectShape

```cangjie
public class RectShape <: ShapeAbstract {
    public init()
    public init(width!: Length, height!: Length)
}
```

**功能：** 用于clip和mask接口的矩形形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

[ShapeAbstract](#class-shapeabstract)

#### init()

```cangjie
public init()
```

**功能：** 构造一个宽度0，高度0的矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Length, Length)

```cangjie
public init(width!: Length, height!: Length)
```

**功能：** 构造一个宽度width，高度height的矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| width | [Length](./cj-common-types.md#interface-length)| 是 | - | **命名参数。**  宽度。<br>初始值：0.vp。 |
| height | [Length](./cj-common-types.md#interface-length) | 是 | - | **命名参数。**  高度。 <br>初始值：0.vp。|

#### func radiusWidth(Length)

```cangjie
public func radiusWidth(value: Length): This
```

**功能：** 设置圆角的宽度，仅设置宽时宽高一致。异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|圆角的宽度。</br>初始值：0.vp。|

#### func radiusHeight(Length)

```cangjie
public func radiusHeight(value: Length): This
```

**功能：** 设置圆角的高度，仅设置高时宽高一致。异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|圆角的高度。</br>初始值：0.vp。|

#### func radius(Length)

```cangjie
public func radius(value: Length): This
```

**功能：** 设置圆角半径大小。异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|圆角的半径大小。</br>初始值：0.vp。|