## class CJLeakWatcher\<T>

```cangjie
public class CJLeakWatcher<T> where T <: Object {}
```

**功能：** 泄露检测者类，用于检查仓颉对象是否疑似泄露。

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**起始版本：** 20

### func enable(Bool)

```cangjie
public func enable(flag: Bool) : Unit
```

**功能：** 使能仓颉对象泄露检测。

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|flag|Bool|是|-|是否使能CJLeakWatcher。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

var leakobj = CJLeakWatcher()
leakobj.enable(true)
```

### func watch(T, String)

```cangjie
public func watch(obj: T, msg: String) : Unit
```

**功能：** 注册待检测泄露的对象。

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**起始版本：** 20

**参数：**

| 参数名 | 类型   | 必填 |默认值| 说明             |
| :----- | :----- | :--- |:---| :--------------- |
| obj    | T | 是   |-   | 类型T需是Object类的子类，obj为需要检测的对象。 |
| msg    | String | 是   |-   | 自定义对象信息。 |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

class A {
    var x1: Bool = true
    init(inputA: Bool) {
        x1 = inputA
    }
    func toString() {
        AppLog.error("A")
    }
}

var leakobj = CJLeakWatcher()
leakobj.enable(true)

let obj1 = ArrayList<A>(5000, {i => A(false)})
leakobj.watch(obj1, "Object-1")
```

### func check()

```cangjie
public func check() : ArrayList<String>
```

**功能：** 获取已通过CJLeakWatcher.watch注册且可能发生泄露的对象列表，触发GC后未被回收的对象会被标记为泄露。

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|ArrayList\<String>|疑似泄漏对象的msg表。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

class A {
    var x1: Bool = true
    init(inputA: Bool) {
        x1 = inputA
    }
    func toString() {
        AppLog.error("A")
    }
}

var leakobj = CJLeakWatcher()
leakobj.enable(true)

let obj1 = ArrayList<A>(5000, {i => A(false)})
leakobj.watch(obj1, "Object-1")

let leakList = leakobj.check()
```

### func dump(String)

```cangjie
public func dump(path: String) : ArrayList<String>
```

**功能：** 获取已通过CJLeakWatcher.watch注册且可能发生泄露的对象列表，触发GC后未被回收的对象会被标记为泄露，将对象列表写入到.leakList为后缀的文件中。同时生成堆快照，生成.dumpHeapData为后缀的快照文件。

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**起始版本：** 20

**参数：**

| 参数名 | 类型   | 必填 |默认值| 说明             |
| :----- | :----- | :--- |:---| :--------------- |
| path | String | 是 |-| 导出信息生成的文件存放的路径。 |

**返回值：**

|类型|说明|
|:----|:----|
|ArrayList\<String>|返回疑似泄漏对象列表文件、仓颉堆快照的文件名列表。|

**异常：**

- FSException：传入路径不存在

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

class A {
    var x1: Bool = true
    init(inputA: Bool) {
        x1 = inputA
    }
    func toString() {
        AppLog.error("A")
    }
}

var leakobj = CJLeakWatcher()
leakobj.enable(true)

let obj1 = ArrayList<A>(5000, {i => A(false)})
leakobj.watch(obj1, "Object-1")

let fileList = leakobj.dump("<your file path>")
```