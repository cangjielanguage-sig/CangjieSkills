## class CircleShape

```cangjie
public class CircleShape <: BaseShape {
    public init(width!: ?Length = None, height!: ?Length = None)
}
```

**功能：** 用于[clipShape](./cj-universal-attribute-shapclip.md#func-clipshapebaseshape)和[maskShape](./cj-universal-attribute-shapclip.md#func-maskshapebaseshape)接口的圆形形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [BaseShape](#class-baseshape)

### init(?Length, ?Length)

```cangjie
public init(width!: ?Length = None, height!: ?Length = None)
```

**功能：** CircleShape的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 圆形宽度。<br>初始值：0.vp。|
|height|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 圆形高度。<br>初始值：0.vp。|

## class EllipseShape

```cangjie
public class EllipseShape <: BaseShape {
    public init(width!: ?Length = None, height!: ?Length = None)
}
```

**功能：** 用于[clipShape](./cj-universal-attribute-shapclip.md#func-clipshapebaseshape)和[maskShape](./cj-universal-attribute-shapclip.md#func-maskshapebaseshape)接口的椭圆形状。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [BaseShape](#class-baseshape)

### init(?Length, ?Length)

```cangjie
public init(width!: ?Length = None, height!: ?Length = None)
```

**功能：** EllipseShape的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 椭圆形宽度。<br>初始值：0.vp。|
|height|?[Length](./cj-common-types.md#interface-length)|否|None| **命名参数。** 椭圆形高度。<br>初始值：0.vp。|