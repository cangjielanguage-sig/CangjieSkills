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

package ohos.app.ability.ability_delegator_registry

import ohos.business_exception.{BusinessException, getUniversalErrorMsg}
import ohos.ffi.{RemoteDataLite, CArrString, releaseFFIData, FFIDataManager}
import ohos.app.ability.ui_ability.{UIAbility, Context, ApplicationContext}
import ohos.app.ability.want.{Want, WantHandle}
import ohos.app.ability.ability_stage.AbilityStage
import std.deriving.Derive
import std.collection.HashMap
import ohos.labels.APILevel

// ERRORCODE
const COMMON_FAILED: Int32 = 16000100
const INVALID_PARA: Int32 = 401
const ERROR_CODE_RESOLVE_ABILITY: Int32 = 16000001
const EERROR_CODE_INVALID_ABILITY_TYPE: Int32 = 16000002
const ERROR_CODE_NO_INVISIBLE_PERMISSION: Int32 = 16000004
const ERROR_CODE_STATIC_CFG_PERMISSION: Int32 = 16000005
const ERROR_CODE_CROSS_USER: Int32 = 16000006
const ERROR_CODE_CROWDTEST_EXPIRED: Int32 = 16000008
const ERROR_CODE_WUKONG_MODE: Int32 = 16000009
const ERROR_CODE_CONTINUATION_FLAG: Int32 = 16000010
const ERROR_CODE_INVALID_CONTEXT: Int32 = 16000011
const ERROR_CODE_CONTROLLED: Int32 = 16000012
const ERROR_CODE_EDM_CONTROLLED: Int32 = 16000013
const ERROR_CODE_INNER: Int32 = 16000050
const ERROR_CODE_NOT_TOP_ABILITY: Int32 = 16000053
const ERROR_CODE_FREE_INSTALL_TIMEOUT: Int32 = 16000055
const ERROR_CALLER_RELEASED: Int32 = 16200001

foreign func FFIAbilityDelegatorRegistryGetAbilityDelegator(): Int64

foreign func FFIAbilityDelegatorStartAbility(id: Int64, wantHandle: WantHandle): Int32

foreign func FFIAbilityDelegatorExecuteShellCommand(id: Int64, cmd: CString, timeoutSec: Int64): Int32

foreign func FFIGetExitCode(id: Int64): Int32

foreign func FFIGetStdResult(id: Int64): CString

foreign func FFIDump(id: Int64): CString

foreign func FFIAbilityDelegatorApplicationContext(id: Int64): Int32

foreign func FFIAbilityDelegatorFinishTest(id: Int64, msg: CString, code: Int64): Unit

foreign func FfiAbilityDelegatorRegistryGetArguments(): Int64

foreign func FfiAbilityDelegatorArgsGetTestBundleName(id: Int64, errCode: CPointer<Int32>): CString

foreign func FfiAbilityDelegatorArgsGetTestParam(id: Int64, errCode: CPointer<Int32>): CRecord

foreign func FfiAbilityDelegatorArgsGetTestCaseName(id: Int64, errCode: CPointer<Int32>): CString

foreign func FfiAbilityDelegatorArgsGetTestRunnerClassName(id: Int64, errCode: CPointer<Int32>): CString

@C
struct CJAbilityInfo {
    CJAbilityInfo(
        let abilityName: CString,
        let moduleName: CString
    ) {}
}

@C
struct CJAbilityStageInfo {
    CJAbilityStageInfo(
        let moduleName: CString,
        let srcEntrance: CString
    ) {}
}

/**
 * Describes all lifecycle states of an ability.
 */
