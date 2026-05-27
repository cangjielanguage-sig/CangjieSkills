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

package ohos.app.ability.ability_constant

import std.deriving.Derive
import ohos.labels.{APILevel, Hide}
import ohos.business_exception.BusinessException

const ERROR_CODE_INNER: Int32 = 16000050

/**
 * Defines the parameters for starting an ability.
 * The parameter values are automatically passed in by the system when the ability is started. You do not need to
 * change the values.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public class LaunchParam {
    /**
     * Ability launch reason, which is an enumerated type.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var launchReason: LaunchReason

    @!Hide[isChecked: true]
    internal var launchReasonMessage: Option<String> = None

    /**
     * Reason for the last exit, which is an enumerated type.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var lastExitReason: LastExitReason

    var lastExitMessage: String = ""

    @!Hide[isChecked: true]
    internal var lastExitDetailInfo: Option<LastExitDetailInfo> = None

    protected init(
        launchReason!: LaunchReason = LaunchReason.Unknown,
        lastExitReason!: LastExitReason = LastExitReason.Normal
    ) {
        this.launchReason = launchReason
        this.lastExitReason = lastExitReason
    }

    protected init(lastExitMessage: String, launchReason!: LaunchReason = LaunchReason.Unknown,
        lastExitReason!: LastExitReason = LastExitReason.Normal) {
        this.lastExitMessage = lastExitMessage
        this.launchReason = launchReason
        this.lastExitReason = lastExitReason
    }
}

/**
 * Enumerates the initial ability launch reasons.
 * You can use it together with the value of launchReason in
 * onCreate(want, launchParam) of the UIAbility to complete different operations.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public enum LaunchReason {
    /**
     * Unknown reason.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Unknown
    |
    /**
     * The ability is started by calling startAbility.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    StartAbility
    |
    /**
     * The ability is started by calling startAbilityByCall.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Call
    |
    /**
     * The ability is started by means of cross-device migration.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Continuation
    |
    /**
     * The ability is automatically started when the application is restored from a fault.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    AppRecovery
    |
    @!Hide[isChecked: true]
    Share
    |
    @!Hide[isChecked: true]
    AutoStartup
    |
    @!Hide[isChecked: true]
    InsightIntent
    |
    @!Hide[isChecked: true]
    PrepareContinuation
    |
    @!Hide[isChecked: true]
    Preload
    | ...

    /**
    * @throws { BusinessException } 16000050 - Internal error.
    */
    protected static func parse(value: Int32): LaunchReason {
        match (value) {
            case 0 => Unknown
            case 1 => StartAbility
            case 2 => Call
            case 3 => Continuation
            case 4 => AppRecovery
            case _ => ABILITY_LOG.error("LaunchReason: The native layer returns a value ${value} outside the specified range.")
                      Unknown
        }
    }

    protected func getValue(): Int32 {
        match (this) {
            case Unknown => 0
            case StartAbility => 1
            case Call => 2
            case Continuation => 3
            case AppRecovery => 4
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }
}

/**
 * Enumerates the reasons for the last exit.
 * You can use it together with the value of lastExitReason in
 * onCreate(want, launchParam) of the UIAbility to complete different operations.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public enum LastExitReason {
    /**
     * Unknown reason.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Unknown
    |
    @!Hide[isChecked: true]
    AbilityNotResponding
    |
    /**
     * The ability exits normally because the user closes the application.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Normal
    |
    /**
     * The ability exits due to abnormal signals on the local host.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    CppCrash
    |
    @!Hide[isChecked: true]
    JsError
    |
    /**
     * The ability exits because watchdog detects that the application is frozen.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    AppFreeze
    |
    @!Hide[isChecked: true]
    PerformanceControl
    |
    @!Hide[isChecked: true]
    ResourceControl
    |
    @!Hide[isChecked: true]
    Upgrade
    |
    @!Hide[isChecked: true]
    UserRequest
    |
    @!Hide[isChecked: true]
    Signal
    | ...

    /**
    * @throws { BusinessException } 16000050 - Internal error.
    */
    protected static func parse(value: Int32): LastExitReason {
        match (value) {
            case 0 => Unknown
            case 2 => Normal
            case 3 => CppCrash
            case 5 => AppFreeze
            case _ =>
                ABILITY_LOG.info("No corresponding LastExitReason: ${value}")
                Unknown
        }
    }

    protected func getValue(): Int32 {
        match (this) {
            case Unknown => 0
            case Normal => 2
            case CppCrash => 3
            case AppFreeze => 5
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }
}

