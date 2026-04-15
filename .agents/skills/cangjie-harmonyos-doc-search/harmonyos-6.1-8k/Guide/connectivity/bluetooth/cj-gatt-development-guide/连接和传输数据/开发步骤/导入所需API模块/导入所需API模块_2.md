相关API请参考[readCharacteristicValue](../../reference/ConnectivityKit/cj-apis-bluetooth-ble.md#func-readcharacteristicvalueblecharacteristic-asynccallbackblecharacteristic)和[writeCharacteristicValue](../../reference/ConnectivityKit/cj-apis-bluetooth-ble.md#func-writecharacteristicvalueblecharacteristic-gattwritetype-asynccallbackunit)。

- 导入模块。

<!-- compile -->

```cangjie
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.*
```

- 读取或写入特征值。

```cangjie
// 此处是伪代码
let device = 'XX:XX:XX:XX:XX:XX'
let bufferDesc: Array<Byte> = [11, 0]
let descriptor = BleDescriptor(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    "00002902-0000-1000-8000-00805F9B34FB",
    bufferDesc
)
let descriptors: Array<BleDescriptor> = [descriptor]
let bufferCCC: Array<Byte> = [1, 0]
let characteristic: BleCharacteristic = BleCharacteristic(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    bufferCCC,
    descriptors
)

var gattClient: ?GattClientDevice = None
try {
    gattClient = createGattClientDevice("XX:XX:XX:XX:XX:XX")
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}

// 读取特征值
try {
    gattClient?.readCharacteristicValue(characteristic) {
        error: ?BusinessException, outData: ?BleCharacteristic =>
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}

// 写入特征值
try {
    gattClient?.writeCharacteristicValue(characteristic, GattWriteType.Write) {
        error: ?BusinessException, c: ?Unit => if (let Some(e) <- error) {
            Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
        }
        Hilog.info(0, "Bluetooth", "writeCharacteristicValue success")
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

**5.2 读取或写入描述符**

读取描述符操作，可以获取服务端描述符的数据内容。

写入描述符操作，可以更新服务端描述符的数据内容。

相关API请参考[readDescriptorValue](../../reference/ConnectivityKit/cj-apis-bluetooth-ble.md#func-readdescriptorvaluebledescriptor-asynccallbackbledescriptor)和[writeDescriptorValue](../../reference/ConnectivityKit/cj-apis-bluetooth-ble.md#func-writedescriptorvaluebledescriptor-asynccallbackunit)。

- 导入模块。

<!-- compile -->

```cangjie
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.*
```

- 读取或写入描述符。

```cangjie
// 此处是伪代码
let device = 'XX:XX:XX:XX:XX:XX'
let bufferDesc: Array<Byte> = [11, 0]
let descriptor = BleDescriptor(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    "00002903-0000-1000-8000-00805F9B34FB",
    bufferDesc
)

var gattClient: ?GattClientDevice = None
try {
    gattClient = createGattClientDevice("XX:XX:XX:XX:XX:XX")
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}

// 读取描述符
try {
    gattClient?.readDescriptorValue(descriptor) {
        error: ?BusinessException, outDescriptor: ?BleDescriptor =>
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}

// 写入描述符
try {
    gattClient?.writeDescriptorValue(descriptor) {
        error: ?BusinessException, c: ?Unit => if (let Some(e) <- error) {
            Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
        }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

**5.3 接收服务端特征值变化通知或指示**