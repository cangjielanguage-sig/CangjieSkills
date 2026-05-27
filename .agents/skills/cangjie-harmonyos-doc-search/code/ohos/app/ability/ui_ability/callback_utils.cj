/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// The Cangjie API is in Beta. For details on its capabilities and limitations, please refer to the README file.

package ohos.app.ability.ui_ability

import ohos.ability.ability_result.{AbilityResult, CJAbilityResult}
import ohos.app.ability.dialog_request.{RequestResult, ResultCode, CJDialogRequestResult}
import ohos.app.ability.want.Want
import ohos.business_exception.{BusinessException, AsyncCallback}
import std.collection.HashMap
import std.sync.{AtomicInt64, Mutex}

class ResultCallbackForAbilityResult {
    private static var callbacks = HashMap<Int64, AsyncCallback<AbilityResult>>()
    private static var id = AtomicInt64(0)
    private static var mtx = Mutex()
    private var id_: Int64

    init(callback: AsyncCallback<AbilityResult>) {
        synchronized(mtx) {
            id.fetchAdd(1)
            id_ = id.load()
            setCallback(callback)
        }
    }

    static func getCallback(callbackId: Int64): Option<AsyncCallback<AbilityResult>> {
        callbacks.get(callbackId)
    }

    static func deleteCallback(callbackId: Int64): Unit {
        callbacks.remove(callbackId)
    }

    func getID(): Int64 {
        return id_
    }

    func setCallback(callback: AsyncCallback<AbilityResult>): Unit {
        let instanceId = id.load()
        callbacks.add(instanceId, callback)
    }
}

class ResultCallbackForDialogRequestResult {
    private static var callbacks = HashMap<Int64, AsyncCallback<RequestResult>>()
    private static var id = AtomicInt64(0)
    private static var mtx = Mutex()
    private var id_: Int64

    init(callback: AsyncCallback<RequestResult>) {
        synchronized(mtx) {
            id.fetchAdd(1)
            id_ = id.load()
            setCallback(callback)
        }
    }

    static func getCallback(callbackId: Int64): Option<AsyncCallback<RequestResult>> {
        callbacks.get(callbackId)
    }

    static func deleteCallback(callbackId: Int64): Unit {
        callbacks.remove(callbackId)
    }

    func getID(): Int64 {
        return id_
    }

    func setCallback(callback: AsyncCallback<RequestResult>): Unit {
        let instanceId = id.load()
        callbacks.add(instanceId, callback)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func invokeAbilityResultCallback(id: Int64, error: Int32, cjAbilityResult: CPointer<CJAbilityResult>): Unit {
    let res = ResultCallbackForAbilityResult.getCallback(id)
    match (res) {
        case None =>
            ABILITY_LOG.error("Invalid id, failed to get ResultCallbackForAbilityResult")
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(callback) =>
            if (error != 0 || cjAbilityResult.isNull()) {
                callback(BusinessException(error, getErrorMsg(error)), Option<AbilityResult>.None)
                ResultCallbackForAbilityResult.deleteCallback(id)
                ABILITY_LOG.info("Invoke ResultCallbackForAbilityResult end and error code is ${error}")
                return
            }

            let cjResult = unsafe { cjAbilityResult.read() }
            let abilityResult = AbilityResult(cjResult.resultCode, want: Want(cjResult.wantHandle))
            callback(None, Option<AbilityResult>.Some(abilityResult))
            ResultCallbackForAbilityResult.deleteCallback(id)
            ABILITY_LOG.info("Invoke ResultCallbackForAbilityResult end")
    }
}

@C
func invokePermissionRequestResultCallback(
    _: Int64,
    _: Int32,
    _: CPointer<CJPermissionRequestResult>
): Unit {}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func invokeDialogRequestResultCallback(
    id: Int64,
    error: Int32,
    cjDialogRequestResult: CPointer<CJDialogRequestResult>
): Unit {
    let res = ResultCallbackForDialogRequestResult.getCallback(id)
    match (res) {
        case None => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(callback) =>
            if (error != 0 || cjDialogRequestResult.isNull()) {
                callback(BusinessException(error, getErrorMsg(error)), Option<RequestResult>.None)
                ResultCallbackForDialogRequestResult.deleteCallback(id)
                ABILITY_LOG.info("Invoke ResultCallbackForDialogRequestResult end, error code is ${error}")
                return
            }

            let nativeResult = unsafe { cjDialogRequestResult.read() }
            let result = RequestResult(ResultCode.parse(nativeResult.result), want: Want(nativeResult.wantHandle))
            callback(None, Option<RequestResult>.Some(result))
            ResultCallbackForDialogRequestResult.deleteCallback(id)
            ABILITY_LOG.info("Invoke ResultCallbackForDialogRequestResult end")
    }
}

@C
protected struct CJAbilityResultCbInfo {
    protected CJAbilityResultCbInfo(
        let lambdaId: Int64,
        let cjCallback: CFunc<(Int64, Int32, CPointer<CJAbilityResult>) -> Unit>
    ) {}
}

unsafe func getCJAbilityResultCbInfo(callback: ?AsyncCallback<AbilityResult>): CJAbilityResultCbInfo {
    let lambdaDataId = if (let Some(v) <- callback) {
        ResultCallbackForAbilityResult(v).getID()
    } else {
        -1 // No callback
    }
    return CJAbilityResultCbInfo(lambdaDataId, invokeAbilityResultCallback)
}

@C
struct CJAbilityCallbacks {
    CJAbilityCallbacks(
        let invokeAbilityResultCallback: CFunc<(Int64, Int32, CPointer<CJAbilityResult>) -> Unit>,
        let invokePermissionRequestResultCallback: CFunc<(Int64, Int32, CPointer<CJPermissionRequestResult>) -> Unit>,
        let invokeDialogRequestResultCallback: CFunc<(Int64, Int32, CPointer<CJDialogRequestResult>) -> Unit>
    ) {}
}

@C
func cjAbilityCallbacksRegister(result: CPointer<CJAbilityCallbacks>): Unit {
    let cjFuncs = CJAbilityCallbacks(
        invokeAbilityResultCallback,
        invokePermissionRequestResultCallback,
        invokeDialogRequestResultCallback
    )
    unsafe { result.write(cjFuncs) }
}

foreign func RegisterCJAbilityCallbacks(callbacks: CFunc<(CPointer<CJAbilityCallbacks>) -> Unit>): Unit

let REGISTER_ABILITY_CONTEXT_CALLBACK = unsafe { RegisterCJAbilityCallbacks(cjAbilityCallbacksRegister) }
