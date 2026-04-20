## enum RichEditorSpanType

```cangjie
public enum RichEditorSpanType <: Equatable<RichEditorSpanType> {
    | Text
    | Image
    | Mixed
    | ...
}
```

**功能：** 表示Span类型信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[RichEditorSpanType](#enum-richeditorspantype)>

### Text

```cangjie
Text
```

**功能：** 表示Span为文字类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Image

```cangjie
Image
```

**功能：** 表示Span为图像类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Mixed

```cangjie
Mixed
```

**功能：** 表示Span为图文混合类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(RichEditorSpanType)

```cangjie
public operator func ==(other: RichEditorSpanType): Bool
```

**功能：** 判断两个RichEditorSpanType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RichEditorSpanType](#enum-richeditorspantype)|是|-|要比较的另一个RichEditorSpanType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(RichEditorSpanType)

```cangjie
public operator func !=(other: RichEditorSpanType): Bool
```

**功能：** 判断两个RichEditorSpanType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RichEditorSpanType](#enum-richeditorspantype)|是|-|要比较的另一个RichEditorSpanType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|