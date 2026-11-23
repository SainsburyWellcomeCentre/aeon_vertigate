---
uid: Aeon.VertiGate.Torque
---

The value is a current limit on the servo, masked to the lower 7 bits. One count is 0.36 kgf·mm. The reply carries the value that the device applied, and not the value that you wrote.

A write to this register switches the motor off and on. The gate thus drops for a moment if it holds a position. The motor stays off if [MotorState](xref:Aeon.VertiGate.MotorState) is [Disabled](xref:Aeon.VertiGate.MotorStatus.Disabled).
