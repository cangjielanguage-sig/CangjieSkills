### class ColorMetrics

```cangjie
public class ColorMetrics {
    public prop color: String
    public prop red: UInt8
    public prop green: UInt8
    public prop blue: UInt8
    public prop alpha: UInt8
}
```

**功能：** 用于混合颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### prop color

```cangjie
public prop color: String
```

**功能：** 获取ColorMetrics的颜色，返回的是rgba字符串的格式。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### prop red

```cangjie
public prop red: UInt8
```

**功能：** 获取ColorMetrics颜色的R分量（红色）。

**类型：** UInt8

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### prop green

```cangjie
public prop green: UInt8
```

**功能：** 获取ColorMetrics颜色的G分量（绿色）。

**类型：** UInt8

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### prop blue

```cangjie
public prop blue: UInt8
```

**功能：** 获取ColorMetrics颜色的B分量（蓝色）。

**类型：** UInt8

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### prop alpha

```cangjie
public prop alpha: UInt8
```

**功能：** 获取ColorMetrics颜色的A分量（透明度）。

**类型：** UInt8

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### static func numeric(UInt32)

```cangjie
public static func numeric(value: UInt32): ColorMetrics
```

**功能：** 使用HEX格式颜色实例化 ColorMetrics 类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :---- | :---- | :--- | :----- | :----------- |
| value | UInt32 | 是   | \-      | HEX格式颜色。 |

**返回值：**

|类型|说明|
| :-------   | :---------- |
| [ColorMetrics](./cj-universal-attribute-focus.md#class-colormetrics) | ColorMetrics 类的实例。|

#### static func rgba(UInt8, UInt8, UInt8, Float32)

```cangjie
public static func rgba(red: UInt8, green: UInt8, blue: UInt8, alpha!: Float32 = MAX_ALPHA_VALUE): ColorMetrics
```

**功能：** 使用rgb或者rgba格式颜色实例化 ColorMetrics 类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :---- | :---- | :--- | :----- | :----------- |
| red | UInt8 | 是 | \- | R分量（红色）。 |
| green | UInt8 | 是 | \- | G分量（绿色）。 |
| blue | UInt8 | 是 | \- | B分量（蓝色）。 |
| alpha | Float32 | 否  | MAX_ALPHA_VALUE | **命名参数。**  A分量（透明度）。 |

**返回值：**

|类型|说明|
| :-------   | :---------- |
| [ColorMetrics](./cj-universal-attribute-focus.md#class-colormetrics) | ColorMetrics 类的实例。|

#### static func resourceColor(Color)

```cangjie
public static func resourceColor(color: Color): ColorMetrics
```

**功能：** 使用颜色枚举值实例化 ColorMetrics 类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :---- | :---- | :--- | :----- | :----------- |
| color | Color | 是   | \- | 颜色类型。 |

**返回值：**

|类型|说明|
| :-------   | :---------- |
| [ColorMetrics](./cj-universal-attribute-focus.md#class-colormetrics) | ColorMetrics 类的实例。|

#### static func resourceColor(UInt32)

```cangjie
public static func resourceColor(color: UInt32): ColorMetrics
```

**功能：** 使用HEX格式颜色实例化 ColorMetrics 类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :---- | :---- | :--- | :----- | :----------- |
| color | UInt32 | 是   | \-  | HEX格式颜色。 |

**返回值：**

|类型|说明|
| :-------   | :---------- |
| [ColorMetrics](./cj-universal-attribute-focus.md#class-colormetrics) | ColorMetrics 类的实例。|