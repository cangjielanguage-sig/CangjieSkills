### func rowsGap(Length)

```cangjie
public func rowsGap(size: Length): This
```

**功能：** 设置行与行的间距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](cj-common-types.md#interface-length)|是|-|行与行的间距。<br/>初始值：0。<br/>取值范围：[0, +∞)。|

### func rowsTemplate(String)

```cangjie
public func rowsTemplate(value: String): This
```

**功能：** 设置当前瀑布流组件布局行的数量，不设置时默认1行。

例如, '1fr 1fr 2fr'是将父组件分三行，将父组件允许的高分为4等份，第一行占1份，第二行占一份，第三行占2份。

可使用rowsTemplate('repeat(auto-fill,track-size)')根据给定的行高track-size自动计算行数，其中repeat、auto-fill为关键字，track-size为可设置的高度，支持的单位包括px、vp、%或有效数字，默认单位为vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|当前瀑布流组件布局行的数量。<br/>初始值："1fr"。|