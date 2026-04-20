## enum TextHeightAdaptivePolicy

```cangjie
public enum TextHeightAdaptivePolicy <: Equatable<TextHeightAdaptivePolicy> {
    | MaxLinesFirst
    | MinFontSizeFirst
    | LayoutConstraintFirst
    | ...
}
```

**功能：** 设置文本高度自适应方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[TextHeightAdaptivePolicy](#enum-textheightadaptivepolicy)>

### MaxLinesFirst

```cangjie
MaxLinesFirst
```

**功能：** 设置文本高度自适应方式为以MaxLines优先。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### MinFontSizeFirst

```cangjie
MinFontSizeFirst
```

**功能：** 设置文本高度自适应方式为以缩小字体优先。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### LayoutConstraintFirst

```cangjie
LayoutConstraintFirst
```

**功能：** 设置文本高度自适应方式为以布局约束（高度）优先。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(TextHeightAdaptivePolicy)

```cangjie
public operator func ==(other: TextHeightAdaptivePolicy): Bool
```

**功能：** 判断两个TextHeightAdaptivePolicy枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextHeightAdaptivePolicy](#enum-textheightadaptivepolicy)|是|-|要比较的另一个TextHeightAdaptivePolicy枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(TextHeightAdaptivePolicy)

```cangjie
public operator func !=(other: TextHeightAdaptivePolicy): Bool
```

**功能：** 判断两个TextHeightAdaptivePolicy枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextHeightAdaptivePolicy](#enum-textheightadaptivepolicy)|是|-|要比较的另一个TextHeightAdaptivePolicy枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|