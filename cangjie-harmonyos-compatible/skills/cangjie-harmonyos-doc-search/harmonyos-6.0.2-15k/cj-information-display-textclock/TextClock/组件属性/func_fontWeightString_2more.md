### func fontWeight(String)

```cangjie
public func fontWeight(value: String): This
```

**功能：** 设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|文本的字体粗细。仅支持Int64类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。|

### func format(String)

```cangjie
public func format(value: String): This
```

**功能：** 设置显示时间格式，如“yyyy/MM/dd”、“yyyy-MM-dd”。

y：年（yyyy表示完整年份，yy表示年份后两位）

M：月（若想使用01月则使用MM）

d：日（若想使用01日则使用dd）

E：星期（若想使用星期六则使用EEEE，若想使用周六则使用E、EE、EEE）H：小时（24小时制） h：小时（12小时制）

m：分钟

s：秒

SS：厘秒(format中S个数<3，全部按厘秒处理)

SSS：毫秒(format中S个数>=3，全部按毫秒处理)

a：上午/下午（当设置小时制式为H时，该参数不生效）

日期间隔符："年月日"、“/”、"-"、"."（可以自定义间隔符样式，间隔符不可以为字母，汉字则作为间隔符处理）

允许自行拼接组合显示格式，即：年、月、日、星期、时、分、秒、毫秒可拆分为子元素，可自行排布组合。时间更新频率最高为一秒一次，不建议单独设置厘秒和毫秒格式。

当设置无效字母时（非上述字母被认为是无效字母），该字母会被忽略。如果format全是无效字母时，显示格式跟随系统语言和系统小时制。例如系统语言为中文时，12小时制显示格式为yyyy/MM/dd aa hh:mm:ss.SSS，24小时制显示格式为yyyy/MM/dd HH:mm:ss.SSS。

若format为空，则使用初始值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|设置显示时间格式，如 `yyyy/MM/dd`、`yyyy-MM-dd`。|

以下是format输入的格式样式及对应的显示效果：

|输入格式|显示效果|
|:---|:---|
|yyyy年M月d日 EEEE|2023年2月4日 星期六|
|yyyy年M月d日|2023年2月4日|
|M月d日 EEEE|2月4日 星期六|
|M月d日|2月4日|
|MM/dd/yyyy|02/04/2023|
|EEEE MM月dd日|星期六 02月04日|
|yyyy（完整年份）|2023年|
|yy（年份后两位）|23年|
|MM（完整月份）|02月|
|M（月份）|2月|
|dd（完整日期）|04日|
|d（日期）|4日|
|EEEE（完整星期）|星期六|
|E、EE、EEE（简写星期）|周六|
|yyyy年M月d日|2023年2月4日|
|yyyy/M/d|2023/2/4|
|yyyy-M-d|2023-2-4|
|yyyy.M.d|2023.2.4|
|HH:mm:ss（时:分:秒）|17:00:04|
|aa hh:mm:ss（时:分:秒）|上午 5:00:04|
|hh:mm:ss（时:分:秒）|5:00:04|
|HH:mm（时:分）|17:00|
|aa hh:mm（时:分）|上午 5:00|
|hh:mm（时:分）|5:00|
|mm:ss（分:秒）|00:04|
|mm:ss.SS（分:秒.厘秒）|00:04.91|
|mm:ss.SSS（分:秒.毫秒）|00:04.536|
|hh:mm:ss aa|5:00:04 上午|
|HH|17|