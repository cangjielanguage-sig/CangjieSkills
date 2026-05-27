// 7. 在确保拿到了server端的服务结果后，写入server端特定服务的描述符时调用
        public func writeDescriptorValue() {
            if (this.gattClient.isNone() || this.connectState != ProfileConnectionState.STATE_CONNECTED) {
                AppLog.error('no gattClient or not connected')
                return
            }
            if (!this.found) { // 要确保server端有对应的descriptor
                AppLog.error('no descriptor from server')
                return
            }

            let descBuffer: Array<UInt8> = [11, 12]
            let descriptor = this.initDescriptor(this.mySecondDescriptorUuid, descBuffer)
            AppLog.info('writeDescriptorValue')
            try {
                this.gattClient?.writeDescriptorValue(descriptor) {
                    err =>
                    if (let Some(e) <- err) {
                        AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
                        return
                    }
                    AppLog.info('writeDescriptorValue success')
                }
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }

        // 8.client端主动断开时调用
        public func stopConnect() {
            if (this.gattClient.isNone() || this.connectState != ProfileConnectionState.STATE_CONNECTED) {
                AppLog.error('no gattClient or not connected')
                return
            }

            AppLog.info('stopConnect ' + this.device.getOrThrow())
            try {
                this.gattClient?.disconnect() // 8.1 断开连接
                this.gattClient?.off(BluetoothBleGattClientDeviceCallbackType.BLE_CONNECTION_STATE_CHANGE)
                this.gattClient?.close() // 8.2 如果不再使用此gattClient，则需要close
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }
    }

    class ChangeStateCb <: Callback1Argument<BLEConnectionChangeState> {
        public func invoke(stateInfo: BLEConnectionChangeState) {
            let state = match (stateInfo.state) {
                case STATE_DISCONNECTED => 'DISCONNECTED'

                case STATE_CONNECTING => 'CONNECTING'

                case STATE_CONNECTED => 'CONNECTED'

                case STATE_DISCONNECTING => 'DISCONNECTING'

                case _ => 'undefined'
            }
            AppLog.info('onGattClientStateChange: device=' + stateInfo.deviceId + ', state=' + state)
        }
    }

    let gattClientManager = GattClientManager()
    ```

8. 错误码请参见[蓝牙服务子系统错误码](../../../API_Reference/source_zh_cn/errorcodes/cj-errorcode-bluetooth_manager.md)。