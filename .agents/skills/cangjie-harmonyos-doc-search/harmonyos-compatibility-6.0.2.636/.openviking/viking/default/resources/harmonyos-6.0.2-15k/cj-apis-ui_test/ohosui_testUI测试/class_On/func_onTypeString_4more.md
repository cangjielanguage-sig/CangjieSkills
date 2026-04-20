### func onType(String)

```cangjie
public func onType(tp: String): On
```

**功能：** 指定目标控件的控件类型属性，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tp|String|是|-|指定控件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件的控件类型属性的[On](#class-on)对象。|

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
        let on: On = On().onType("Button") // 指定目标控件的控件类型属性。
    }
}
```

### func scrollable(Bool)

```cangjie
public func scrollable(b!: Bool = true): On
```

**功能：** 指定目标控件的可滑动状态属性，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|b|Bool|否|true| **命名参数。** 控件可滑动状态，true：可滑动，false：不可滑动。默认为true。|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件的可滑动状态属性的[On](#class-on)对象。|

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
        let on: On = On().scrollable(b: true) // 指定目标控件的可滑动状态属性。
    }
}
```

### func selected(Bool)

```cangjie
public func selected(b!: Bool = true): On
```

**功能：** 指定目标控件的被选中状态属性，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|b|Bool|否|true| **命名参数。** 指定控件被选中状态，true：被选中，false：未被选中。默认为true。|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件的被选中状态属性的[On](#class-on)对象。|

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
        let on: On = On().selected(b: true) // 指定目标控件的被选中状态属性。
    }
}
```

### func text(String, MatchPattern)

```cangjie
public func text(txt: String, pattern!: MatchPattern = MatchPattern.EQUALS): On
```

**功能：** 指定目标控件文本属性，支持多种匹配模式，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|txt|String|是|-|指定控件文本，用于匹配目标控件文本。|
|pattern|[MatchPattern](#enum-matchpattern)|否|[MatchPattern](#enum-matchpattern).EQUALS| **命名参数。** 指定的文本匹配模式，默认为EQUALS。|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件文本属性的[On](#class-on)对象。|

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
        let on: On = On().text("123") // 指定目标控件的text属性。
    }
}
```