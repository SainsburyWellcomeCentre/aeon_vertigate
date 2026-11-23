---
uid: Aeon.VertiGate.Speed
---

The value maps onto the profile velocity of the Dynamixel servo. One count adds 0.38 mm/s.

A write of 0 gives the slowest motion, and not a stop, because the servo receives this value plus a fixed offset of 60. Use [Stop](xref:Aeon.VertiGate.ControlFlags.Stop) to stop a movement.

A write to this register switches the motor off and on. The gate thus drops for a moment if it holds a position. The motor stays off if [MotorState](xref:Aeon.VertiGate.MotorState) is [Disabled](xref:Aeon.VertiGate.MotorStatus.Disabled).
