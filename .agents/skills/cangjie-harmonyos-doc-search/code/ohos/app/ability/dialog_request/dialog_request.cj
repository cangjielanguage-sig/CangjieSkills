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

package ohos.app.ability.dialog_request

import ohos.app.ability.want.{Want, WantHandle}
import ohos.labels.APILevel
import ohos.business_exception.BusinessException

const ERROR_CODE_INNER: Int32 = 16000050

/**
 * The modal bullet box requests the result code.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public enum ResultCode {
    /**
     * The modal bullet box requests succeeded.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    ResultOk
    | 
    /**
     * The modal bullet box requests Failed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    ResultCancel
    | ...

    /**
    * @throws { BusinessException } 16000050 - Internal error.
    */
    protected static func parse(value: Int32): ResultCode {
        match (value) {
            case 0 => ResultOk
            case 1 => ResultCancel
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }

    protected func getValue(): Int32 {
        match (this) {
            case ResultOk => 0
            case ResultCancel => 1
            case _ => throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        }
    }
}

/**
 * The result of requestDialogService with asynchronous callback.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public class RequestResult {
    /**
     * The request result passed in by the user.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var result: ResultCode

    /**
     * The request additional want data passed in by the user.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var want: Want

    protected init(result: ResultCode, want!: Want = Want()) {
        this.result = result
        this.want = want
    }
}

@C
protected struct CJDialogRequestResult {
    protected CJDialogRequestResult(
        protected let result: Int32,
        protected let wantHandle: WantHandle
    ) {}
}