@Derive[ToString, Equatable]
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public enum AbilityLifecycleState {
    /**
     * Ability is in invalid state.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Uninitialized
    |
    /**
     * Ability is in the created state.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Create
    |
    /**
     * Ability is in the foreground state.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Foreground
    |
    /**
     * Ability is in the background state.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Background
    |
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Destroy
    | ...

    /**
    * @throws { BusinessException } 16000050 - Internal error.
    */
    static func parse(mode: Int64): AbilityLifecycleState {
        match (mode) {
            case 0 => Uninitialized
            case 1 => Create
            case 2 => Foreground
            case 3 => Background
            case 4 => Destroy
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }
}

foreign {
    func FFIAbilityDelegatorDoAbilityForeground(id: Int64, abilityId: Int64, ret: CPointer<Bool>): Int32

    func FFIAbilityDelegatorDoAbilityBackground(id: Int64, abilityId: Int64, ret: CPointer<Bool>): Int32

    func FFIAbilityDelegatorGetCurrentTopAbility(id: Int64, abilityId: CPointer<Int64>): Int32

    func FFIAbilityDelegatorGetAbilityState(id: Int64, abilityId: Int64, state: CPointer<Int64>): Int32

    func FFIAbilityDelegatorPrint(id: Int64, msg: CString): Int32

    func FFIAbilityDelegatorAddAbilityMonitor(
        id: Int64, monitorId: Int64, abilityName: CString, moduleName: CString): Int32

    func FFIAbilityDelegatorRemoveAbilityMonitor(
        id: Int64, monitorId: Int64, abilityName: CString, moduleName: CString): Int32

    func FFIAbilityDelegatorWaitAbilityMonitor(id: Int64, monitorId: Int64, abilityInfo: CJAbilityInfo,
        abilityId: CPointer<Int64>): Int32

    func FFIAbilityDelegatorWaitAbilityMonitorWithTimeout(id: Int64, monitorId: Int64, abilityInfo: CJAbilityInfo,
        timeout: Int64, abilityId: CPointer<Int64>): Int32

    func FFIAbilityDelegatorAddAbilityStageMonitor(id: Int64, stageMonitorId: Int64, moduleName: CString,
        srcEntrance: CString): Int32

    func FFIAbilityDelegatorRemoveAbilityStageMonitor(id: Int64, stageMonitorId: Int64, moduleName: CString,
        srcEntrance: CString): Int32

    func FFIAbilityDelegatorWaitAbilityStageMonitor(id: Int64, stageMonitorId: Int64,
        abilityStageInfo: CJAbilityStageInfo, abilityStageId: CPointer<Int64>): Int32

    func FFIAbilityDelegatorWaitAbilityStageMonitorWithTimeout(id: Int64, stageMonitorId: Int64,
        abilityStageInfo: CJAbilityStageInfo, timeout: Int64, abilityStageId: CPointer<Int64>): Int32
}

let ERROR_MSG = HashMap<String, String>(
    [
        ("addAbilityMonitor", "Calling AddAbilityMonitor failed."),
        ("removeAbilityMonitor", "Calling RemoveAbilityMonitor failed."),
        ("waitAbilityMonitor", "Calling WaitAbilityMonitor failed."),
        ("getCurrentTopAbility", "Calling GetCurrentTopAbility failed."),
        ("doAbilityForeground", "Calling DoAbilityForeground failed."),
        ("doAbilityBackground", "Calling DoAbilityBackground failed."),
        ("addAbilityStageMonitor", "Calling AddAbilityStageMonitor failed."),
        ("removeAbilityStageMonitor", "Calling RemoveAbilityStageMonitor failed."),
        ("waitAbilityStageMonitor", "Calling WaitAbilityStageMonitor failed.")
    ]
)
let ERROR_CODE_MAP = HashMap<Int32, String>(
    (INVALID_PARA, "Parameter error."),
    (ERROR_CODE_RESOLVE_ABILITY, "The specified ability does not exist."),
    (EERROR_CODE_INVALID_ABILITY_TYPE, "Incorrect ability type."),
    (ERROR_CODE_NO_INVISIBLE_PERMISSION, "Cannot start an invisible component."),
    (ERROR_CODE_STATIC_CFG_PERMISSION, "The specified process does not have the permission."),
    (ERROR_CODE_CROSS_USER, "Cross-user operations are not allowed."),
    (ERROR_CODE_CROWDTEST_EXPIRED, "The crowdtesting application expires."),
    (ERROR_CODE_WUKONG_MODE, "An ability cannot be started or stopped in Wukong mode."),
    (ERROR_CODE_CONTINUATION_FLAG, "The call with the continuation and prepare continuation flag is forbidden."),
    (ERROR_CODE_INVALID_CONTEXT, "The context does not exist."),
    (ERROR_CODE_CONTROLLED, "The application is controlled."),
    (ERROR_CODE_EDM_CONTROLLED, "The application is controlled by EDM."),
    (ERROR_CODE_INNER, "Internal error."),
    (ERROR_CODE_NOT_TOP_ABILITY, "The ability is not on the top of the UI."),
    (ERROR_CODE_FREE_INSTALL_TIMEOUT, "Installation-free timed out."),
    (ERROR_CALLER_RELEASED, "The caller has been released.")
)

func getErrorMsg(code: Int32, funcName: String): String {
    if (let Some(v) <- getUniversalErrorMsg(code)) {
        return v
    } else if (code == COMMON_FAILED) {
        return ERROR_MSG[funcName]
    } else if (ERROR_CODE_MAP.contains(code)) {
        return ERROR_CODE_MAP[code]
    }
    return "Unknown error code ${code}"
}

func throwIfNotSuccess(code: Int32, funcName: String): Unit {
    if (code != 0) {
        let msg = getErrorMsg(code, funcName)
        throw BusinessException(code, msg)
    }
}

@C
struct CRecord {
    CRecord(
        let keys: CArrString,
        let values: CArrString
    ) {}

    func toHashMapAndFree(): HashMap<String, String> {
        let cjKeys = unsafe { getArrayStringAndFree(keys) }
        let cjValues = unsafe { getArrayStringAndFree(values) }
        return HashMap<String, String>(
            keys.size,
            {i => (cjKeys[i], cjValues[i])}
        )
    }
}

/**
 * A global register used to store the AbilityDelegator and AbilityDelegatorArgs objects registered
 * during application startup.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public class AbilityDelegatorRegistry {
    static var delegator_: ?AbilityDelegator = None
    static var delegatorArgs_: ?AbilityDelegatorArgs = None
    init() {}
    /**
     * Get the AbilityDelegator object of the application.
     *
     * @returns { AbilityDelegator } Return the AbilityDelegator object initialized when the application is started.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public static func getAbilityDelegator(): AbilityDelegator {
        match (delegator_) {
            case Some(v) => v
            case _ => unsafe {
                let res = AbilityDelegator(FFIAbilityDelegatorRegistryGetAbilityDelegator())
                delegator_ = res
                res
            }
        }
    }

    /**
     * Get unit test arguments stored in the AbilityDelegatorArgs object.
     *
     * @returns { AbilityDelegatorArgs } Return the previously registered AbilityDelegatorArgs object.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public static func getArguments(): AbilityDelegatorArgs {
        match (delegatorArgs_) {
            case Some(v) => v
            case _ => unsafe {
                let id = FfiAbilityDelegatorRegistryGetArguments()
                if (id < 0) {
                    throw BusinessException(ERROR_CODE_INNER, "Internal error.")
                }
                let res = AbilityDelegatorArgs(id)
                delegatorArgs_ = res
                res
            }
        }
    }
}

/**
 * A object that records the result of shell command executes.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public class ShellCmdResult <: RemoteDataLite {
    var exitCode_: ?Int32 = None
    var stdResult_: ?String = None
    init(id: Int64) {
        super(id)
    }

    ~init() {
        releaseFFIData(myDataId)
    }

    /**
     * the cmd standard result.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public mut prop stdResult: String {
        get() {
            if (let Some(v) <- stdResult_) {
                return v
            }
            let tempData = unsafe { FFIGetStdResult(this.getID()) }
            stdResult_ = tempData.toString()
            unsafe { LibC.free(tempData) }
            return stdResult_.getOrThrow()
        }
        set(v) {
            stdResult_ = v
        }
    }
    
    /**
     * shell cmd exec result.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public mut prop exitCode: Int32 {
        get() {
            if (let Some(v) <- exitCode_) {
                return v
            }
            exitCode_ = unsafe { FFIGetExitCode(this.getID()) }
            return exitCode_.getOrThrow()
        }
        set(v) {
            exitCode_ = v
        }
    }
}

/**
 * A global test utility interface used for adding AbilityMonitor objects and control lifecycle states of abilities.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public class AbilityDelegator <: RemoteDataLite {
    init(id: Int64) {
        super(id)
    }

    ~init() {
        releaseFFIData(myDataId)
    }

    /**
     * Start a new ability.
     *
     * @param { Want } want - Indicates the ability to start
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
        throwexception: true,
        workerthread: true
    ]
    public func startAbility(want: Want): Unit {
        let wantHandle = want.createWantHandle()
        let errorCode = unsafe { FFIAbilityDelegatorStartAbility(this.getID(), wantHandle) }
        unsafe { Want.releaseWantHandle(wantHandle) }
        ABILITY_DELEGATOR_LOG.debug("startAbility: errorCode is ${errorCode}")
        throwIfNotSuccess(errorCode, "startAbility")
    }

    /**
     * Execute the given command in the aa tools side.
     *
     * @param { String } cmd - Shell command
     * @param { Int64 } [timeoutSecs] - Timeout, in seconds.
     * @returns { ShellCmdResult } Returns the result of the shell command execution.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        workerthread: true
    ]
    public func executeShellCommand(cmd: String, timeoutSecs!: Int64 = 0): ShellCmdResult {
        unsafe {
            var cCmd = LibC.mallocCString(cmd)
            let shellCmdResultID = FFIAbilityDelegatorExecuteShellCommand(this.getID(), cCmd, timeoutSecs)
            ABILITY_DELEGATOR_LOG.info("AbilityDelegator: Start Execute Shell Command: ${shellCmdResultID}")
            LibC.free(cCmd)
            return ShellCmdResult(Int64(shellCmdResultID))
        }
    }

    /**
     * Obtain the application context.
     *
     * @returns { Context } Returns the app Context.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public func getAppContext(): Context {
        unsafe {
            let appContextID = FFIAbilityDelegatorApplicationContext(this.getID())
            ABILITY_DELEGATOR_LOG.info("AbilityDelegator: Start get Application Context")
            return ApplicationContext(Int64(appContextID))
        }
    }

    /**
     * Finish the test and print log information to the unit testing console.
     * The total length of the log information to be printed cannot exceed 1000 characters.
     *
     * @param { String } msg - Log information.
     * @param { Int64 } code - Result code.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        workerthread: true
    ]
    public func finishTest(msg: String, code: Int64): Unit {
        unsafe {
            var cMsg = LibC.mallocCString(msg)
            FFIAbilityDelegatorFinishTest(this.getID(), cMsg, code)
            ABILITY_DELEGATOR_LOG.info("AbilityDelegator: Finish Test")
            LibC.free(cMsg)
        }
    }

    /**
     * Add an AbilityMonitor object for monitoring the lifecycle state changes of the specified ability in this process.
     *
     * @param { AbilityMonitor } monitor - AbilityMonitor objects.
     * @throws { BusinessException } 16000100 - Calling AddAbilityMonitor failed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true,
        workerthread: true
    ]
    public func addAbilityMonitor(monitor: AbilityMonitor): Unit {
        var errorCode: Int32 = COMMON_FAILED
        unsafe {
            try (abilityName = LibC.mallocCString(monitor.abilityName).asResource(), moduleName = LibC
                .mallocCString(monitor.moduleName)
                .asResource()) {
                errorCode = FFIAbilityDelegatorAddAbilityMonitor(this.getID(), monitor.getID(), abilityName.value,
                    moduleName.value)
            }
        }
        throwIfNotSuccess(errorCode, "addAbilityMonitor")
    }

    /**
     * Remove a specified AbilityMonitor object from the application memory.
     *
     * @param { AbilityMonitor } monitor - AbilityMonitor object.
     * @throws { BusinessException } 16000100 - Calling RemoveAbilityMonitor failed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true,
        workerthread: true
    ]
    public func removeAbilityMonitor(monitor: AbilityMonitor): Unit {
        var errorCode: Int32 = COMMON_FAILED
        unsafe {
            try (abilityName = LibC.mallocCString(monitor.abilityName).asResource(), moduleName = LibC
                .mallocCString(monitor.moduleName)
                .asResource()) {
                errorCode = FFIAbilityDelegatorRemoveAbilityMonitor(this.getID(), monitor.getID(), abilityName.value,
                    moduleName.value)
            }
        }
        throwIfNotSuccess(errorCode, "removeAbilityMonitor")
    }

    /**
     * Wait for and returns the Ability object that matches the conditions set in the given AbilityMonitor.
     *
     * @param { AbilityMonitor } monitor - AbilityMonitor object.
     * @param { Int64 } [timeout] - Maximum wait time, in milliseconds.
     * @returns { UIAbility } Returns the Ability object that matches the conditions.
     * @throws { BusinessException } 16000050 - Internal error.
     * @throws { BusinessException } 16000100 - Calling WaitAbilityMonitor failed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true,
        workerthread: true
    ]
    public func waitAbilityMonitor(monitor: AbilityMonitor, timeout!: Int64 = 5000): UIAbility {
        var errorCode: Int32 = COMMON_FAILED
        var abilityId: Int64 = 0i64
        unsafe {
            try (abilityName = LibC.mallocCString(monitor.abilityName).asResource(), moduleName = LibC
                .mallocCString(monitor.moduleName)
                .asResource()) {
                let abilityInfo = CJAbilityInfo(abilityName.value, moduleName.value)
                errorCode = FFIAbilityDelegatorWaitAbilityMonitorWithTimeout(this.getID(), monitor.getID(), abilityInfo,
                    timeout, inout abilityId)
            }
        }

        throwIfNotSuccess(errorCode, "waitAbilityMonitor")
        let optAbility = FFIDataManager.getInstance().getData<UIAbility>(abilityId)
        return optAbility.getOrThrow {=> BusinessException(ERROR_CODE_INNER, "Internal error.")}
    }

    /**
     * Add an AbilityStageMonitor object for monitoring the lifecycle state changes of the specified abilityStage in
     * this process.
     *
     * @param { AbilityStageMonitor } monitor - AbilityStageMonitor object.
     * @throws { BusinessException } 16000100 - Calling AddAbilityStageMonitor failed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true,
        workerthread: true
    ]
    public func addAbilityStageMonitor(monitor: AbilityStageMonitor): Unit {
        var errorCode: Int32 = COMMON_FAILED
        unsafe {
            try (moduleName = LibC.mallocCString(monitor.moduleName).asResource(), srcEntrance = LibC
                .mallocCString(monitor.srcEntrance)
                .asResource()) {
                errorCode = FFIAbilityDelegatorAddAbilityStageMonitor(this.getID(), monitor.getID(), moduleName.value,
                    srcEntrance.value)
            }
        }

        throwIfNotSuccess(errorCode, "addAbilityStageMonitor")
    }

    /**
     * Remove a specified AbilityStageMonitor object from the application memory.
     *
     * @param { AbilityStageMonitor } monitor - AbilityStageMonitor object.
     * @throws { BusinessException } 16000100 - Calling RemoveAbilityStageMonitor failed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true,
        workerthread: true
    ]
    public func removeAbilityStageMonitor(monitor: AbilityStageMonitor): Unit {
        var errorCode: Int32 = COMMON_FAILED
        unsafe {
            try (moduleName = LibC.mallocCString(monitor.moduleName).asResource(), srcEntrance = LibC
                .mallocCString(monitor.srcEntrance)
                .asResource()) {
                errorCode = FFIAbilityDelegatorRemoveAbilityStageMonitor(this.getID(), monitor.getID(), moduleName.value,
                    srcEntrance.value)
            }
        }

        throwIfNotSuccess(errorCode, "removeAbilityStageMonitor")
    }

    /**
     * Wait for and returns the AbilityStage object that matches the conditions set in the given AbilityStageMonitor.
     *
     * @param { AbilityStageMonitor } monitor - AbilityStageMonitor object.
     * @param { Int64 } [timeout] - Maximum wait time, in milliseconds.
     * @returns { AbilityStage } Returns the AbilityStage object that matches the conditions.
     * @throws { BusinessException } 16000050 - Internal error.
     * @throws { BusinessException } 16000100 - Calling WaitAbilityStageMonitor failed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true,
        workerthread: true
    ]
    public func waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout!: Int64 = 5000): AbilityStage {
        var abilityStageId: Int64 = 0i64
        var errorCode: Int32 = COMMON_FAILED
        unsafe {
            try (moduleName = LibC.mallocCString(monitor.moduleName).asResource(), srcEntrance = LibC
                .mallocCString(monitor.srcEntrance)
                .asResource()) {
                let abilityStageInfo = CJAbilityStageInfo(moduleName.value, srcEntrance.value)
                errorCode = FFIAbilityDelegatorWaitAbilityStageMonitorWithTimeout(this.getID(), monitor.getID(),
                    abilityStageInfo, timeout, inout abilityStageId)
            }
        }

        throwIfNotSuccess(errorCode, "waitAbilityStageMonitor")
        let optAbilityStage = FFIDataManager.getInstance().getData<AbilityStage>(abilityStageId)
        return optAbilityStage.getOrThrow {=> BusinessException(ERROR_CODE_INNER, "Internal error.")}
    }

    /**
     * Prints log information to the unit testing console.
     * The total length of the log information to be printed cannot exceed 1000 characters.
     *
     * @param { String } msg - Log information.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        workerthread: true
    ]
    public func print(msg: String): Unit {
        var errorCode: Int32 = COMMON_FAILED
        unsafe {
            try (cMsg = LibC.mallocCString(msg).asResource()) {
                errorCode = FFIAbilityDelegatorPrint(this.getID(), cMsg.value)
            }
        }
        throwIfNotSuccess(errorCode, "print")
    }

    /**
     * Obtain the lifecycle state of a specified ability.
     *
     * @param { UIAbility } ability - The Ability object.
     * @returns { AbilityLifecycleState } Returns the state of the Ability object.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public func getAbilityState(ability: UIAbility): AbilityLifecycleState {
        var errorCode: Int32 = COMMON_FAILED
        var state: Int64 = -1i64
        unsafe {
            errorCode = FFIAbilityDelegatorGetAbilityState(this.getID(), ability.getID(), inout state)
        }

        throwIfNotSuccess(errorCode, "getAbilityState")
        return AbilityLifecycleState.parse(state)
    }

    /**
     * Obtain the ability that is currently being displayed in this process.
     *
     * @returns { UIAbility } Returns the UIAbility object that is currently on top.
     * @throws { BusinessException } 16000050 - Internal error.
     * @throws { BusinessException } 16000100 - Calling GetCurrentTopAbility failed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true,
        workerthread: true
    ]
    public func getCurrentTopAbility(): UIAbility {
        var errorCode: Int32 = COMMON_FAILED
        var abilityId: Int64 = 0i64
        unsafe {
            errorCode = FFIAbilityDelegatorGetCurrentTopAbility(this.getID(), inout abilityId)
        }

        throwIfNotSuccess(errorCode, "getCurrentTopAbility")
        let optAbility = FFIDataManager.getInstance().getData<UIAbility>(abilityId)
        return optAbility.getOrThrow {=> BusinessException(ERROR_CODE_INNER, "Internal error.")}
    }

    /**
     * Invoke the Ability.onForeground() callback of a specified ability without changing its lifecycle state.
     *
     * @param { UIAbility } ability - The ability object.
     * @throws { BusinessException } 16000100 - Calling DoAbilityForeground failed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true,
        workerthread: true
    ]
    public func doAbilityForeground(ability: UIAbility): Unit {
        var errorCode: Int32 = COMMON_FAILED
        var ret: Bool = false;
        unsafe {
            errorCode = FFIAbilityDelegatorDoAbilityForeground(this.getID(), ability.getID(), inout ret)
        }
        if (!ret) {
            throwIfNotSuccess(errorCode, "doAbilityForeground")
        }
        return
    }

    /**
     * Invoke the Ability.onBackground() callback of a specified ability without changing its lifecycle state.
     *
     * @param { UIAbility } ability - The ability object.
     * @throws { BusinessException } 16000100 - Calling DoAbilityBackground failed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core",
        throwexception: true,
        workerthread: true
    ]
    public func doAbilityBackground(ability: UIAbility): Unit {
        var errorCode: Int32 = COMMON_FAILED
        var ret: Bool = false
        unsafe {
            errorCode = FFIAbilityDelegatorDoAbilityBackground(this.getID(), ability.getID(), inout ret)
        }
        if (!ret) {
            throwIfNotSuccess(errorCode, "doAbilityBackground")
        }
        return
    }
}

/**
 * Store unit testing-related parameters, including test case names, and test runner name.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public class AbilityDelegatorArgs <: RemoteDataLite {
    var bundleName_: ?String = None
    var parameters_: ?HashMap<String, String> = None
    var testCaseNames_: ?String = None
    var testRunnerClassName_: ?String = None

    init(id: Int64) {
        super(id)
    }

    ~init() {
        releaseFFIData(myDataId)
    }

    /**
     * the bundle name of the application being tested.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public mut prop bundleName: String {
        get() {
            if (let Some(v) <- bundleName_) {
                return v
            }
            var code: Int32 = 0
            unsafe {
                let cBundleName = FfiAbilityDelegatorArgsGetTestBundleName(getID(), inout code)
                if (code != 0) {
                    ABILITY_DELEGATOR_LOG.error("AbilityDelegatorArgs get bundleName failed")
                    return ""
                }
                bundleName_ = cBundleName.toString()
                LibC.free(cBundleName)
                return bundleName_ ?? ""
            }
        }
        set(v) {
            bundleName_ = v
        }
    }

    /**
     * the parameters used for unit testing.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public mut prop parameters: HashMap<String, String> {
        get() {
            if (let Some(v) <- parameters_) {
                return v
            }
            var code: Int32 = 0
            unsafe {
                let cParameters = FfiAbilityDelegatorArgsGetTestParam(getID(), inout code)
                if (code != 0) {
                    ABILITY_DELEGATOR_LOG.error("AbilityDelegatorArgs get parameters failed")
                    return HashMap<String, String>()
                }
                parameters_ = cParameters.toHashMapAndFree()
                return parameters_ ?? HashMap<String, String>()
            }
        }
        set(v) {
            parameters_ = v
        }
    }

    /**
     * the class names of all test cases.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public mut prop testCaseNames: String {
        get() {
            if (let Some(v) <- testCaseNames_) {
                return v
            }
            var code: Int32 = 0
            unsafe {
                let cTestCaseNames = FfiAbilityDelegatorArgsGetTestCaseName(getID(), inout code)
                if (code != 0) {
                    ABILITY_DELEGATOR_LOG.error("AbilityDelegatorArgs get testCaseNames failed")
                    return ""
                }
                testCaseNames_ = cTestCaseNames.toString()
                LibC.free(cTestCaseNames)
                return testCaseNames_ ?? ""
            }
        }
        set(v) {
            testCaseNames_ = v
        }
    }

    /**
     * the class name of the test runner used to execute test cases.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public mut prop testRunnerClassName: String {
        get() {
            if (let Some(v) <- testRunnerClassName_) {
                return v
            }
            var code: Int32 = 0
            unsafe {
                let cTestRunnerClassName = FfiAbilityDelegatorArgsGetTestRunnerClassName(getID(), inout code)
                if (code != 0) {
                    ABILITY_DELEGATOR_LOG.error("AbilityDelegatorArgs get testRunnerClassName failed")
                    return ""
                }
                testRunnerClassName_ = cTestRunnerClassName.toString()
                LibC.free(cTestRunnerClassName)
                return testRunnerClassName_ ?? ""
            }
        }
        set(v) {
            testRunnerClassName_ = v
        }
    }
}

unsafe func getArrayStringAndFree(arr: CArrString): Array<String> {
    let ptr = arr.head
    if (ptr.isNull()) {
        return Array<String>()
    }
    let size = arr.size
    let ret = Array<String>(
        size,
        {
            i =>
                let cString = ptr.read(i)
                let data = cString.toString()
                LibC.free(cString)
                data
        }
    )
    LibC.free<CString>(ptr)
    return ret
}
