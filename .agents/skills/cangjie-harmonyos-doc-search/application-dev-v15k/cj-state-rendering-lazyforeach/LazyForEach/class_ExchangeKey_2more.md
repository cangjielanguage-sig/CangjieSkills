## class ExchangeKey

```cangjie
public class ExchangeKey {
    public ExchangeKey(public let start!: String = "", public let end!: String = "")
}
```

**功能：** 键值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let start

```cangjie
public let start: String = ""
```

**功能：** 为第一个交换的位置分配新的键值，默认使用原键值。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let end

```cangjie
public let end: String = ""
```

**功能：** 为第二个交换的位置分配新的键值，默认使用原键值。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### ExchangeKey(String, String)

```cangjie
public ExchangeKey(public let start!: String = "", public let end!: String = "")
```

**功能：** 创建一个ExchangeKey类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|String|否|""| **命名参数。** 为第一个交换的位置分配新的键值，默认使用原键值。|
|end|String|否|""| **命名参数。** 为第二个交换的位置分配新的键值，默认使用原键值。|

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.*

public class Student {
    public Student(
        let name: String,
        let id: Int64
    ) {}
}

class StudentDataSource <: IDataSource<Student> {
    public StudentDataSource(let data_: ArrayList<Student>) {}
    public var listenerOp: Option<DataChangeListener> = None
    public func totalCount(): Int64 {
        return data_.size
    }
    public func getData(index: Int64): Student {
        return data_[index]
    }

    public func onRegisterDataChangeListener(listener: DataChangeListener): Unit {
        listenerOp = listener
    }

    public func onUnregisterDataChangeListener(listener: DataChangeListener): Unit {
        listenerOp = None
    }

    public func notifyChange(): Unit {
        let listener: DataChangeListener = listenerOp.getOrThrow()
        listener.onDataReloaded()
    }
}

func getDS(): StudentDataSource {
    let data: ArrayList<Student> = ArrayList<Student>()
    for (i in 0..10) {
        data.add(Student("name ${i}", i * i))
    }
    let dataSourceStu: StudentDataSource = StudentDataSource(data)
    return dataSourceStu
}

let dataSourceStu: StudentDataSource = getDS()
var changeID: Int64 = 0

@Entry
@Component
public class EntryView {
    public func build(): Unit {
        Column(30) {
            Column {
                LazyForEach(
                    dataSourceStu,
                    itemGeneratorFunc: {
                        stu: Student, idx: Int64 => Column {
                            Text(stu.name)
                        }
                    }
                )
            }.height(220.0)

            Text("click to notifyChange").onClick(
                {
                evt => if (changeID < dataSourceStu.data_.size) {
                    dataSourceStu.data_.remove(at: changeID)
                    dataSourceStu.data_.add(Student("xiaoming", 10086), at: changeID)
                    dataSourceStu.notifyChange()
                    changeID += 1
                }
            })
        }
    }
}
```

![lazyforeach](figures/lazyforeach.gif)