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

import ohos.app.ability.want.{Want, WantHandle}
import ohos.ability.ability_result.{AbilityResult, CJAbilityResult}
import ohos.ability.connect_options.ConnectOptions
import ohos.app.ability.configuration.{CConfiguration, Configuration}
import ohos.app.ability.dialog_request.RequestResult
import ohos.app.ability.open_link_options.CJOpenLinkOptions
import ohos.app.ability.start_options.{StartOptions, CJStartOptions,
    CJNewStartOptions, startOptionsToCJNewStartOptions, startOptionsToExternal}
import ohos.base.VectorInt32Handle
import ohos.business_exception.{BusinessException, AsyncCallback}
import ohos.bundle.bundle_manager.{RetAbilityInfoV2, RetHapModuleInfoV2, AbilityInfo, HapModuleInfo}
import ohos.ffi.RetDataBool
import ohos.multimedia.image.PixelMap
import ohos.window.WindowStage
import std.sync.{AtomicInt32, Mutex, AtomicInt64}
import std.collection.HashMap
import ohos.labels.{APILevel, Hide}

internal type AbilityInfoHandle = UIntNative

internal type HapModuleInfoHandle = UIntNative

internal type ConfigurationHandle = UIntNative

foreign {
    func FFIAbilityContextGetBroker(): CPointer<AbilityContextBroker>

    func FFIGetContext(id: Int64): CPointer<Unit>

    func free(ptr: CPointer<Unit>): Unit

    func FFICreateNapiValue(env: CPointer<Unit>, context: StageContext): CPointer<Unit>

    func FFIAbilityContextRequestDialogService(id: Int64, handle: WantHandle, callback: Int64): Int32

    func FFIAbilityContextGetFilesDir(id: Int64, accept: CFunc<(CString) -> Unit>): Unit

    func FFIAbilityContextMoveAbilityToBackground(id: Int64): Int32

    func FFIAbilityContextStartAbilityByType(id: Int64, cType: CString, cWantParams: CString, onError: Int64,
        onResult: Int64): Int32

    func FFIAbilityContextPropAbilityInfo(id: Int64, errCode: CPointer<Int32>): RetAbilityInfoV2

    func FFIAbilityContextPropCurrentHapModuleInfo(id: Int64, errCode: CPointer<Int32>): RetHapModuleInfoV2

    func FFIAbilityContextPropConfiguration(id: Int64, errCode: CPointer<Int32>): CConfiguration

    func FFIAbilityContextOpenLink(id: Int64, cLink: CString, cOpenLinkOptions: CJOpenLinkOptions, requestCode: Int32,
        lambdaId: Int64): Int32

    func FFIAbilityContextOpenAtomicService(id: Int64, cAppId: CString, cAtomicServiceOptions: CJAtomicServiceOptions,
        requestCode: Int32, lambdaId: Int64): Int32

    func FFIAbilityContextBackToCallerAbilityWithResult(id: Int64, cAbilityResult: CJAbilityResult, requestCode: CString): Int32

    func FFIAbilityContextSetRestoreEnabled(id: Int64, enabled: Bool): Int32

    func FFIAbilityContextSetMissionContinueState(id: Int64, state: Int32): Int32

    func FFIAbilityContextReportDrawnCompleted(id: Int64): Int32

    func FFIAbilityContextStartAbilityWithOptions(id: Int64, want: WantHandle, startOptions: CJNewStartOptions): Int32

    func FFIAbilityContextShowAbility(id: Int64): Int32

    func FFIAbilityContextHideAbility(id: Int64): Int32

    func FFIAbilityContextStartAbilityByCall(id: Int64, handle: WantHandle, callerId: CPointer<Int64>,
        remoteId: CPointer<Int64>): Int32
}

const SUCCESS_CODE: Int32 = 0

