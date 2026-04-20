## func getResourcePluralString(PluralResource)

```cangjie
public func getResourcePluralString(content: PluralResource): String
```

**功能：** 获取资源对象对应的单复数字符串资源值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content| [PluralResource](#class-pluralresource)|是|-|资源对象。|

**返回值：**

|类型|说明|
|:----|:----|
|String|单复数字符串资源值。|

## func getResourceStringArray(AppResource)

```cangjie
public func getResourceStringArray(res: AppResource): Array<String>
```

**功能：** 获取资源对象对应的字符串数组资源值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|res| [AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|资源对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|字符串数组资源值。|

## func getResourceUInt32(AppResource)

```cangjie
public func getResourceUInt32(res: AppResource): UInt32
```

**功能：** 获取资源对象对应的无符号整型资源值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|res| [AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|资源对象。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|无符号整型资源值。|

## func hasContainer()

```cangjie
public func hasContainer(): Bool
```

**功能：** 判断是否在容器上下文中，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|判断结果。|

## func loadNativeView(CustomView)

```cangjie
public func loadNativeView(view: CustomView): Bool
```

**功能：** UI框架使用的基础函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|view|[CustomView](#class-customview)|是|-|-|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|-|

## func throwNativeError(String)

```cangjie
public func throwNativeError(msg: String): Unit
```

**功能：** 异常抛出接口。内部接口，UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|msg|String|是|-|错误信息。|

## interface ArrayLike

```cangjie
public interface ArrayLike<T> {
    prop size: Int64
    operator func [](idx: Int64, value!: T): Unit
    operator func [](idx: Int64): T
}
```

**功能：** 数组类型。内部接口，框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### prop size

```cangjie
prop size: Int64
```

**功能：** 数组大小。

**类型：** Int64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func [](Int64, T)

```cangjie
operator func [](idx: Int64, value!: T): Unit
```

**功能：** 在指定索引处写入数组元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|idx|Int64|是|-|索引值。|
|value|T|是|-| **命名参数。** 写入值。|

### func []\(Int64)

```cangjie
operator func [](idx: Int64): T
```

**功能：** 通过索引获取数组元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|idx|Int64|是|-|索引值。|

**返回值：**

|类型|说明|
|:----|:----|
|T|数组元素。|