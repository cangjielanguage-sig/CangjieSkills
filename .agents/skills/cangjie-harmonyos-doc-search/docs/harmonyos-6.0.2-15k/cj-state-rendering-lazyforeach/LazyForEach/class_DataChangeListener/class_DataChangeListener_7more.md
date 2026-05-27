## class DataChangeListener

```cangjie
public class DataChangeListener {
    public DataChangeListener(id: Int64)
}
```

**功能：** 数据变化监听器。

> **说明：**
>
> DataChangeListener除onDatasetChange以外的方法中，当参数包含index且值为负数时，会默认用0来替换。
> onDatasetChange中，当单个DataOperation参数包含index且值在数据源索引范围之外（DataAddOperation中index可以等于数据源长度），则对应DataOperation不会生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### DataChangeListener(Int64)

```cangjie
public DataChangeListener(id: Int64)
```

**功能：** 创建一个DataChangeListener类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|是|-|监听器ID。|

### func onDataAdd(Int64)

```cangjie
public func onDataAdd(index: Int64): Unit
```

**功能：** 通知组件index的位置有数据添加。添加数据完成后调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|数据添加位置的索引值。|

### func onDataChange(Int64)

```cangjie
public func onDataChange(index: Int64): Unit
```

**功能：** 通知组件index的位置有数据有变化。改变数据完成后调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|数据变化位置的索引值。|

### func onDataDelete(Int64)

```cangjie
public func onDataDelete(index: Int64): Unit
```

**功能：** 通知组件删除index位置的数据并刷新LazyForEach的展示内容。删除数据完成后调用。

> **说明：**
>
> 需要保证dataSource中的对应数据已经在调用onDataDelete前删除，否则页面渲染将出现未定义的行为。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|数据删除位置的索引值。|

### func onDataMove(Int64, Int64)

```cangjie
public func onDataMove(fromIdx: Int64, toIdx: Int64): Unit
```

**功能：** 通知组件数据有移动。将fromIdx和toIdx位置的数据进行交换。数据移动起始位置与数据移动目标位置交换完成后调用。

> **说明：**
>
> 数据移动前后键值要保持不变，如果键值有变化，应使用删除数据和新增数据接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fromIdx|Int64|是|-|数据移动起始位置。|
|toIdx|Int64|是|-|数据移动目标位置。|

### func onDataReloaded()

```cangjie
public func onDataReloaded(): Unit
```

**功能：** 通知组件重新加载所有数据。键值没有变化的数据项会使用原先的子组件，键值发生变化的会重建子组件。重新加载数据完成后调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12