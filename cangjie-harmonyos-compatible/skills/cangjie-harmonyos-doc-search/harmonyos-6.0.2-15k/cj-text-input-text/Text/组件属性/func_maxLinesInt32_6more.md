### func maxLines(Int32)

```cangjie
public func maxLines(value: Int32): This
```

**功能：** 设置文本的最大行数。

> **说明：**
>
> 默认情况下，文本是自动折行的，如果指定此属性，则文本最多不会超过指定的行。如果有多余的文本，可以通过[textOverflow](#func-textoverflowtextoverflow)来指定截断方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|文本的最大行数。|

### func maxFontScale(Float32)

```cangjie
public func maxFontScale(value: Float32): This
```

**功能：** 设置文本最大的字体缩放倍数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float32|是|-|文本最大的字体缩放倍数。<br>取值范围：[1, +∞)。<br>设置的值小于1时，按值为1处理，异常值默认不生效。|

### func maxFontSize(Length)

```cangjie
public func maxFontSize(value: Length): This
```

**功能：** 根据Length设置文本最大显示字号。

> **说明：**
>
> - 需配合[minFontSize](#func-minfontsizelength)以及[maxLines](#func-maxlinesint32)或布局大小限制使用，单独设置不生效，对子组件和属性字符串不生效。
> - 自适应字号生效时，fontSize设置不生效。
> - maxFontSize小于或等于0时，自适应字号不生效，此时按照[fontSize](#func-fontsizelength)属性的值生效，未设置时按照其默认值生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|文本最大显示字号。单位：fp。|

### func minFontScale(Float32)

```cangjie
public func minFontScale(value: Float32): This
```

**功能：** 设置文本最小的字体缩放倍数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float32|是|-|文本最小的字体缩放倍数。取值范围：(0, 1]。设置的值小于0时，按值为0处理，设置的值大于1，按值为1处理，异常值默认不生效。|

### func minFontSize(Length)

```cangjie
public func minFontSize(value: Length): This
```

**功能：** 根据Length设置文本最小显示字号。

> **说明：**
>
> - 需配合[maxFontSize](#func-maxfontsizelength)以及[maxLines](#func-maxlinesint32)或布局大小限制使用，单独设置不生效，对子组件和属性字符串不生效。
> - 自适应字号生效时，fontSize设置不生效。
> - minFontSize小于或等于0时，自适应字号不生效，此时按照[fontSize](#func-fontsizelength)属性的值生效，未设置时按照其默认值生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|文本最小显示字号。单位：fp。|

### func privacySensitive(Bool)

```cangjie
public func privacySensitive(value: Bool): This
```

**功能：** 设置是否支持卡片敏感隐私信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否支持卡片敏感隐私信息。<br>初始值：false。当设置为true时，隐私模式下文字将被遮罩为横杠“-”样式。进入隐私模式需要卡片框架支持。|