@C
struct AbilityContextBroker {
    private AbilityContextBroker(
        let isAbilityContextExisted: CFunc<(Int64) -> Bool>,
        let getSizeOfStartOptions: CFunc<() -> Int64>,
        let getAbilityInfo: CFunc<(Int64) -> AbilityInfoHandle>,
        let getHapModuleInfo: CFunc<(Int64) -> HapModuleInfoHandle>,
        let getConfiguration: CFunc<(Int64) -> ConfigurationHandle>,
        let startAbility: CFunc<(Int64, WantHandle) -> Int32>,
        let startAbilityWithOption: CFunc<(Int64, WantHandle, CPointer<CJStartOptions>) -> Int32>,
        let startAbilityWithAccount: CFunc<(Int64, WantHandle, Int32) -> Int32>,
        let startAbilityWithAccountAndOption: CFunc<(Int64, WantHandle, Int32, CPointer<CJStartOptions>) -> Int32>,
        let startServiceExtensionAbility: CFunc<(Int64, WantHandle) -> Int32>,
        let startServiceExtensionAbilityWithAccount: CFunc<(Int64, WantHandle, Int32) -> Int32>,
        let stopServiceExtensionAbility: CFunc<(Int64, WantHandle) -> Int32>,
        let stopServiceExtensionAbilityWithAccount: CFunc<(Int64, WantHandle, Int32) -> Int32>,
        let terminateSelf: CFunc<(Int64) -> Int32>,
        let terminateSelfWithResult: CFunc<(Int64, WantHandle, Int32) -> Int32>,
        let isTerminating: CFunc<(Int64) -> RetDataBool>,
        let connectAbility: CFunc<(Int64, WantHandle, Int64) -> Int32>,
        let connectAbilityWithAccount: CFunc<(Int64, WantHandle, Int32, Int64) -> Int32>,
        let disconnectAbility: CFunc<(Int64, WantHandle, Int64) -> Int32>,
        let startAbilityForResult: CFunc<(Int64, WantHandle, Int32, Int64) -> Int32>,
        let startAbilityForResultWithOption: CFunc<(Int64, WantHandle, CPointer<CJStartOptions>, Int32, Int64) -> Int32>,
        let startAbilityForResultWithAccount: CFunc<(Int64, WantHandle, Int32, Int32, Int64) -> Int32>,
        let startAbilityForResultWithAccountAndOption: CFunc<(Int64, WantHandle, Int32, CPointer<CJStartOptions>, Int32,
            Int64) -> Int32>,
        let requestPermissionsFromUser: CFunc<(Int64, VectorStringHandle, Int32, Int64) -> Int32>,
        let setMissionLabel: CFunc<(Int64, CString) -> Int32>,
        let setMissionIcon: CFunc<(Int64, Int64) -> Int32>
    ) {}
}

@C
struct CJPermissionRequestResult {
    CJPermissionRequestResult(
        let permissions: VectorStringHandle,
        let authResults: VectorInt32Handle
    ) {}
}

@C
struct CJAtomicServiceOptions {
    CJAtomicServiceOptions(
        let hasValue: Bool,
        let flags: Int32,
        let parameters: CString,
        let startOptions: CJNewStartOptions
    ) {}

    unsafe func free() {
        LibC.free(parameters)
    }
}

type StageContext = CPointer<Unit>

protected func getStageContext(abilityContext: UIAbilityContext): StageContext {
    unsafe {
        FFIGetContext(abilityContext.getID())
    }
}

class UIAbilityContextImpl {}

