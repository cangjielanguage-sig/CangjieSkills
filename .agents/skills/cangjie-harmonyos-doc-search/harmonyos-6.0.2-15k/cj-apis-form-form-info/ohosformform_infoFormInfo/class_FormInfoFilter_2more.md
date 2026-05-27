## class FormInfoFilter

```cangjie
public class FormInfoFilter {
    public init(moduleName: String)
}
```

**功能：** 卡片信息过滤器，仅将符合过滤器内要求的卡片信息返回。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

### prop moduleName

```cangjie
public prop moduleName: String
```

**功能：** 仅保留含moduleName与提供值相符的卡片信息，为空时则不通过moduleName进行过滤。

**类型：** String

**读写能力：** 只读

**起始版本：** 20

### init(String)

```cangjie
public init(moduleName: String)
```

**功能：** FormInfoFilter的构造器。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|moduleName|String|是|-|仅保留含moduleName与提供值相符的卡片信息，为空时则不通过moduleName进行过滤。|

## enum ColorMode

```cangjie
public enum ColorMode <: Equatable<ColorMode> & ToString {
    | ModeAuto
    | ModeDark
    | ModeLight
    | ...
}
```

**功能：** 卡片支持的颜色模式枚举。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**父类型：**

- Equatable\<ColorMode>
- ToString

### ModeAuto

```cangjie
ModeAuto
```

**功能：** 表示自动模式。跟随系统。

**起始版本：** 20

### ModeDark

```cangjie
ModeDark
```

**功能：** 表示暗色。

**起始版本：** 20

### ModeLight

```cangjie
ModeLight
```

**功能：** 表示亮色。

**起始版本：** 20

### func !=(ColorMode)

```cangjie
public operator func !=(other: ColorMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ColorMode](#enum-colormode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ColorMode)

```cangjie
public operator func ==(other: ColorMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ColorMode](#enum-colormode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|