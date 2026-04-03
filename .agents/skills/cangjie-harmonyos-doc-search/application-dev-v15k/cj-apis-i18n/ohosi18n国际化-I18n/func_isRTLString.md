## func isRTL(String)

```cangjie
public func isRTL(locale: String): Bool
```

**功能：** 判断某区域语言是否从右到左显示。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示输入的字符是从右到左语言的字符，返回false表示输入的字符不是从右到左语言的字符。|