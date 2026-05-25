# ohos.app.form.formBindingData（卡片数据绑定类）

卡片数据绑定模块提供卡片数据绑定的能力。包括FormBindingData对象的创建、相关信息的描述。

## 导入模块

```cangjie
import kit.FormKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func createFormBindingData(?String)

```cangjie
public func createFormBindingData(obj!: ?String = None): FormBindingData
```

**功能：** 创建一个FormBindingData对象。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|obj|?String|否|None| **命名参数。** 卡片要展示的数据。其中图片数据以'formImages'作为标识，内容为图片标识与图片文件描述符的键值对{'formImages': {'key1': fd1, 'key2': fd2}}。|

**返回值：**

|类型|说明|
|:----|:----|
|[FormBindingData](#class-formbindingdata)|根据传入数据创建的FormBindingData对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.FormKit.*

let json = '{ "name" : "hello" , "imgSrc" : "image"}'
let formbindingdata = createFormBindingData(obj: json)
```

## class FormBindingData

```cangjie
public class FormBindingData {
    public FormBindingData (
        public var data: String,
        public var proxies!: ?Array<ProxyData> = Array<ProxyData>()
    )
}
```

**功能：** 卡片绑定数据相关信息描述。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 19

### var data

```cangjie
public var data: String
```

**功能：** 卡片要展示的数据。可以是包含若干键值对的String或者json格式的字符串。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var proxies

```cangjie
public var proxies: ?Array<ProxyData> = Array<ProxyData>()
```

**功能：** 卡片代理刷新的订阅信息，默认为空数组。

**类型：** ?Array\<[ProxyData](#class-proxydata)>

**读写能力：** 可读写

**起始版本：** 19

### FormBindingData(String, ?Array\<ProxyData>)

```cangjie
public FormBindingData (
    public var data: String,
    public var proxies!: ?Array<ProxyData> = Array<ProxyData>()
)
```

**功能：** 构造FormBindingData对象。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|String|是|-|卡片要展示的数据。可以是包含若干键值对的json格式的字符串。|
|proxies|?Array\<[ProxyData](#class-proxydata)>()|否|Array\<ProxyData>()| **命名参数。** 卡片代理刷新的订阅信息，默认为空数组。|