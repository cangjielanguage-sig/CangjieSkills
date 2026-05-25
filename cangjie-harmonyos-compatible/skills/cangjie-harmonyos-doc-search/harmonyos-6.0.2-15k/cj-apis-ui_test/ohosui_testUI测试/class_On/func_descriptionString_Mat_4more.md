### func description(String, ?MatchPattern)

```cangjie
public func description(val: String, pattern!: ?MatchPattern = None): On
```

**功能：** 指定目标控件的描述属性，支持多种匹配模式，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|String|是|-|控件的描述属性。|
|pattern|?[MatchPattern](#enum-matchpattern)|否|None| **命名参数。** 指定的文本匹配模式，默认为EQUALS。|

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
        let on: On = On().description("123") // 指定目标控件的控件类型属性。
    }
}
```

### func enabled(Bool)

```cangjie
public func enabled(b!: Bool = true): On
```

**功能：** 指定目标控件的使能状态属性，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|b|Bool|否|true| **命名参数。** 指定控件使能状态，true：使能，false：未使能。默认为true。|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件的使能状态属性的[On](#class-on)对象。|

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
        let on: On = On().enabled(b: true) // 指定目标控件的使能状态属性。
    }
}
```

### func focused(Bool)

```cangjie
public func focused(b!: Bool = true): On
```

**功能：** 指定目标控件的获焦状态属性，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|b|Bool|否|true| **命名参数。** 控件获焦状态，true：获焦，false：未获焦。默认为true。|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件的获焦状态属性的[On](#class-on)对象。|

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
        let on: On = On().focused(b: true) // 指定目标控件的获焦状态属性。
    }
}
```

### func id(String)

```cangjie
public func id(id: String): On
```

**功能：** 指定目标控件id属性，返回[On](#class-on)对象自身。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|指定控件的id值。|

**返回值：**

|类型|说明|
|:----|:----|
|[On](#class-on)|返回指定目标控件id属性的[On](#class-on)对象。|

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
        let on: On = On().id("123") // 指定目标控件的id属性。
    }
}
```