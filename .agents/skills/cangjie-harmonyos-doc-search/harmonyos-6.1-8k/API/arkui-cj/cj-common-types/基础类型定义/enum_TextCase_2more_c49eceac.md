## enum TextCase

```cangjie
public enum TextCase <: Equatable<TextCase> {
    | Normal
    | LowerCase
    | UpperCase
    | ...
}
```

**功能：** 文本大小写格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[TextCase](#enum-textcase)>

### Normal

```cangjie
Normal
```

**功能：** 保持文本原有大小写。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### LowerCase

```cangjie
LowerCase
```

**功能：** 文本采用全小写。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### UpperCase

```cangjie
UpperCase
```

**功能：** 文本采用全大写。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(TextCase)

```cangjie
public operator func ==(other: TextCase): Bool
```

**功能：** 判断两个TextCase枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextCase](#enum-textcase)|是|-|要比较的另一个TextCase枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(TextCase)

```cangjie
public operator func !=(other: TextCase): Bool
```

**功能：** 判断两个TextCase枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextCase](#enum-textcase)|是|-|要比较的另一个TextCase枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum BorderStyle

```cangjie
public enum BorderStyle <: Equatable<BorderStyle> {
    | Solid
    | Dashed
    | Dotted
    | ...
}
```

**功能：** 边框样式，用于描述组件边框四条边的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[BorderStyle](#enum-borderstyle)>

### Solid

```cangjie
Solid
```

**功能：** 显示为一条实线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Dashed

```cangjie
Dashed
```

**功能：** 显示为一系列短的方形虚线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Dotted

```cangjie
Dotted
```

**功能：** 显示为一系列圆点，圆点半径为borderWidth的一半。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(BorderStyle)

```cangjie
public operator func ==(other: BorderStyle): Bool
```

**功能：** 判断两个BorderStyle枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BorderStyle](#enum-borderstyle)|是|-|要比较的另一个BorderStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(BorderStyle)

```cangjie
public operator func !=(other: BorderStyle): Bool
```

**功能：** 判断两个BorderStyle枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BorderStyle](#enum-borderstyle)|是|-|要比较的另一个BorderStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|