---
uid: Aeon.VertiGate.Control
---

Write one bit to run one command. A write that sets both bits of a pair gives an error reply.

A read reports the state, not the last command. It gives [EnableMotor](xref:Aeon.VertiGate.ControlFlags.EnableMotor) while the motor is on, [EnablePositionEvent](xref:Aeon.VertiGate.ControlFlags.EnablePositionEvent) while [Position](xref:Aeon.VertiGate.Position) events are on, and [EnableTelemetryEvent](xref:Aeon.VertiGate.ControlFlags.EnableTelemetryEvent) while [ServoTelemetry](xref:Aeon.VertiGate.ServoTelemetry) events are on. [Stop](xref:Aeon.VertiGate.ControlFlags.Stop) and [Calibrate](xref:Aeon.VertiGate.ControlFlags.Calibrate) are commands, so a read never shows them.

The device keeps this state over a power cycle.
