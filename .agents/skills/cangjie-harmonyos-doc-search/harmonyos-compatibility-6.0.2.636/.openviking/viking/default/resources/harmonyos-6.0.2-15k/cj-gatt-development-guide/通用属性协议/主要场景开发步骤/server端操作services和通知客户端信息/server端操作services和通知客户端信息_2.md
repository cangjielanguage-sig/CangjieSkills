AppLog.info('onDescriptorRead')
            try {
                this.gattServer?.on(BluetoothBleGattServerCallbackType.DESCRIPTOR_READ, DescriptorReadRequestCb())
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }

        // 6. 订阅来自gattClient的写入描述符请求时调用
        public func onDescriptorWrite() {
            if (this.gattServer.isNone()) {
                AppLog.error('no gattServer')
                return
            }

            AppLog.info('onDescriptorWrite')
            try {
                this.gattServer?.on(BluetoothBleGattServerCallbackType.DESCRIPTOR_WRITE, DescriptorWriteRequestCb())
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }

        // 7. server端删除服务，不再使用时调用
        public func unRegisterServer() {
            if (this.gattServer.isNone()) {
                AppLog.error('no gattServer')
                return
            }

            AppLog.info('unRegisterServer ' + this.myServiceUuid)
            try {
                this.gattServer?.removeService(this.myServiceUuid) // 7.1 删除服务
                this.gattServer?.off(BluetoothBleGattServerCallbackType.CONNECTION_STATE_CHANGE)
                this.gattServer?.close() // 7.3 如果不再使用此gattServer，则需要close
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

    let gattServerManager = GattServerManager()

    class ReadRequestCb <: Callback1Argument<CharacteristicReadRequest> {
        public func invoke(charReq: CharacteristicReadRequest): Unit {
            let deviceId: String = charReq.deviceId
            let transId: Int32 = charReq.transId
            let offset: Int32 = charReq.offset
            AppLog.info('receive characteristicRead')
            let rspBuffer: Array<UInt8> = [21, 22]
            let serverResponse: ServerResponse = ServerResponse(
                deviceId,
                transId,
                0, // 0表示成功
                offset,
                rspBuffer
            )

            try {
                gattServerManager.gattServer?.sendResponse(serverResponse)
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }
    }

    class WriteRequestCb <: Callback1Argument<CharacteristicWriteRequest> {
        public func invoke(charReq: CharacteristicWriteRequest): Unit {
            let deviceId: String = charReq.deviceId
            let transId: Int32 = charReq.transId
            let offset: Int32 = charReq.offset
            AppLog.info('receive characteristicWrite: needRsp=${charReq.needRsp}')
            if (!charReq.needRsp) {
                return
            }
            let rspBuffer: Array<UInt8> = [0]
            let serverResponse: ServerResponse = ServerResponse(
                deviceId,
                transId,
                0, // 0表示成功
                offset,
                rspBuffer
            )

            try {
                gattServerManager.gattServer?.sendResponse(serverResponse)
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }
    }

    class DescriptorReadRequestCb <: Callback1Argument<DescriptorReadRequest> {
        public func invoke(desReq: DescriptorReadRequest): Unit {
            let deviceId: String = desReq.deviceId
            let transId: Int32 = desReq.transId
            let offset: Int32 = desReq.offset
            AppLog.info('receive descriptorRead')
            let rspBuffer: Array<UInt8> = [31, 32]
            let serverResponse: ServerResponse = ServerResponse(
                deviceId,
                transId,
                0, // 0表示成功
                offset,
                rspBuffer
            )

            try {
                gattServerManager.gattServer?.sendResponse(serverResponse)
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }
    }