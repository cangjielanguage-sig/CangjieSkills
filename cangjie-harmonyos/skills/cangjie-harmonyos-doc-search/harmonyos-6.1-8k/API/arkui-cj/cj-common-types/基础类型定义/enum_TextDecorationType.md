## enum TextDecorationType

```cangjie
public enum TextDecorationType <: Equatable<TextDecorationType> {
    | None
    | Underline
    | Overline
    | LineThrough
    | ...
}
```

**功能：** 装饰线类型枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[TextDecorationType](#enum-textdecorationtype)>

### None

```cangjie
None
```

**功能：** 不使用文本装饰线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Underline

```cangjie
Underline
```

**功能：** 在文字下方加下划线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Overline

```cangjie
Overline
```

**功能：** 文字上划线修饰。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### LineThrough

```cangjie
LineThrough
```

**功能：** 穿过文本的修饰线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(TextDecorationType)

```cangjie
public operator func ==(other: TextDecorationType): Bool
```

**功能：** 判断两个TextDecorationType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextDecorationType](#enum-textdecorationtype)|是|-|要比较的另一个TextDecorationType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(TextDecorationType)

```cangjie
public operator func !=(other: TextDecorationType): Bool
```

**功能：** 判断两个TextDecorationType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextDecorationType](#enum-textdecorationtype)|是|-|要比较的另一个TextDecorationType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|