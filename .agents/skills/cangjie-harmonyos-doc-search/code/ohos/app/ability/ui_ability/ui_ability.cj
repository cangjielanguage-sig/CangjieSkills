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

import ohos.app.ability.ability_constant.{LastExitReason, LaunchReason, LaunchParam,
    OnContinueResult, StateType, OnSaveResult}
import ohos.app.ability.want.{Want, WantHandle}
import ohos.app.ability.configuration.{CConfiguration, CJConfiguration}
import ohos.base.FFIVectorString
import ohos.ffi.{FFIDataManager}
import ohos.window.WindowStage
import ohos.encoding.json.{jsonObjectWrapper, jsonStringUnWrapper}

import ohos.labels.{APILevel, Hide}
import ohos.business_exception.BusinessException

type AbilityHandle = UIntNative

type VectorStringHandle = CPointer<Unit>

type WindowStageHandle = Int64

foreign func FFIAbilityGetAbilityContext(handle: AbilityHandle): Int64

@C
struct CJAbilityFuncs {
    CJAbilityFuncs(
        let createAbility: CFunc<(CString) -> Int64>,
        let releaseAbility: CFunc<(Int64) -> Unit>,
        let abilityOnStart: CFunc<(Int64, WantHandle, CJLaunchParam) -> Unit>,
        let abilityOnStop: CFunc<(Int64) -> Unit>,
        let abilityOnSceneCreated: CFunc<(Int64, WindowStageHandle) -> Unit>,
        let abilityOnSceneRestored: CFunc<(Int64, WindowStageHandle) -> Unit>,
        let abilityOnSceneDestroyed: CFunc<(Int64) -> Unit>,
        let abilityOnForeground: CFunc<(Int64, WantHandle) -> Unit>,
        let abilityOnBackground: CFunc<(Int64) -> Unit>,
        let abilityOnConfigurationUpdated: CFunc<(Int64, CJConfiguration) -> Unit>,
        let abilityOnNewWant: CFunc<(Int64, WantHandle, CJLaunchParam) -> Unit>,
        let abilityDump: CFunc<(Int64, VectorStringHandle) -> VectorStringHandle>,
        let abilityOnContinue: CFunc<(Int64, CString) -> Int32>,
        let abilityInit: CFunc<(Int64, AbilityHandle) -> Unit>,
        let abilityOnBackPress: CFunc<(Int64) -> Bool>,
        let abilityOnSceneWillDestroy: CFunc<(Int64, WindowStageHandle) -> Unit>,
        let abilityOnConfigurationUpdate: CFunc<(Int64, CConfiguration) -> Unit>,
        let abilityOnMemoryLevel: CFunc<(Int64, Int32) -> Unit>,
        let abilityOnPrepareTerminate: CFunc<(Int64) -> Bool>,
        let abilityOnSaveState: CFunc<(Int64, Int32, CString) -> CJNumberParmas>,
        let abilityOnShare: CFunc<(Int64, CString) -> CString>,
        let abilityOnContinueWithParams: CFunc<(Int64, CString) -> CJNumberParmas>,
        let abilityOnCallRequest: CFunc<(Int64) -> Int64>,
        let abilityOnSetCalleeFlag: CFunc<(Int64, Bool) -> Unit>
    ) {}
}

@C
struct CJNumberParmas {
    CJNumberParmas(
        let numberResult: Int32,
        let params: CString
    ) {}
}

@C
struct CJLaunchParam {
    CJLaunchParam(
        let launchReason: Int32,
        let lastExitReason: Int32,
        let lastExitMessage: CString
    ) {}
}

