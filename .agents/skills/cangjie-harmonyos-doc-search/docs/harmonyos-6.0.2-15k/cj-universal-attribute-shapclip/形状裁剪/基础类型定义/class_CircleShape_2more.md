### class CircleShape

```cangjie
public class CircleShape <: ShapeAbstract {
    public init()
    public init(width!: Length, height!: Length)
}
```

**功能：** 用于clip和mask接口的圆形形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

[ShapeAbstract](#class-shapeabstract)

#### init()

```cangjie
public init()
```

**功能：** 构造一个宽度0，高度0的圆形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(length, length)

```cangjie
public init(width!: Length, height!: Length)
```

**功能：** 构造一个宽度width，高度height的圆形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| width | [Length](./cj-common-types.md#interface-length)| 是 | - | **命名参数。**  宽度。<br>初始值：0.vp。 |
| height | [Length](./cj-common-types.md#interface-length) | 是 | - | **命名参数。**  高度。<br>初始值：0.vp。 |

### class EllipseShape

```cangjie
public class EllipseShape <: ShapeAbstract {
    public init()
    public init(width!: Length, height!: Length)
}
```

**功能：** 用于clip和mask接口的椭圆形形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

[ShapeAbstract](#class-shapeabstract)

#### init()

```cangjie
public init()
```

**功能：** 构造一个宽度0，高度0的椭圆形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(length, length)

```cangjie
public init(width!: Length, height!: Length)
```

**功能：** 构造一个宽度width，高度height的椭圆形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| width | [Length](./cj-common-types.md#interface-length)| 是 | - | **命名参数。**  宽度。<br>初始值：0.vp。 |
| height | [Length](./cj-common-types.md#interface-length) | 是 | - | **命名参数。**  高度。 <br>初始值：0.vp。|