## interface DataOperation

```cangjie
public interface DataOperation {}
```

**功能：** 数据操作公共类型定义。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## interface IDataSource

```cangjie
public interface IDataSource<T> {
    func totalCount(): Int64
    func getData(index: Int64): T
    func onRegisterDataChangeListener(listener: DataChangeListener): Unit
    func onUnregisterDataChangeListener(listener: DataChangeListener): Unit
}
```

**功能：** LazyForEach数据源，需要开发者实现相关接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func getData(Int64)

```cangjie
func getData(index: Int64): T
```

**功能：** 获取索引值index对应的数据。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|数据对应的索引值。|

**返回值：**

|类型|说明|
|:----|:----|
|T|索引值index对应的数据。|

### func onRegisterDataChangeListener(DataChangeListener)

```cangjie
func onRegisterDataChangeListener(listener: DataChangeListener): Unit
```

**功能：** 注册数据改变的监听器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|listener|[DataChangeListener](#class-datachangelistener)|是|-|数据变化监听器。|

### func onUnregisterDataChangeListener(DataChangeListener)

```cangjie
func onUnregisterDataChangeListener(listener: DataChangeListener): Unit
```

**功能：** 注销数据改变的监听器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|listener|[DataChangeListener](#class-datachangelistener)|是|-|数据变化监听器。|

### func totalCount()

```cangjie
func totalCount(): Int64
```

**功能：** 获得数据总数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|数据总数。|