@C
func createAbility(name: CString): Int64 {
    let optAbility = UIAbility.create(name.toString())
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("Failed to load Ability: " + name.toString())
            0
        case Some(ability) =>
            FFIDataManager.getInstance().register(ability)
            ability.getID()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func releaseAbility(id: Int64): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None => throw BusinessException(ERROR_CODE_INNER, "No such Ability: " + id.toString())
        case Some(ability) => ABILITY_LOG.info("Release abilityContext end")
    }
    FFIDataManager.getInstance().releaseData(id)
    ABILITY_LOG.info("Release ability end")
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnStart(id: Int64, wantHandle: WantHandle, launchParam: CJLaunchParam): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) =>
            let want = Want(wantHandle)
            ability.setLaunchWant(want)
            ability.setLastRequestWant(want)

            let launchReason = unsafe { LaunchReason.parse(launchParam.launchReason) }
            let lastExitReason = unsafe { LastExitReason.parse(launchParam.lastExitReason) }
            let param: LaunchParam = LaunchParam(
                launchParam.lastExitMessage.toString(),
                launchReason: launchReason,
                lastExitReason: lastExitReason
            )
            ability.onCreate(want, param)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnStop(id: Int64): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) => ability.onDestroy()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnSceneCreated(id: Int64, windowStageHandle: WindowStageHandle): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) =>
            let windowStage = WindowStage(windowStageHandle)
            ability.context.windowStage_ = windowStage
            ability.onWindowStageCreate(windowStage)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnSceneRestored(id: Int64, windowStageHandle: WindowStageHandle): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) =>
            let windowStage = WindowStage(windowStageHandle)
            ability.context.windowStage_ = windowStage
            ability.onWindowStageRestore(windowStage)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnSceneDestroyed(id: Int64): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) =>
            ability.context.windowStage_ = None
            ability.onWindowStageDestroy()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnSceneWillDestroy(id: Int64, windowStageHandle: WindowStageHandle): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) =>
            let windowStage = WindowStage(windowStageHandle)
            ability.context.windowStage_ = windowStage
            ability.onWindowStageWillDestroy(windowStage)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnForeground(id: Int64, wantHandle: WantHandle): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) =>
            let want = Want(wantHandle)
            ability.setLastRequestWant(want)
            ability.onForeground()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnBackground(id: Int64): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) => ability.onBackground()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnBackPress(id: Int64): Bool {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) => ability.onBackPressed()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnConfigurationUpdated(id: Int64, _: CJConfiguration): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) => ()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnNewWant(id: Int64, wantHandle: WantHandle, launchParams: CJLaunchParam): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) =>
            let want = Want(wantHandle)
            ability.setLastRequestWant(want)

            let launchReason = unsafe { LaunchReason.parse(launchParams.launchReason) }
            let lastExitReason = unsafe { LastExitReason.parse(launchParams.lastExitReason) }
            let param: LaunchParam = LaunchParam(
                launchParams.lastExitMessage.toString(),
                launchReason: launchReason,
                lastExitReason: lastExitReason
            )
            ability.onNewWant(want, param)
    }
}

