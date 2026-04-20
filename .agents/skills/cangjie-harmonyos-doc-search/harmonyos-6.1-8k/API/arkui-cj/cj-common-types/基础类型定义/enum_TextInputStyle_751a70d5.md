## enum TextInputStyle

```cangjie
public enum TextInputStyle <: Equatable<TextInputStyle> {
    | Default
    | Inline
    | ...
}
```

**功能：** 表示输入风格。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[TextInputStyle](#enum-textinputstyle)>

### Default

```cangjie
Default
```

**功能：** 表示默认风格，光标宽1.5.vp，光标高度与文本选中底板高度和字体大小相关。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Inline

```cangjie
Inline
```

**功能：** 表示内联输入风格。文本选中底板高度与输入框高度相同。内联输入适用于需要明显区分编辑状态和非编辑状态的场景，如文件列表视图中的重命名。内联输入不支持`showError`属性，并且在内联模式下不支持拖入文本功能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(TextInputStyle)

```cangjie
public operator func ==(other: TextInputStyle): Bool
```

**功能：** 判断两个TextInputStyle枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextInputStyle](#enum-textinputstyle)|是|-|要比较的另一个TextInputStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(TextInputStyle)

```cangjie
public operator func !=(other: TextInputStyle): Bool
```

**功能：** 判断两个TextInputStyle枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextInputStyle](#enum-textinputstyle)|是|-|要比较的另一个TextInputStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|