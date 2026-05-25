func publicUpdateFunc(handle: HuksHandle, huksOptions: HuksOptions) {
    AppLog.info("enter doUpdate")
    let throwObject: throwObject = throwObject(false)
    try {
        updateSession(handle, huksOptions, throwObject)
    } catch (e: Exception) {
        AppLog.error("doUpdate input arg invalid, ${e}")
    }
}

func finishSession(handle: HuksHandle, huksOptions: HuksOptions, throwObject: throwObject) {
    return try {
        finishSession(handle, huksOptions)
    } catch (e: Exception) {
        throwObject.isThrow = true
        throw e
    }
}

func publicFinishFunc(handle: HuksHandle, huksOptions: HuksOptions) {
    AppLog.info("enter doFinish")
    let throwObject: throwObject = throwObject(false)
    try {
        finishSession(handle, huksOptions, throwObject)
    } catch (e: Exception) {
        AppLog.error("doFinish input arg invalid, ${e}")
    }
}

func deleteKeyItem(keyAlias: String, huksOptions: HuksOptions, throwObject: throwObject) {
    try {
        deleteKeyItem(keyAlias, huksOptions)
    } catch (e: Exception) {
        throwObject.isThrow = true
        throw e
    }
}

func publicDeleteKeyFunc(keyAlias: String, huksOptions: HuksOptions) {
    AppLog.info("enter deleteKeyItem")
    let throwObject: throwObject = throwObject(false)
    try {
        deleteKeyItem(keyAlias, huksOptions, throwObject)
    } catch (e: Exception) {
        AppLog.error("deleteKeyItem input arg invalid, ${e}")
    }
}

func testDerive() {
    /* 生成密钥 */
    publicGenKeyFunc(srcKeyAlias, huksOptions)
    /* 进行派生操作 */
    publicInitFunc(srcKeyAlias, initOptions)
    initOptions.inData = StringToUint8Array(deriveHkdfInData)
    publicUpdateFunc(handle.getOrThrow(), initOptions)
    publicFinishFunc(handle.getOrThrow(), finishOptions)
    publicDeleteKeyFunc(srcKeyAlias, huksOptions)
}
```