@C
func abilityDump(id: Int64, params: VectorStringHandle): VectorStringHandle {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None => return FFIVectorString(0).getNativeHandle()
        case Some(ability) =>
            var unsafeParams = FFIVectorString(params)
            var paramsSize = unsafeParams.getSize()
            let arrayParams = Array<String>(paramsSize, repeat: "")
            for (i in 0..paramsSize) {
                arrayParams[i] = unsafeParams.getElement(i)
            }
            let info = ability.onDump(arrayParams)
            let vecFfi = FFIVectorString(info.size)
            for (i in 0..info.size) {
                vecFfi.setElement(i, info[i])
            }
            return vecFfi.getNativeHandle()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnContinue(id: Int64, params: CString): Int32 {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) =>
            let jsonValue = jsonStringUnWrapper(params.toString())
            let res = ability.onContinue(jsonValue.toString())
            return res.getValue()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityInit(id: Int64, abilityHandle: AbilityHandle): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) => ability.abilityInit(abilityHandle)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnConfigurationUpdate(id: Int64, configuration: CConfiguration): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) => unsafe { configuration.free() }
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnMemoryLevel(id: Int64, _: Int32): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) => ()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnPrepareTerminate(id: Int64): Bool {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) => ability.onPrepareToTerminate()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnSaveState(id: Int64, reason: Int32, params: CString): CJNumberParmas {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) =>
            let reasonType = StateType.parse(reason)
            let wantParam = jsonStringUnWrapper(params.toString())
            let saveState = ability.onSaveState(reasonType, wantParam.toString())
            let jsonCString = unsafe {
                LibC.mallocCString(jsonObjectWrapper(wantParam).toString())
            }
            return CJNumberParmas(saveState.getValue(), jsonCString)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnShare(id: Int64, params: CString): CString {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) =>
            let wantParam = jsonStringUnWrapper(params.toString())
            ability.onShare(wantParam.toString())
            let jsonCString = unsafe {
                LibC.mallocCString(jsonObjectWrapper(wantParam).toString())
            }
            return jsonCString
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnContinueWithParams(id: Int64, params: CString): CJNumberParmas {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None =>
            ABILITY_LOG.error("No such Ability: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) =>
            let wantParam = jsonStringUnWrapper(params.toString())
            let continueResult = ability.onContinue(wantParam.toString())
            let jsonCString = unsafe {
                LibC.mallocCString(jsonObjectWrapper(wantParam).toString())
            }
            return CJNumberParmas(continueResult.getValue(), jsonCString)
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnCallRequest(id: Int64): Int64 {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) =>
            let callee = ability.onCallRequest()
            return callee.getID()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func abilityOnSetCalleeFlag(id: Int64, _: Bool): Unit {
    let optAbility = FFIDataManager.getInstance().getData<UIAbility>(id)
    match (optAbility) {
        case None => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(ability) => ()
    }
}

class UIAbilityImpl {}

/**
 * UIAbility is an application component that has the UI.
 * The UIAbility module, inherited from Ability, provides lifecycle callbacks such as component creation, destruction,
 * and foreground/background switching.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
]
public open class UIAbility <: Ability {
    private var remoteLaunchWant: Option<Want> = Option<Want>.None
    private var remoteLastRequestWant: Option<Want> = Option<Want>.None
    private var abilityContext: Option<UIAbilityContext> = Option<UIAbilityContext>.None
    private let callee_: Callee = Callee()
    private let impl_: UIAbilityImpl = UIAbilityImpl()
    @!Hide
    protected init() {}
    /**
     * Context of the UIAbility.
     *
     * @returns { UIAbilityContext } Returns the context of the UIAbility.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
    ]
    public mut prop context: UIAbilityContext {
        get() {
            match (abilityContext) {
                case None => throw BusinessException(ERROR_CODE_INNER, "Invalid context")
                case Some(value) => return value
            }
        }
        set(value) {
            abilityContext = value
        }
    }

    /**
     * Parameters for starting the UIAbility.
     *
     * @returns { Want } Returns the parameters for starting the UIAbility.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
    ]
    public mut prop launchWant: Want {
        get() {
            remoteLaunchWant.getOrThrow({=> BusinessException(ERROR_CODE_INNER, "Invalid LaunchWant")})
        }
        set(value) {
            remoteLaunchWant = value
        }
    }

    /**
     * Latest Want received through onCreate or onNewWant when the UIAbility is started for multiple times.
     *
     * @returns { Want } Returns the latest Want received through onCreate or onNewWant when the UIAbility is started
     * for multiple times.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
    ]
    public mut prop lastRequestWant: Want {
        get() {
            remoteLastRequestWant.getOrThrow({=> BusinessException(ERROR_CODE_INNER, "Invalid LastRequestWant")})
        }
        set(value) {
            remoteLastRequestWant = value
        }
    }

    prop callee: Callee {
        get() {
            callee_
        }
    }

    /**
     * Called to initialize the service logic when a UIAbility instance in the completely closed state is created.
     * In other words, a UIAbility instance enters this lifecycle callback from a cold start. This API returns the
     * result synchronously and does not support asynchronous callback.
     *
     * @param { Want } want - Want information, including the ability name and bundle name.
     * @param { LaunchParam } launchParam - Parameters for starting the UIAbility, and the reason for
     * the last abnormal exit.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
    ]
    public open func onCreate(want: Want, launchParam: LaunchParam): Unit {}

    /**
     * Called when a WindowStage is created for this UIAbility.
     *
     * @param { WindowStage } windowStage - WindowStage information.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
    ]
    public open func onWindowStageCreate(windowStage: WindowStage): Unit {}

    func onWindowStageWillDestroy(_: WindowStage): Unit {}

    /**
     * Called when the WindowStage is destroyed for this UIAbility.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
    ]
    public open func onWindowStageDestroy(): Unit {}

    /**
     * Called when the WindowStage is restored during the migration of this UIAbility, which is a multi-instance
     * ability.
     *
     */
    func onWindowStageRestore(_: WindowStage): Unit {}

    /**
     * Called to clear resources when this UIAbility is destroyed.
     * This API returns the result synchronously or uses a promise to return the result.
     * After the onDestroy() lifecycle callback is executed, the application may exit. Consequently,
     * the asynchronous function (for example, asynchronously writing data to the database) in onDestroy() may fail to
     * be executed. You can use the asynchronous lifecycle to ensure that the subsequent lifecycle continues only after
     * the asynchronous function in onDestroy() finishes the execution.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
    ]
    public open func onDestroy(): Unit {}

    /**
     * Triggered when the application transitions from the background to the foreground.
     * It is called between onWillForeground and onDidForeground.
     * It can be used to request system resources required, for example, requesting location services when the
     * application transitions to the foreground.
     * 
     * **NOTE**:
     * This API returns the result synchronously and does not support asynchronous callback.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
    ]
    public open func onForeground(): Unit {}

    @!Hide[isChecked: true]
    public open func onWillForeground(): Unit {}

    @!Hide[isChecked: true]
    public open func onDidForeground(): Unit {}

    /**
     * Triggered when the application transitions from the background to the foreground.
     * It is called between onWillForeground and onDidForeground.
     * It can be used to request system resources required, for example, requesting location services when the
     * application transitions to the foreground.
     * 
     * **NOTE**:
     * This API returns the result synchronously and does not support asynchronous callback.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
    ]
    public open func onBackground(): Unit {}

    @!Hide[isChecked: true]
    public open func onWillBackground(): Unit {}

    @!Hide[isChecked: true]
    public open func onDidBackground(): Unit {}

    func onContinue(_: String): OnContinueResult {
        OnContinueResult.Agree
    }

    /**
     * Called when a UIAbility instance that has undergone the following states is started again:
     * started in the foreground, running in the foreground, and switched to the background.
     *
     * The triggering of the onNewWant lifecycle of a UIAbility instance indicates that this launch is a hot launch.
     * Note that a hot launch does not necessarily trigger the onNewWant lifecycle.
     *
     * @param { Want } want - Want information, such as the ability name and bundle name.
     * @param { LaunchParam } launchParam - Reason for the UIAbility startup and the last abnormal exit.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
    ]
    public open func onNewWant(want: Want, launchParam: LaunchParam): Unit {}

    func onDump(_: Array<String>): Array<String> {
        return Array<String>()
    }

    func onSaveState(_: StateType, _: String): OnSaveResult {
        return OnSaveResult.RecoveryAgree
    }

    func onShare(_: String): Unit {}

    func onPrepareToTerminate(): Bool {
        return false
    }

    func onBackPressed(): Bool {
        return true
    }

    @!Hide[isChecked: true]
    public open func onCollaborate(_: String): CollaborateResult {
        throw Exception()
    }

    func onCallRequest(): Callee {
        return this.callee
    }

    /**
    * @throws { BusinessException } 16000050 - Internal error.
    */
    func abilityInit(remote: AbilityHandle): Unit {
        if (remote == 0) {
            ABILITY_LOG.error("Invalid remote Ability")
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }

        // Init abilityContext
        let nativeAbilityContextId = unsafe { FFIAbilityGetAbilityContext(remote) }
        var value = UIAbilityContext(nativeAbilityContextId)
        abilityContext = Option<UIAbilityContext>.Some(value)
        ABILITY_LOG.info("Bind remote UIAbilityContext successfully, the id is ${nativeAbilityContextId}")
    }

    func setLaunchWant(want: Want): Unit {
        remoteLaunchWant = Option<Want>.Some(want)
    }

    func setLastRequestWant(want: Want): Unit {
        remoteLastRequestWant = Option<Want>.Some(want)
    }
}

@C
func abilityCjFuncsRegister(result: CPointer<CJAbilityFuncs>): Unit {
    let atCFuncs = CJAbilityFuncs(
        createAbility,
        releaseAbility,
        abilityOnStart,
        abilityOnStop,
        abilityOnSceneCreated,
        abilityOnSceneRestored,
        abilityOnSceneDestroyed,
        abilityOnForeground,
        abilityOnBackground,
        abilityOnConfigurationUpdated,
        abilityOnNewWant,
        abilityDump,
        abilityOnContinue,
        abilityInit,
        abilityOnBackPress,
        abilityOnSceneWillDestroy,
        abilityOnConfigurationUpdate,
        abilityOnMemoryLevel,
        abilityOnPrepareTerminate,
        abilityOnSaveState,
        abilityOnShare,
        abilityOnContinueWithParams,
        abilityOnCallRequest,
        abilityOnSetCalleeFlag
    )
    unsafe { result.write(atCFuncs) }
}

foreign func RegisterCJAbilityFuncs(funcs: CFunc<(CPointer<CJAbilityFuncs>) -> Unit>): Unit

let REGISTER_ABILITY = unsafe { RegisterCJAbilityFuncs(abilityCjFuncsRegister) }

@!Hide[isChecked: true]
public enum CollaborateResult {
    @!Hide[isChecked: true]
    Accept
    |
    @!Hide[isChecked: true]
    Reject
    | ...
}