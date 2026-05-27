#### func size()

```cangjie
public func size(): Int64
```

**功能：** 返回LocalStorage中的属性数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|LocalStorage中属性的数量。|

**示例：**

```cangjie
let storage = LocalStorage()
let tmp = storage.setOrCreate("PropA", 47)
let size = storage.size()
```