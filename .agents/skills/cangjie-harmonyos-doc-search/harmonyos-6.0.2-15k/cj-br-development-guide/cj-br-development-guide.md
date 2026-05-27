# 蓝牙设置

## 简介

蓝牙设置主要提供了开启蓝牙、关闭蓝牙、获取蓝牙状态的方法，帮助开发者实现基本蓝牙功能。

## 场景介绍

主要场景有：

- 开启、关闭蓝牙

## 接口说明

完整的仓颉 API 说明以及实例代码请参见：[access 接口](../../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-bluetooth-access.md)。

具体接口说明如下表。

| 接口名 | 功能描述 |
| ---------------------------------- | --------------------------------------------------- |
| enableBluetooth() | 开启蓝牙。 |
| disableBluetooth() | 关闭蓝牙。 |
| getState() | 获取蓝牙开关状态。 |
| on(`type`: BluetoothAccessCallbackType) | 订阅蓝牙设备开关状态事件。 |
| off(`type`: BluetoothAccessCallbackType) | 取消订阅蓝牙设备开关状态事件。 |

## 主要场景开发步骤

### 开启、关闭蓝牙

1. import需要的access模块。
2. 需要SystemCapability.Communication.Bluetooth.Core系统能力。
3. 开启蓝牙。
4. 关闭蓝牙。
5. 示例代码：

    ```cangjie
    import kit.ConnectivityKit.*
    import ohos.base.Callback1Argument

    func test() {
        // 开启蓝牙
        enableBluetooth()
        on(BluetoothAccessCallbackType.STATE_CHANGE, BluetoothStateCb())

        // 关闭蓝牙
        disableBluetooth()
        on(BluetoothAccessCallbackType.STATE_CHANGE, BluetoothStateCb())
    }

    class BluetoothStateCb <: Callback1Argument<BluetoothState> {
        public func invoke(data: BluetoothState): Unit {
            var btStateMessage = ''
            match (data) {
                case STATE_OFF => btStateMessage += 'STATE_OFF'
                case STATE_TURNING_ON => btStateMessage += 'STATE_TURNING_ON'
                case STATE_ON => btStateMessage += 'STATE_ON'
                case STATE_TURNING_OFF => btStateMessage += 'STATE_TURNING_OFF'
                case STATE_BLE_TURNING_ON => btStateMessage += 'STATE_BLE_TURNING_ON'
                case STATE_BLE_ON => btStateMessage += 'STATE_BLE_ON'
                case STATE_BLE_TURNING_OFF => btStateMessage += 'STATE_BLE_TURNING_OFF'
                case _ => btStateMessage += 'unknown status'
            }
            if (btStateMessage == 'STATE_ON') {
                off(BluetoothAccessCallbackType.STATE_CHANGE)
            }
            AppLog.info('bluetooth statues: ' + btStateMessage)
        }
    }
    ```

6. 错误码请参见[蓝牙服务子系统错误码](../../../API_Reference/source_zh_cn/errorcodes/cj-errorcode-bluetooth_manager.md)。

7. 验证：执行开启蓝牙代码，记录日志“bluetooth statues: STATE_ON”，则表示开启蓝牙成功。执行关闭蓝牙代码，记录日志“bluetooth statues: STATE_OFF”，则表示蓝牙关闭成功。
