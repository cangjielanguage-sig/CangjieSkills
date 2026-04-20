func initSession(keyAlias: String, huksOptions: HuksOptions, throwObject: throwObject) {
    return try {
        initSession(keyAlias, huksOptions)
    } catch (e: Exception) {
        throwObject.isThrow = true
        throw e
    }
}

func publicInitFunc(keyAlias: String, huksOptions: HuksOptions) {
    loggerInfo("enter doInit")
    let throwObject: throwObject = throwObject(false)
    try {
        handle = initSession(keyAlias, huksOptions, throwObject).handle
    } catch (e: Exception) {
        loggerInfo("doInit input arg invalid, ${e}")
    }
}

func updateSession(handle: HuksHandleId, huksOptions: HuksOptions, throwObject: throwObject) {
    return try {
        updateSession(handle, huksOptions)
    } catch (e: Exception) {
        throwObject.isThrow = true
        throw e
    }
}

func publicUpdateFunc(handle: HuksHandleId, huksOptions: HuksOptions) {
    loggerInfo("enter doUpdate")
    let throwObject: throwObject = throwObject(false)
    try {
        updateSession(handle, huksOptions, throwObject)
    } catch (e: Exception) {
        loggerInfo("doUpdate input arg invalid, ${e}")
    }
}

func finishSession(handle: HuksHandleId, huksOptions: HuksOptions, throwObject: throwObject) {
    return try {
        finishSession(handle, huksOptions)
    } catch (e: Exception) {
        throwObject.isThrow = true
        throw e
    }
}

func publicFinishFunc(handle: HuksHandleId, huksOptions: HuksOptions) {
    loggerInfo("enter doFinish")
    let throwObject: throwObject = throwObject(false)
    try {
        finishSession(handle, huksOptions, throwObject)
    } catch (e: Exception) {
        loggerInfo("doFinish input arg invalid, ${e}")
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
    loggerInfo("enter deleteKeyItem")
    let throwObject: throwObject = throwObject(false)
    try {
        deleteKeyItem(keyAlias, huksOptions, throwObject)
    } catch (e: Exception) {
        loggerInfo("deleteKeyItem input arg invalid, ${e}")
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