/**
 * The context of an ability. It allows access to ability-specific resources.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public open class UIAbilityContext <: Context {
    private static let BROKER: AbilityContextBroker = getBroker()

    // connectId is the id of the ability connected shared by all UIAbilityContext objects.
    private static var connectId = AtomicInt64(0)
    private static var abilityConnects = HashMap<Int64, (Want, ConnectOptions)>()

    // curRequestCode is the key of callbacks stored in native owned by UIAbilityContext instance.
    private var curRequestCode = AtomicInt32(0)
    private var mtx = Mutex()

    var windowStage_: ?WindowStage = None

    private let UIAbilityContextImpl_ = UIAbilityContextImpl()

    @!Hide[isChecked: true]
    internal mut prop abilityInfo: AbilityInfo {
        get() {
            throw Exception()
        }

        set(value) {
            throw Exception()
        }
    }

    @!Hide[isChecked: true]
    internal mut prop currentHapModuleInfo: HapModuleInfo {
        get() {
            throw Exception()
        }

        set(value) {
            throw Exception()
        }
    }

    @!Hide[isChecked: true]
    internal mut prop config: Configuration {
        get() {
            throw Exception()
        }

        set(value) {
            throw Exception()
        }
    }

    @!Hide[isChecked: true]
    internal mut prop windowStage: WindowStage {
        get() {
            throw Exception()
        }

        set(value) {
            throw Exception()
        }
    }

    init(id: Int64) {
        super(UIAbilityContext.create(id))
    }

    /**
     * @throws { BusinessException } 16000050 - Internal error.
     */
    private static func getBroker(): AbilityContextBroker {
        let nativeHandle = unsafe { FFIAbilityContextGetBroker() }
        if (nativeHandle.isNull()) {
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }

        let abilityContextBroker = unsafe { nativeHandle.read() }
        ABILITY_LOG.info("Get AbilityContextBroker successfully")
        return abilityContextBroker
    }

    /**
     * @throws { BusinessException } 16000050 - Internal error.
     */
    private static func create(id: Int64): Int64 {
        var status = unsafe { BROKER.isAbilityContextExisted(id) }
        if (status == true) {
            return id
        }
        throw BusinessException(ERROR_CODE_INNER, "Internal error.")
    }

    /**
     * Starts a new ability. If the caller application is in foreground, you can use this method to start ability;
     * If the caller application is in the background, you need to apply for
     * permission:ohos.permission.START_ABILITIES_FROM_BACKGROUND.
     * If the target ability is visible, you can start the target ability; If the target ability is invisible,
     * you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to start target invisible ability.
     * If the target ability is in cross-device, you need to apply for permission:ohos.permission.DISTRIBUTED_DATASYNC.
     *
     * @param { Want } want - Indicates the ability to start.
     * @param { ?StartOptions } [options] - Indicates the start options. The default value is None.
     * @throws { BusinessException } 201 - The application does not have permission to call the interface.
     * @throws { BusinessException } 801 - Capability not support.
     * @throws { BusinessException } 16000001 - The specified ability does not exist.
     * @throws { BusinessException } 16000002 - Incorrect ability type.
     * @throws { BusinessException } 16000004 - Cannot start an invisible component.
     * @throws { BusinessException } 16000005 - The specified process does not have the permission.
     * @throws { BusinessException } 16000006 - Cross-user operations are not allowed.
     * @throws { BusinessException } 16000008 - The crowdtesting application expires.
     * @throws { BusinessException } 16000009 - An ability cannot be started or stopped in Wukong mode.
     * @throws { BusinessException } 16000010 - The call with the continuation and prepare continuation flag is
     * forbidden.
     * @throws { BusinessException } 16000011 - The context does not exist.
     * @throws { BusinessException } 16000012 - The application is controlled.
     * @throws { BusinessException } 16000013 - The application is controlled by EDM.
     * @throws { BusinessException } 16000018 - Redirection to a third-party application is not allowed in API version
     * greater than 11.
     * @throws { BusinessException } 16000019 - No matching ability is found.
     * @throws { BusinessException } 16000050 - Internal error.
     * @throws { BusinessException } 16000053 - The ability is not on the top of the UI.
     * @throws { BusinessException } 16000055 - Installation-free timed out.
     * @throws { BusinessException } 16000067 - The StartOptions check failed.
     * @throws { BusinessException } 16000068 - The ability is already running.
     * @throws { BusinessException } 16000071 - App clone is not supported.
     * @throws { BusinessException } 16000072 - App clone or multi-instance is not supported.
     * @throws { BusinessException } 16000073 - The app clone index is invalid.
     * @throws { BusinessException } 16000076 - The app instance key is invalid.
     * @throws { BusinessException } 16000077 - The number of app instances reaches the limit.
     * @throws { BusinessException } 16000078 - The multi-instance is not supported.
     * @throws { BusinessException } 16000079 - The APP_INSTANCE_KEY cannot be specified.
     * @throws { BusinessException } 16000080 - Creating a new instance is not supported.
     * @throws { BusinessException } 16200001 - The caller has been released.
     * @throws { BusinessException } 16300003 - The target application is not the current application.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true,
        workerthread: true
    ]
    public func startAbility(want: Want, options!: ?StartOptions = None): Unit {
        var errorCode: Int32 = 0
        let wantHandle = want.createWantHandle()
        if (let Some(opt) <- options) {
            let cOptions = startOptionsToCJNewStartOptions(opt)
            errorCode = unsafe {
                FFIAbilityContextStartAbilityWithOptions(this.getID(), wantHandle, cOptions)
            }
        } else {
            errorCode = unsafe { BROKER.startAbility(this.getID(), wantHandle) }
        }
        unsafe { Want.releaseWantHandle(wantHandle) }
        checkCodeAndThrow(errorCode)
    }

    func startAbilityWithAccount(want: Want, accountId: Int32): Future<Unit> {
        spawn {
            let wantHandle = want.createWantHandle()
            let errorCode = unsafe { BROKER.startAbilityWithAccount(this.getID(), wantHandle, accountId) }
            unsafe { Want.releaseWantHandle(wantHandle) }
            ABILITY_LOG.info("startAbilityWithAccount: errorCode is ${errorCode}")
        }
    }

    func startAbilityWithAccount(want: Want, accountId: Int32, options: StartOptions): Future<Unit> {
        spawn {
            var cOptions = startOptionsToExternal(options)
            let wantHandle = want.createWantHandle()
            let errorCode = unsafe {
                BROKER.startAbilityWithAccountAndOption(this.getID(), wantHandle, accountId, inout cOptions)
            }
            unsafe { Want.releaseWantHandle(wantHandle) }
            ABILITY_LOG.info("startAbilityWithAccount: errorCode is ${errorCode}")
        }
    }

    func startServiceExtensionAbility(want: Want): Future<Unit> {
        spawn {
            let wantHandle = want.createWantHandle()
            let errorCode = unsafe { BROKER.startServiceExtensionAbility(this.getID(), wantHandle) }
            unsafe { Want.releaseWantHandle(wantHandle) }
            ABILITY_LOG.info("startServiceExtensionAbility: errorCode is ${errorCode}")
        }
    }

    func startServiceExtensionAbilityWithAccount(want: Want, accountId: Int32): Future<Unit> {
        spawn {
            let wantHandle = want.createWantHandle()
            let errorCode = unsafe { BROKER.startServiceExtensionAbilityWithAccount(this.getID(), wantHandle, accountId) }
            unsafe { Want.releaseWantHandle(wantHandle) }
            ABILITY_LOG.info("startServiceExtensionAbilityWithAccount: errorCode is ${errorCode}")
        }
    }

    func stopServiceExtensionAbility(want: Want): Future<Unit> {
        spawn {
            let wantHandle = want.createWantHandle()
            let errorCode = unsafe { BROKER.stopServiceExtensionAbility(this.getID(), wantHandle) }
            unsafe { Want.releaseWantHandle(wantHandle) }
            ABILITY_LOG.info("stopServiceExtensionAbility: errorCode is ${errorCode}")
        }
    }

    func stopServiceExtensionAbilityWithAccount(want: Want, accountId: Int32): Future<Unit> {
        spawn {
            let wantHandle = want.createWantHandle()
            let errorCode = unsafe { BROKER.stopServiceExtensionAbilityWithAccount(this.getID(), wantHandle, accountId) }
            unsafe { Want.releaseWantHandle(wantHandle) }
            ABILITY_LOG.info("stopServiceExtensionAbilityWithAccount: errorCode is ${errorCode}")
        }
    }

    /**
     * Destroys this Page ability.
     *
     * @throws { BusinessException } 16000009 - An ability cannot be started or stopped in Wukong mode.
     * @throws { BusinessException } 16000011 - The context does not exist.
     * @throws { BusinessException } 16000050 - Internal error.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true,
        workerthread: true
    ]
    public func terminateSelf(): Unit {
        let errorCode = unsafe { BROKER.terminateSelf(this.getID()) }
        checkCodeAndThrow(errorCode)
    }

    /**
     * Destroys the Page ability while returning the specified result code and data to the caller.
     *
     * @param { AbilityResult } parameter - Indicates the result to return.
     * @throws { BusinessException } 16000009 - An ability cannot be started or stopped in Wukong mode.
     * @throws { BusinessException } 16000011 - The context does not exist.
     * @throws { BusinessException } 16000050 - Internal error.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true,
        workerthread: true
    ]
    public func terminateSelfWithResult(parameter: AbilityResult): Unit {
        let wantHandle = parameter.want.createWantHandle()
        let errorCode = unsafe { BROKER.terminateSelfWithResult(this.getID(), wantHandle, parameter.resultCode) }
        unsafe { Want.releaseWantHandle(wantHandle) }
        checkCodeAndThrow(errorCode)
    }

    /**
     * Check to see ability is in terminating state.
     *
     * @returns { Bool } Returns true when ability is in terminating state, else returns false.
     * @throws { BusinessException } 16000011 - The context does not exist.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true
    ]
    public func isTerminating(): Bool {
        var res = unsafe { BROKER.isTerminating(this.getID()) }
        checkCodeAndThrow(res.code)
        return res.data
    }

    /**
     * @throws { BusinessError } 201 - The application does not have permission to call the interface.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.
     * @throws { BusinessError } 16000001 - The specified ability does not exist.
     * @throws { BusinessError } 16000002 - Incorrect ability type.
     * @throws { BusinessError } 16000004 - Cannot start an invisible component.
     * @throws { BusinessError } 16000005 - The specified process does not have the permission.
     * @throws { BusinessError } 16000006 - Cross-user operations are not allowed.
     * @throws { BusinessError } 16000008 - The crowdtesting application expires.
     * @throws { BusinessError } 16000011 - The context does not exist.
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 16000053 - The ability is not on the top of the UI.
     * @throws { BusinessError } 16000055 - Installation-free timed out.
     */
    func connectServiceExtensionAbility(want: Want, options: ConnectOptions): Int64 {
        let wantHandle = want.createWantHandle()
        var res = unsafe { BROKER.connectAbility(this.getID(), wantHandle, options.getID()) }
        unsafe { Want.releaseWantHandle(wantHandle) }
        if (res != 0) {
            throw BusinessException(res, getErrorMsg(res))
        }
        afterConnectAbility(want, res, options)
    }

    private func afterConnectAbility(want: Want, res: Int32, options: ConnectOptions) {
        if (res == SUCCESS_CODE) {
            connectId.fetchAdd(1)
            let id = connectId.load()
            synchronized(mtx) {
                abilityConnects.add(id, (want, options))
            }
            ABILITY_LOG.info("Connect Ability successfully and the connectId is ${id}")
            return id
        }
        options.onFailed(res)
        throw BusinessException(ERROR_CODE_INNER, "Internal error.")
    }

    func connectAbilityWithAccount(want: Want, accountId: Int32, options: ConnectOptions): Int64 {
        let wantHandle = want.createWantHandle()
        var res = unsafe { BROKER.connectAbilityWithAccount(this.getID(), wantHandle, accountId, options.getID()) }
        unsafe { Want.releaseWantHandle(wantHandle) }
        afterConnectAbility(want, res, options)
    }

    func disconnectAbility(connection: Int64): Future<Unit> {
        spawn {
            var item = abilityConnects.get(connection)
            match (item) {
                case None => ABILITY_LOG.error("Failed to get want and connectOptions, id is: ${connection}")
                case Some(connects) => dealDisconnectAbility(connection, connects)
            }
        }
    }

    private func dealDisconnectAbility(connection: Int64, connects: (Want, ConnectOptions)) {
        var wantHandle = connects[0].createWantHandle()
        var connectOptions = connects[1]
        let errorCode = unsafe { BROKER.disconnectAbility(this.getID(), wantHandle, connectOptions.getID()) }
        unsafe { Want.releaseWantHandle(wantHandle) }
        if (errorCode == SUCCESS_CODE) {
            synchronized(mtx) {
                abilityConnects.remove(connection)
            }
            ABILITY_LOG.info("Succeed to disconnect Ability")
        } else {
            ABILITY_LOG.error("Failed to disconnect Ability: errorCode is ${errorCode}")
        }
    }

    /**
     * Starts an ability and returns the execution result when the ability is destroyed. If the caller application is
     * in foreground,
     * you can use this method to start ability; If the caller application is in the background,
     * you need to apply for permission:ohos.permission.START_ABILITIES_FROM_BACKGROUND.
     * If the target ability is visible, you can start the target ability; If the target ability is invisible,
     * you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to start target invisible ability.
     * If the target ability is in cross-device, you need to apply for permission:ohos.permission.DISTRIBUTED_DATASYNC.
     *
     * @param { Want } want - Indicates the ability to start.
     * @param { AsyncCallback<AbilityResult> } callback - The callback is used to return the result of startAbility.
     * @throws { BusinessException } 201 - The application does not have permission to call the interface.
     * @throws { BusinessException } 16000001 - The specified ability does not exist.
     * @throws { BusinessException } 16000002 - Incorrect ability type.
     * @throws { BusinessException } 16000004 - Cannot start an invisible component.
     * @throws { BusinessException } 16000005 - The specified process does not have the permission.
     * @throws { BusinessException } 16000006 - Cross-user operations are not allowed.
     * @throws { BusinessException } 16000008 - The crowdtesting application expires.
     * @throws { BusinessException } 16000009 - An ability cannot be started or stopped in Wukong mode.
     * @throws { BusinessException } 16000010 - The call with the continuation and prepare continuation flag is
     * forbidden.
     * @throws { BusinessException } 16000011 - The context does not exist.
     * @throws { BusinessException } 16000012 - The application is controlled.
     * @throws { BusinessException } 16000013 - The application is controlled by EDM.
     * @throws { BusinessException } 16000018 - Redirection to a third-party application is not allowed in API version
     * greater than 11.
     * @throws { BusinessException } 16000019 - No matching ability is found.
     * @throws { BusinessException } 16000050 - Internal error.
     * @throws { BusinessException } 16000053 - The ability is not on the top of the UI.
     * @throws { BusinessException } 16000055 - Installation-free timed out.
     * @throws { BusinessException } 16000071 - App clone is not supported.
     * @throws { BusinessException } 16000072 - App clone or multi-instance is not supported.
     * @throws { BusinessException } 16000073 - The app clone index is invalid.
     * @throws { BusinessException } 16000076 - The app instance key is invalid.
     * @throws { BusinessException } 16000077 - The number of app instances reaches the limit.
     * @throws { BusinessException } 16000078 - The multi-instance is not supported.
     * @throws { BusinessException } 16000079 - The APP_INSTANCE_KEY cannot be specified.
     * @throws { BusinessException } 16000080 - Creating a new instance is not supported.
     * @throws { BusinessException } 16200001 - The caller has been released.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true
    ]
    public func startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): Unit {
        let requestCode = genRequestCode()
        let wantHandle = want.createWantHandle()
        let lambdaData = ResultCallbackForAbilityResult(callback)
        let errorCode = unsafe {
            BROKER.startAbilityForResult(this.getID(), wantHandle, requestCode, lambdaData.getID())
        }
        unsafe { Want.releaseWantHandle(wantHandle) }
        checkCodeAndThrow(errorCode)
    }

    /**
     * Starts an ability and returns the execution result when the ability is destroyed. If the caller application is
     * in foreground,
     * you can use this method to start ability; If the caller application is in the background,
     * you need to apply for permission:ohos.permission.START_ABILITIES_FROM_BACKGROUND.
     * If the target ability is visible, you can start the target ability; If the target ability is invisible,
     * you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to start target invisible ability.
     * If the target ability is in cross-device, you need to apply for permission:ohos.permission.DISTRIBUTED_DATASYNC.
     *
     * @param { Want } want - Indicates the ability to start.
     * @param { StartOptions } options - Indicates the start options.
     * @param { AsyncCallback<AbilityResult> } callback - The callback is used to return the result of startAbility.
     * @throws { BusinessException } 201 - The application does not have permission to call the interface.
     * @throws { BusinessException } 16000001 - The specified ability does not exist.
     * @throws { BusinessException } 16000004 - Cannot start an invisible component.
     * @throws { BusinessException } 16000005 - The specified process does not have the permission.
     * @throws { BusinessException } 16000006 - Cross-user operations are not allowed.
     * @throws { BusinessException } 16000008 - The crowdtesting application expires.
     * @throws { BusinessException } 16000009 - An ability cannot be started or stopped in Wukong mode.
     * @throws { BusinessException } 16000011 - The context does not exist.
     * @throws { BusinessException } 16000012 - The application is controlled.
     * @throws { BusinessException } 16000013 - The application is controlled by EDM.
     * @throws { BusinessException } 16000018 - Redirection to a third-party application is not allowed in API version
     * greater than 11.
     * @throws { BusinessException } 16000019 - No matching ability is found.
     * @throws { BusinessException } 16000050 - Internal error.
     * @throws { BusinessException } 16000053 - The ability is not on the top of the UI.
     * @throws { BusinessException } 16000055 - Installation-free timed out.
     * @throws { BusinessException } 16000071 - App clone is not supported.
     * @throws { BusinessException } 16000072 - App clone or multi-instance is not supported.
     * @throws { BusinessException } 16000073 - The app clone index is invalid.
     * @throws { BusinessException } 16000076 - The app instance key is invalid.
     * @throws { BusinessException } 16000077 - The number of app instances reaches the limit.
     * @throws { BusinessException } 16000078 - The multi-instance is not supported.
     * @throws { BusinessException } 16000079 - The APP_INSTANCE_KEY cannot be specified.
     * @throws { BusinessException } 16000080 - Creating a new instance is not supported.
     * @throws { BusinessException } 16200001 - The caller has been released.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true
    ]
    public func startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): Unit {
        let requestCode = genRequestCode()
        var cOptions = startOptionsToExternal(options)
        let wantHandle = want.createWantHandle()
        let lambdaData = ResultCallbackForAbilityResult(callback)
        let errorCode = unsafe {
            BROKER.startAbilityForResultWithOption(
                this.getID(),
                wantHandle,
                inout cOptions,
                requestCode,
                lambdaData.getID()
            )
        }
        unsafe { Want.releaseWantHandle(wantHandle) }
        checkCodeAndThrow(errorCode)
    }

    func startAbilityForResultWithAccount(
        want: Want,
        accountId: Int32,
        callback: AsyncCallback<AbilityResult>
    ): Unit {
        let requestCode = genRequestCode()
        let wantHandle = want.createWantHandle()
        let lambdaData = ResultCallbackForAbilityResult(callback)
        let errorCode = unsafe {
            BROKER.startAbilityForResultWithAccount(
                this.getID(),
                wantHandle,
                accountId,
                requestCode,
                lambdaData.getID()
            )
        }
        unsafe { Want.releaseWantHandle(wantHandle) }
        ABILITY_LOG.info("startAbilityForResultWithAccount: errorCode is ${errorCode}")
    }

    func startAbilityForResultWithAccount(
        want: Want,
        accountId: Int32,
        options: StartOptions,
        callback: AsyncCallback<AbilityResult>
    ): Unit {
        let requestCode = genRequestCode()
        var cOptions = startOptionsToExternal(options)
        let wantHandle = want.createWantHandle()
        let lambdaData = ResultCallbackForAbilityResult(callback)
        let errorCode = unsafe {
            BROKER.startAbilityForResultWithAccountAndOption(
                this.getID(),
                wantHandle,
                accountId,
                inout cOptions,
                requestCode,
                lambdaData.getID()
            )
        }
        unsafe { Want.releaseWantHandle(wantHandle) }
        ABILITY_LOG.info("startAbilityForResultWithAccount: errorCode is ${errorCode}")
    }

    func setMissionIcon(icon: PixelMap): Future<Unit> {
        spawn {
            let errorCode = unsafe { BROKER.setMissionIcon(this.getID(), icon.getID()) }
            ABILITY_LOG.info("setMissionIcon: errorCode is ${errorCode}")
        }
    }

    /**
     * Starts a service extension ability that supports modal dialog. If the caller application is in foreground,
     * you can use this method to start service extension ability; If the caller application is in the background,
     * you need to apply for permission:ohos.permission.START_ABILITIES_FROM_BACKGROUND.
     * If the target service extension ability is visible, you can start the target service extension ability;
     * If the target service extension ability is invisible,
     * you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to start target invisible service
     * extension ability.
     *
     * @param { Want } want - Indicates the dialog service to start.
     * @param { AsyncCallback<RequestResult> } result - The callback is used to return the request result.
     * @throws { BusinessException } 201 - The application does not have permission to call the interface.
     * @throws { BusinessException } 16000001 - The specified ability does not exist.
     * @throws { BusinessException } 16000002 - Incorrect ability type.
     * @throws { BusinessException } 16000004 - Cannot start an invisible component.
     * @throws { BusinessException } 16000005 - The specified process does not have the permission.
     * @throws { BusinessException } 16000006 - Cross-user operations are not allowed.
     * @throws { BusinessException } 16000008 - The crowdtesting application expires.
     * @throws { BusinessException } 16000009 - An ability cannot be started or stopped in Wukong mode.
     * @throws { BusinessException } 16000010 - The call with the continuation and prepare continuation flag is
     * forbidden.
     * @throws { BusinessException } 16000011 - The context does not exist.
     * @throws { BusinessException } 16000012 - The application is controlled.
     * @throws { BusinessException } 16000013 - The application is controlled by EDM.
     * @throws { BusinessException } 16000050 - Internal error.
     * @throws { BusinessException } 16000053 - The ability is not on the top of the UI.
     * @throws { BusinessException } 16000055 - Installation-free timed out.
     * @throws { BusinessException } 16200001 - The caller has been released.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true
    ]
    public func requestDialogService(want: Want, result: AsyncCallback<RequestResult>): Unit {
        let wantHandle = want.createWantHandle()
        let errorCode = unsafe {
            FFIAbilityContextRequestDialogService(this.getID(), wantHandle,
                ResultCallbackForDialogRequestResult(result).getID())
        }
        unsafe { Want.releaseWantHandle(wantHandle) }
        ABILITY_LOG.info("requestDialogService: errorCode is ${errorCode}")
    }

    private func genRequestCode(): Int32 {
        if (!curRequestCode.compareAndSwap(Int32.Max, 0)) {
            curRequestCode.fetchAdd(1)
        }
        curRequestCode.load()
    }
}
