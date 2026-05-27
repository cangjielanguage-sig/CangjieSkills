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

package ohos.application.error_observer

import std.collection.HashMap
import ohos.labels.APILevel

/**
 * Error object.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public class ErrorObject {
    /**
     * Error object name.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public let name: String
    /**
     * Error object message.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public let message: String
    /**
     * Error object stack.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public let stack: Option<String>

    init(name: String, message: String, stack!: Option<String> = None) {
        this.name = name
        this.message = message
        this.stack = stack
    }

    init(ret: CErrorObject) {
        this.name = ret.name.toString()
        this.message = ret.message.toString()
        if (ret.stack.isEmpty()) {
            this.stack = None
        } else {
            this.stack = Some(ret.stack.toString())
        }
    }
}

/**
 * The observer will be called by system when an error occurs.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public class ErrorObserver {
    /**
     * Will be called when the js runtime throws an exception which doesn't caught by user.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var onUnhandledException: (String) -> Unit
    /**
     * Will be called when the js runtime throws an exception which doesn't caught by user.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var onException: Option<(ErrorObject) -> Unit>

    /**
     * ErrorObserver constructor.
     *
     * @param { (String) -> Unit } onUnhandledException - Will be called when the js runtime throws an exception which
     * doesn't caught by user.
     * @param { Option<(ErrorObject) -> Unit> } [onException] - Will be called when the js runtime throws an exception
     * which doesn't caught by user. The default value is None.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public init(
        onUnhandledException: (String) -> Unit,
        onException!: Option<(ErrorObject) -> Unit> = None
    ) {
        this.onUnhandledException = onUnhandledException
        this.onException = onException
    }
}

let ERROR_CODE_MAP: HashMap<Int32, String> = HashMap<Int32, String>(
    (401, "Parameter error."),
    (16000003, "Id does not exist.")
)

protected func getErrorInfo(code: Int32): String {
    if (ERROR_CODE_MAP.contains(code)) {
        return ERROR_CODE_MAP[code]
    } else {
        return "Unknown error"
    }
}
