### func onDatasetChange(ArrayList\<DataOperation>)

```cangjie
public func onDatasetChange(dataOperations: ArrayList<DataOperation>): Unit
```

**功能：** 进行批量的数据处理后，调用onDatasetChange接口通知组件按照dataOperations刷新组件。

> **说明：**
>
> onDatasetChange接口不能与其他DataChangeListener的更新接口混用。如在同一个LazyForEach中，调用过onDataAdd接口后，不能再调用onDatasetChange接口；反之，调用过onDatasetChange接口后，也不能调用onDataAdd等其他更新接口。页面中不同LazyForEach之间互不影响。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dataOperations|ArrayList\<[DataOperation](#interface-dataoperation)>|是|-|一次处理数据的操作。|