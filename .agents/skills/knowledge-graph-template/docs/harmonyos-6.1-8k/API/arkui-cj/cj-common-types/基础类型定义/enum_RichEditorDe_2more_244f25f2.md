## enum RichEditorDeleteDirection

```cangjie
public enum RichEditorDeleteDirection <: Equatable<RichEditorDeleteDirection> {
    | Backward
    | Forward
    | ...
}
```

**功能：** 表示删除操作的方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[RichEditorDeleteDirection](#enum-richeditordeletedirection)>

### Backward

```cangjie
Backward
```

**功能：** 表示向后删除。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Forward

```cangjie
Forward
```

**功能：** 表示向前删除。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(RichEditorDeleteDirection)

```cangjie
public operator func ==(other: RichEditorDeleteDirection): Bool
```

**功能：** 判断两个RichEditorDeleteDirection枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RichEditorDeleteDirection](#enum-richeditordeletedirection)|是|-|要比较的另一个RichEditorDeleteDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(RichEditorDeleteDirection)

```cangjie
public operator func !=(other: RichEditorDeleteDirection): Bool
```

**功能：** 判断两个RichEditorDeleteDirection枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RichEditorDeleteDirection](#enum-richeditordeletedirection)|是|-|要比较的另一个RichEditorDeleteDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum MixedMode

```cangjie
public enum MixedMode <: Equatable<MixedMode> {
    | All
    | Compatible
    | None
    | ...
}
```

**功能：** 设置混合内容安全加载模式。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**父类型：**

- Equatable\<[MixedMode](#enum-mixedmode)>

### All

```cangjie
All
```

**功能：** 宽松模式：允许加载HTTP和HTTPS混合内容。所有不安全的内容都可以被加载。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### Compatible

```cangjie
Compatible
```

**功能：** 兼容模式：混合内容兼容性模式，部分不安全的内容可能被加载。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### None

```cangjie
None
```

**功能：** 严格模式：不允许加载HTTP和HTTPS混合内容。不允许安全来源（secure origin）加载不安全来源（insecure origin）的内容。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### operator func ==(MixedMode)

```cangjie
public operator func ==(other: MixedMode): Bool
```

**功能：** 判断两个MixedMode枚举是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MixedMode](#enum-mixedmode)|是|-|要比较的另一个MixedMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(MixedMode)

```cangjie
public operator func !=(other: MixedMode): Bool
```

**功能：** 判断两个MixedMode枚举是否不相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MixedMode](#enum-mixedmode)|是|-|要比较的另一个MixedMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|