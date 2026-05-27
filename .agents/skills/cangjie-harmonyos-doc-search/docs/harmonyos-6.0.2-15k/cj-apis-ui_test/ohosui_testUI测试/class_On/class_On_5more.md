## class On

```cangjie
public class On {
    public init()
}
```

**功能：** UiTest框架中，通过On类提供了丰富的控件特征描述API，用于进行控件筛选来匹配或查找出目标控件。

[On](#class-on)提供的API能力具有以下几个特点:

1、支持单属性匹配和多属性组合匹配，例如同时指定目标控件text和id。

2、控件属性支持多种匹配模式。

3、支持控件绝对定位，相对定位，可通过[isBefore](#func-isbeforeon)和[isAfter](#func-isafteron)等API限定邻近控件特征进行辅助定位。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### init()

```cangjie
public init()
```

**功能：** 创建[On](#class-on)实例。

**起始版本：** 12

### func checkable(Bool)

```cangjie
public func checkable(b!: Bool = true): On
```

**功能：** 指定目标控件能否被勾选状态属性，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|b|Bool|否|true| **命名参数。** 指定控件能否被勾选状态，true：能被勾选，false：不能被勾选。默认为false。|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件能否被勾选状态属性的[On](#class-on)对象。|

**示例：**

<!-- compile -->

```cangjie
//example_test.cj

import kit.TestKit.*

@Test
class TestExample00 {
    @TestCase
    func test00(): Unit {
        unittest()
    }
    @TestCase
    func test01(): Unit {
        let on: On = On().checkable(b: true) // 指定目标控件的能否被勾选状态属性。
    }
}
```

### func checked(Bool)

```cangjie
public func checked(b!: Bool = true): On
```

**功能：** 指定目标控件的被勾选状态属性，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|b|Bool|否|true| **命名参数。** 指定控件被勾选状态，true：被勾选，false：未被勾选。默认为false。|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件的被勾选状态属性的[On](#class-on)对象。|

**示例：**

<!-- compile -->

```cangjie
//example_test.cj

import kit.TestKit.*

@Test
class TestExample00 {
    @TestCase
    func test00(): Unit {
        unittest()
    }
    @TestCase
    func test01(): Unit {
        let on: On = On().checked(b: true) // 指定目标控件的被勾选状态属性
    }
}
```

### func clickable(Bool)

```cangjie
public func clickable(b!: Bool = true): On
```

**功能：** 指定目标控件的可点击状态属性，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|b|Bool|否|true| **命名参数。** 指定控件可点击状态，true：可点击，false：不可点击。默认为true。|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件的可点击状态属性的[On](#class-on)对象。|

**示例：**

<!-- compile -->

```cangjie
//example_test.cj

import kit.TestKit.*

@Test
class TestExample00 {
    @TestCase
    func test00(): Unit {
        unittest()
    }
    @TestCase
    func test01(): Unit {
        let on: On = On().clickable(b: true) // 指定目标控件的可点击状态属性。
    }
}
```