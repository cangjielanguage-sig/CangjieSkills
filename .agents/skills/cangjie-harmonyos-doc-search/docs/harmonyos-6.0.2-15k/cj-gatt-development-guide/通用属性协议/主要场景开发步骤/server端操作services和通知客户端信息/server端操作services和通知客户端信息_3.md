class DescriptorWriteRequestCb <: Callback1Argument<DescriptorWriteRequest> {
        public func invoke(desReq: DescriptorWriteRequest): Unit {
            let deviceId: String = desReq.deviceId
            let transId: Int32 = desReq.transId
            let offset: Int32 = desReq.offset
            AppLog.info('receive descriptorWrite: needRsp=${desReq.needRsp}')
            if (!desReq.needRsp) {
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
    ```

8. 错误码请参见[蓝牙服务子系统错误码](../../../API_Reference/source_zh_cn/errorcodes/cj-errorcode-bluetooth_manager.md)。