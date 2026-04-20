# LazyForEach

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

在大量子组件的场景下，LazyForEach与缓存列表项、动态预加载、组件复用等方法配合使用，可以进一步提升滑动帧率并降低应用内存占用。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## interface IDataSource\<T>

```cangjie
public interface IDataSource<T> {
    func totalCount(): Int64
    func getData(index: Int64): T
    func registerDataChangeListener(listener: DataChangeListener): Unit
    func unregisterDataChangeListener(listener: DataChangeListener): Unit
}
```

**功能：** LazyForEach数据源，需要开发者实现相关接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func getData(Int64)

```cangjie
func getData(index: Int64): T
```

**功能：** 获取索引值index对应的数据。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|数据对应的索引值。|

**返回值：**

|类型|说明|
|:----|:----|
|T|索引值index对应的数据。|

### func registerDataChangeListener(DataChangeListener)

```cangjie
func registerDataChangeListener(listener: DataChangeListener): Unit
```

**功能：** 注册数据改变的监听器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|listener|[DataChangeListener](#class-datachangelistener)|是|-|数据变化监听器。|

### func unregisterDataChangeListener(DataChangeListener)

```cangjie
func unregisterDataChangeListener(listener: DataChangeListener): Unit
```

**功能：** 注销数据改变的监听器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int64|数据总数。|