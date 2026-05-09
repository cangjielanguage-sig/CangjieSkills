## enum TextContentStyle

```cangjie
public enum TextContentStyle <: Equatable<TextContentStyle> {
    | Default
    | Inline
    | ...
}
```

**功能：** 文本框多态样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[TextContentStyle](#enum-textcontentstyle)>

### Default

```cangjie
Default
```

**功能：** 默认风格，光标宽1.5vp，光标高度与文本选中底板高度和字体大小相关。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Inline

```cangjie
Inline
```

**功能：** 内联输入风格。文本选中底板高度与输入框高度相同。
内联输入是在有明显的编辑态/非编辑态的区分场景下使用，例如：文件列表视图中的重命名。
不支持showError属性。
内联模式下，不支持拖入文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(TextContentStyle)

```cangjie
public operator func ==(other: TextContentStyle): Bool
```

**功能：** 判断两个TextContentStyle枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextContentStyle](#enum-textcontentstyle)|是|-|要比较的另一个TextContentStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(TextContentStyle)

```cangjie
public operator func !=(other: TextContentStyle): Bool
```

**功能：** 判断两个TextContentStyle枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextContentStyle](#enum-textcontentstyle)|是|-|要比较的另一个TextContentStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum CheckBoxShape

```cangjie
public enum CheckBoxShape <: Equatable<CheckBoxShape> {
    | Circle
    | RoundedSquare
    | ...
}
```

**功能：** 多选框形状类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[CheckBoxShape](#enum-checkboxshape)>

### Circle

```cangjie
Circle
```

**功能：** 圆形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### RoundedSquare

```cangjie
RoundedSquare
```

**功能：** 圆角正方形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(CheckBoxShape)

```cangjie
public operator func ==(other: CheckBoxShape): Bool
```

**功能：** 判断两个CheckBoxShape枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CheckBoxShape](#enum-checkboxshape)|是|-|要比较的另一个CheckBoxShape枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(CheckBoxShape)

```cangjie
public operator func !=(other: CheckBoxShape): Bool
```

**功能：** 判断两个CheckBoxShape枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CheckBoxShape](#enum-checkboxshape)|是|-|要比较的另一个CheckBoxShape枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|