/**
 * Enumerates the ability continuation results.
 * You can use it together with <code>onContinue(wantParam)</code> of the UIAbility to complete different
 * operations.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public enum OnContinueResult {
    /**
     * The ability continuation is accepted.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Agree
    |
    /**
     * The ability continuation is rejected.
     * If the application is abnormal in onContinue, which results in abnormal display during data restoration, this
     * error code is returned.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Reject
    |
    /**
     * The version does not match.
     * The application on the initiator can obtain the version of the target application from onContinue. If the
     * ability continuation cannot be performed due to version mismatch, this error code is returned.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    Mismatch
    | ...

    protected func getValue(): Int32 {
        match (this) {
            case Agree => 0
            case Reject => 1
            case Mismatch => 2
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }
}

protected const WINDOW_MODE_UNDEFINED: Int32 = 0

/**
 * Enumerates the window mode when the ability is started.
 * It can be used together with startAbility to specify the window mode for starting the ability.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public enum WindowMode {
    @!Hide[isChecked: true]
    WindowModeUndefined
    |
    /**
     * Full screen mode. It takes effect only on 2-in-1 devices and tablets.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    WindowModeFullscreen
    |
    /**
     * Primary screen (left screen in the case of horizontal orientation) in split-screen mode. It is valid only in
     * intra-app redirection scenarios.
     * It takes effect only on foldable devices and tablets.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    WindowModeSplitPrimary
    |
    /**
     * Secondary screen (right screen in the case of horizontal orientation) in split-screen mode. It is valid only in
     * intra-app redirection scenarios.
     * It takes effect only on foldable devices and tablets.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    WindowModeSplitSecondary
    |
    @!Hide[isChecked: true]
    WindowModeFloating
    | ...

    /**
    * @throws { BusinessException } 16000050 - Internal error.
    */
    protected static func parse(value: Int32): WindowMode {
        match (value) {
            case 1 => WindowModeFullscreen
            case 100 => WindowModeSplitPrimary
            case 101 => WindowModeSplitSecondary
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }

    protected func getValue(): Int32 {
        match (this) {
            case WindowModeFullscreen => 1
            case WindowModeSplitPrimary => 100
            case WindowModeSplitSecondary => 101
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }
}

/**
 * Enumerates the memory levels. You can use it in onMemoryLevel(level) of the UIAbility to complete
 * different operations.
 */
@Derive[ToString, Equatable]
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public enum MemoryLevel {
    /**
     * Moderate memory usage.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    MemoryLevelModerate
    |
    /**
     * Low memory usage.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    MemoryLevelLow
    |
    /**
     * High memory usage.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    MemoryLevelCritical
    | ...

    /**
    * @throws { BusinessException } 16000050 - Internal error.
    */
    protected static func parse(value: Int32): MemoryLevel {
        match (value) {
            case 0 => MemoryLevelModerate
            case 1 => MemoryLevelLow
            case 2 => MemoryLevelCritical
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }

    protected func getValue(): Int32 {
        match (this) {
            case MemoryLevelModerate => 0
            case MemoryLevelLow => 1
            case MemoryLevelCritical => 2
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }
}

@Derive[ToString, Equatable]
protected enum StateType {
    Continuation
    | AppRecovery
    | ...

    protected func getValue(): Int32 {
        match (this) {
            case Continuation => 0
            case AppRecovery => 1
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }

    /**
    * @throws { BusinessException } 16000050 - Internal error.
    */
    protected static func parse(value: Int32): StateType {
        match (value) {
            case 0 => Continuation
            case 1 => AppRecovery
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }
}

@Derive[ToString, Equatable]
protected enum OnSaveResult {
    AllAgree
    | ContinuationReject
    | ContinuationMismatch
    | RecoveryAgree
    | RecoveryReject
    | AllReject
    | ...

    protected func getValue(): Int32 {
        match (this) {
            case AllAgree => 0
            case ContinuationReject => 1
            case ContinuationMismatch => 2
            case RecoveryAgree => 3
            case RecoveryReject => 4
            case AllReject => 5
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }
}

@!Hide[isChecked: true]
class LastExitDetailInfo {
    init() {}
}